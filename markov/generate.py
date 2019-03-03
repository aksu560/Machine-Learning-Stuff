#!/usr/bin/env python3
import sys
import markovify


with open(sys.argv[1], 'r') as input:
    model = markovify.Text.from_json(input.read())

print("Model Loaded\n")
x = int(sys.argv[2])
i = 0
failed = 0
while i < x:
    sentence = str(model.make_sentence())+"\n"
    if sentence != "None\n":
        print(sentence)
    else:
        failed = failed + 1
        x = x + 1
    i = i + 1


if failed > 0:
    print("{} out of {} ({}%) generation attempts failed".format(failed, x, failed/x*100))
