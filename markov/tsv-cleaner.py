#!/usr/bin/env python3
import sys
import csv

output = []
with open(sys.argv[1], 'r', errors='ignore') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader) # Ignore first row

    for row in reader:
        output.append(row[int(sys.argv[3])])

output = ' '.join(output).rstrip('\n')

print(output)

with open(sys.argv[2], 'w') as o:
    o.write(output)
