#!/usr/bin/env python3
import markovify
import sys
import pickle

with open(sys.argv[1]) as f:
    text = f.read()

text_model = markovify.Text(text)
print("Model Trained")

with open(sys.argv[2], "wb") as o:
    pickle.dump(text_model, o)
print("Model dumped to "+sys.argv[2])
