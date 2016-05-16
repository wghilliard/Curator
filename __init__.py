from curator.tasks import master

from curator.util import setup


def start(debug, update):
    key_list = setup(debug)

    # master.delay(debug, update, key_list)
    master(debug, update, key_list)
    # setup(debug)
    # rm_2(debug, update)
    # report()
