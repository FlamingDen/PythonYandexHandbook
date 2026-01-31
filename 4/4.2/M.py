lm = lambda x: (len(x), x.lower())
string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=lm))