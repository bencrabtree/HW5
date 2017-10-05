import re

filename = "regex_sum_38405.txt"
f = open(filename, 'r')
integers = []
for line in f.readlines():
    nums = re.findall('[0-9]+', line)
    for dude in nums:
        integers.append(int(dude))
        
print (sum(integers))
