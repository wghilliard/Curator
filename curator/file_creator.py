__author__ = 'wghilliard'

import itertools
import shutil
import os
from config import PATH

test_lists = [["RCE", "SSP", "PTB"],
              ["APA1", "APA2", "TSURU"],
              ["ADC", "Hits", "Triggers"],
              ["Mean", "Total", "Size"]]

final = itertools.product(*test_lists)




for item in final:
    name = "{0}_{1}_{2}_{3}.png".format(item[0], item[1], item[2], item[3])

    shutil.copyfile(os.path.join(PATH, 'test.png'), os.path.join(PATH, 'meow', name))