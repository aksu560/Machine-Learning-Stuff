#!/usr/bin/env python3

import markovify
import sys



with open(sys.argv[1], 'r') as input:
    model1 = markovify.Text.from_json(input.read())

print('Model 1 at {} read'.format(sys.argv[1]))

with open(sys.argv[2], 'r') as input:
    model2 = markovify.Text.from_json(input.read())

print('Model 2 at {} read'.format(sys.argv[2]))


if len(sys.argv) >= 5:
    weights = tuple(map(int, sys.argv[4].split('/')))
    combined_model = markovify.combine([model1, model2], weights)

else:
    combined_model = markovify.combine([model1, model2])

print("Models combined")

del model1
del model2

with open(sys.argv[3], "w") as o:
    o.write(combined_model.to_json())
print("Combined model dumped to {}".format(sys.argv[3]))
