#!/usr/bin/python3
'''
data = 'changed text'

file = open('output.txt', 'w')
file.write(data)
file.close()
'''

dataset = [1,4,5,88,44,'ololo','ololox2',3940]
#file = open('output.txt', 'a')
'''
with open('output.txt', 'a') as file:
    for i in dataset:
        file.write(str(i))
        file.write('\n')

print(file.closed)
'''

with open('output.txt', 'r') as file:
    text_data = file.readlines()

for s in text_data:
    text_data[text_data.index(s)] = s.replace('\n', '')

print(text_data)
