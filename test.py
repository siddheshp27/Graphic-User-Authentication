priordict = {1: 'sfruitPass', 2: 'schocoPass', 3: 'salfaPass'}
cpriordict = priordict.copy()
fPass = ''
for i in priordict:
    pmax = max(cpriordict)
    fPass += priordict[pmax]
    cpriordict.pop(pmax)
print(fPass)
