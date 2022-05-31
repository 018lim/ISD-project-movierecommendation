import json

data = {}
data['Book'] = []
data['Book'].append({
    'Title': 'Python',
    'Authors': ['John','Bob'],
    'Date':'2013',
    'Publisher': 'Springer'
})
data['Book'].append({
    'Title': 'Information System',
    'Authors': ['Andrew','Martin'],
    'Date':'2014',
    'Publisher': 'Elsevier'
})
data['Book'].append({
    'Title': 'Database',
    'Authors': ['Edward','David'],
    'Date':'2016',
    'Publisher': 'Wiley'
})

with open('BookData.json', 'w') as outfile:
    json.dump(data, outfile)
