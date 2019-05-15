vstup = open('mereni.txt', encoding='utf-8')
radky = [radek.split('\t') for radek in vstup]
vstup.close()
radky = [[radek[0], float(radek[1])] for radek in radky]
print(radky)
