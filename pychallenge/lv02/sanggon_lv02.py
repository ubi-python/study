import collections

chr_dict = collections.OrderedDict()

with open('mess.txt', 'r') as openfile:
    lines = openfile.readlines()

for line in lines:
    for chr in line:
        if chr not in chr_dict:
            chr_dict[chr] = 1
        else:
            chr_dict[chr] += 1

# sorted(chr_dict)
rare_chr_dict = collections.OrderedDict((key, value) for key, value in chr_dict.items() if value < 100)
print(rare_chr_dict.keys())

print(len(rare_chr_dict.keys()))

# u i q t a e y l
