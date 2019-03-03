#!/usr/bin/env python3
import markovify
import sys

with open(sys.argv[1]) as f:
    text = f.read()

text_model = markovify.NewlineText(text)
print("Model Trained")

with open(sys.argv[2], "w") as o:
    o.write(text_model.to_json())
print("Model dumped to "+sys.argv[2])
