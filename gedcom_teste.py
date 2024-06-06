file_path = "Francisco Restivo full family_20240604.ged"
output_file = "redegenealogica20240604.csv"

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

with open(output_file, 'w') as f:
    for i in indi:
        f.write(i)
