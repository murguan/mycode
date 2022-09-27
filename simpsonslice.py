#!/usr/bin/env python3
# Program to list 

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a = challenge[2][1]
b = challenge[2][0]
c = challenge[3] 

print(a)
print(b)
print(c)

print(f"My {a}! the {b} do {c}!")
