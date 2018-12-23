#!/usr/bin/env python3
import sys
import markovify
import pickle


with open(sys.argv[1], 'rb') as input:
    model = pickle.load(input)

print("Model Loaded\n")
for i in range(int(sys.argv[2])):
    print(str(model.make_sentence())+"\n")
