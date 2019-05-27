import re

fname='regex_sum_226103.txt'
fh = open(fname)
sumreg=0
for line in fh:
    x=re.findall('[0-9]+',line)
    if len(x)==0: continue
    for i in x:
        sumreg+=int(i)

print(sumreg)

