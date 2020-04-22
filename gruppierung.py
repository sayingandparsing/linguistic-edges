text = ''
with open('/home/reagan/code/proj/familienanlichkeiten/data/DeReKo-2014-II-MainArchive-STT.100000.freq', 'r+') as f:
    text = f.read()

def process_line(line: str):
    parts = line.split('\t')
    return (parts[1], parts[2])

known = set()
lemmas = []

for line in text.splitlines():
    lemma = process_line(line)
    if lemma[0]+lemma[1] not in known:
        lemmas.append(lemma)
        known.add(lemma[0]+lemma[1])

print(known)
