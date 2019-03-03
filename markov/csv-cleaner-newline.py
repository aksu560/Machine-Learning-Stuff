#!/usr/bin/env python3
import sys
import csv

output = []
with open(sys.argv[1], 'r', errors='ignore') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        output.append(row[int(sys.argv[3])]+'\n')

output = ''.join(output)

print(output)

with open(sys.argv[2], 'w') as o:
    o.write(output)
