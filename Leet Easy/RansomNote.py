

ransomNote = 'aa'
magazine = 'ababbababbaa'

dicts = {}

for ch in magazine:
    if ch in dicts:
        dicts[ch] += 1
    else:
        dicts.setdefault(ch, 1)
print(dicts)