__author__ = 'William Hilliard'

import re
import os
from pymongo.errors import *
from models import *
from __init__ import app, path
# from bson.objectid import ObjectId
import traceback
# from util import build_regex
from config import IGNORE, PATH


@app.task(name='tasks.master')
def master(debug, update, key_list):
    walked_items = dict()
    stats = {'added': 0, 'not_added': 0}

    if debug:
        print('path = {0}'.format(path))

    # built_key_list = build_regex(key_list)

    config_object = Config.objects().first()

    added_items = dict(config_object.to_mongo())['added']

    if debug: print "key_list: \n {0}".format(key_list)

    for directory in os.listdir(path):
        if directory not in IGNORE:
            try:
                tmp_directory = added_items[directory]
                stats['not_added'] += 1

            except KeyError:
                parse.delay(directory, os.path.join(PATH, directory), key_list)
                added_items[directory] = True
                stats['added'] += 1
    print added_items
    config_object['added'] = added_items

    config_object.save()
    print stats


@app.task(name='tasks.parse')
def parse(directory, fullPath, keys, debug=False):
    files = os.listdir(fullPath)
    # print keys
    print '############################'

    # print directory

    split = re.split('[R E S]', directory)

    # print split

    # Don't judge me. I didn't create the naming scheme, I just have to interpret it.
    run = 'Run ' + split[1][2:]
    if 'vent' in split[2]:
        type = 'event'
        entry = 'Event ' + split[2][4:]
    elif 'ubrun' in split[2]:
        type = 'subRun'
        entry = 'Subrun ' + split[2][5:]

    if debug:
        print "run = " + run
        print "entry = " + entry

    for filename in files:
        if filename not in IGNORE:
            filename_split = re.split('[_.]', filename)

            print filename_split

            # Populate the histogram dictionary.
            hist_dict = dict()
            tag_list = []
            hist_dict.update({'filename': filename,
                              'run': run,
                              'entry': entry,
                              'fullPath': os.path.join(fullPath, filename),
                              'tags': {}
                              })

            tags = dict()
            for item in filename_split:
                if item != "png" and (item not in IGNORE):
                    try:
                        value = keys[item]
                        tags[value] = item
                    except KeyError as e:
                        # tags[item] = True
                        print 'error {0}'.format(e)
            hist_dict.update({'tags': tags.copy()})
            hist_object = Histogram(**hist_dict).save()

            if hist_object:
                # Update Entry
                try:
                    entryObject = Entry.objects(name=entry, run=run, type=type).modify(upsert=True, new=True,
                                                                                       add_to_set__histograms=[
                                                                                           hist_object.id])
                except PyMongoError as e:
                    print traceback.format_exception()
                    print e

                    # Update Run
            if entryObject:

                if type in 'event':
                    try:
                        runObject = Run.objects(name=run).modify(upsert=True, new=True,
                                                                 add_to_set__events=[entryObject.id])
                    except PyMongoError as e:
                        print traceback.format_exception()
                        print e
                elif type in 'subRun':
                    try:
                        runObject = Run.objects(name=run).modify(upsert=True, new=True,
                                                                 add_to_set__subRuns=[entryObject.id])
                    except PyMongoError as e:
                        print traceback.format_exception()
                        print e
                print hist_dict

        else:
            pass
