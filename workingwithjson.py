import json

with open('aws.json') as rd:
  jsonData = json.load(rd)

for data in jsonData['Users']:
  del data['CreateDate']

with open('awsModified.json', 'w') as wd:
  json.dump(jsonData, wd, indent = 2)
