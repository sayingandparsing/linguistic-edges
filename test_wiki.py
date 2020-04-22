import wiktextract
import json

path = '/home/reagan/Downloads/enwiktionary-latest-pages-articles.xml.bz2'

all_data = {}
count = {'c':0}

def cb(data):
    word = data['word']
    if word not in all_data:
        all_data[word] = data
    else:
        word += '_'
    if count['c'] == 0:
        with open('test.json', 'w') as f:
            f.write(json.dumps(all_data))
    count['c'] = count['c'] + 1
    if count['c'] % 100 == 0:
        print(count['c'])


ctx = wiktextract.parse_wiktionary(
    path, cb,
    capture_cb=None,
    languages=["German"],
    translations=True,
    linkages=True,
    pronunciations=False,
    redirects=False)

import json

out = 'alles.json'

with open(out, 'w') as f:
    f.write(json.dumps(all_data))
