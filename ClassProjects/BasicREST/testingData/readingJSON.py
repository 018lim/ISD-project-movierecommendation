import json

with open('BookData.json') as json_file:
    data = json.load(json_file)
    for p in data['Book']:
        print('Title: ' + p['Title'])
        for a in p['Authors']:
            print('Authors: ' + a)
        print('Date: ' + p['Date'])
        print('Publisher: ' + p['Publisher'])
        print('')
