file_path = "/Users/frestivo/Documents/Genealogia/Francisco Restivo full family 20231129.ged"

with open(file_path, "r") as f:
    lines = f.readlines()

indi = ['Source,Target,Label,Kind']

n = 0

for l in lines:
    if 'INDI' in l:
        i = l[2:16]
    if 'SURN' in l:
        s = l[7:-1]
    if 'FAMS' in l:
        indi.append('\n'+i+','+l[7:-1]+','+s+',FAMS')
    if 'FAMC' in l:
        indi.append('\n'+i+','+l[7:-1]+','+s+',FAMC')
    n = n+1

print(n, 'lines read')

with open('redegenealogica2.csv', 'w') as f:
    for i in indi:
        f.write(i)
