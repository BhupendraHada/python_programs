mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key in sorted(mydict.iterkeys()):
    print "%s: %s" % (key, mydict[key])

sort_dict = dict(sorted(mydict.items(), key=lambda x: x[1]))
print  sort_dict

#How to sort a dict by keys (Python older than 2.4):
keylist = mydict.keys()
keylist.sort()
for key in keylist:
    print "%s: %s" % (key, mydict[key])

#How to sort a list of dicts in Python
DATA = [{'avg': 2.9165000000000001, 'count': 10.0, 'total': 29.165000000000003, 'ups_ad': u'10.194.154.49:80'},
    {'avg': 2.6931000000000003, 'count': 10.0, 'total': 26.931000000000001, 'ups_ad': u'10.194.155.176:80'}]

data_sorted = sorted(DATA, key=lambda item: item['ups_ad'])
