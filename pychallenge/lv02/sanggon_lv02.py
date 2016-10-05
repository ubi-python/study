chr_dict = dict()

with open('mess.txt', 'r') as openfile:
    lines = openfile.readlines()

for line in lines:
    for chr in line:
        if chr not in chr_dict:
            chr_dict[chr] = 1
        else:
            chr_dict[chr] += 1

sorted(chr_dict.items(), key=lambda items: items[1][0])
print(chr_dict)
