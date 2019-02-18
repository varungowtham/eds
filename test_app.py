import requests
import time
import sys
import os

ems = os.environ["ET_EMS_LSBEATS_HOST"]
headers = {'content-type': 'application/json'}

stampers = '''
when e.strcmp(type,"net") do #NetData
when e.path(message) do #TJobMsg

when e.tag(#testresulted) do #websocket
'''

moms = '''
stream bool testcorrect = e.strmatch(message, "Hello Varun")

trigger tjobfinished do emit testcorrect on #testresulted
trigger tjobfinished do emit testcorrect on #websocket
'''

url = "http://" + ems + ":8888/stamper/tag0.1"
response = requests.post(url, headers=headers, data=stampers)
print(response.content)

url = "http://" + ems + ":8888/MonitoringMachine/signals0.1"
response = requests.post(url, headers=headers, data=moms)
print(response.content)

from websocket import create_connection
url = "ws://" + ems + ":3232"
ws = create_connection(url)
i = 0
while True:
  result = ws.recv()
  print result
  i+=1
  if i == 5:
    print "Hello Varun"
    break

print "Hello Varun"
