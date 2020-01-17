#!/usr/bin/python

import datetime
import json

date = str(datetime.datetime.now())
print json.dumps({
    "time" : date
})

#run
#ansible -m timetest.py  localhost --module-path=.
