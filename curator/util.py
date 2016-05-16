from models import Histogram, Config
from mongoengine.errors import OperationError
import json, re
from config import PATH, PW


def setup(debug=False):
    conf = Config.objects.first()

    if not conf:
        Config(password=PW).save()

    with open(PATH + "/config_test.JSON") as data_file:
        data = json.load(data_file)

    key_list = dict(data['sort_keys'])

    return key_list


# def make_tags(possibleTags, debug=False):
#     tag_list = []
#     for category in possibleTags:
#
#         for item in possibleTags[category]:
#             if debug:
#                 print "JSON Check"
#                 print 'category = ', category
#                 print "value = " + item['value']
#                 print "pretty =" + item['pretty']
#             try:
#                 tag = Tag.objects(category=category, value=item['value']).modify(upsert=True, new=True,
#                                                                                  set__pretty=item['pretty'])
#                 if debug:
#                     print "Tag Check:"
#                     print '\n' \
#                           'tag category    {0}\n' \
#                           'value       {1}\n' \
#                           'pretty      {2}\n'.format(tag.category, tag.value, tag.pretty)
#
#                 tag_list.append(tag)
#             except Exception as e:
#                 print e
#                 return False
#
#     if debug:
#         print "{0} Tags inserted from JSON file.".format(len(tag_list))
#         print "{0} Tags now present in DB.".format(Tag.objects().count())
#     return True


# def insert_keys(sort_keys, debug=False):
#     print type(sort_keys)
#     print sort_keys
#     for item in sort_keys:
#         SortKey.objects()
#
#     return [dict(item.to_mongo()) for item in SortKey.objects()]


# def report():
#     print "Histograms {0} \n" \
#           "Tags       {1} \n" \
#           "Filters    {2} \n" \
#           "".format(Histogram.objects().count(),
#                     Tag.objects().count(),
#                     Filter.objects().count())


# def build_regex(skl):
#     for item in skl:
#         if item.get('value'):
#             item['regex_value'] = re.compile(item['value'])
#         else:
#             item['regex_value'] = None
#     return skl
