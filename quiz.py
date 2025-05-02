import random

with open('quiz.txt', 'r') as file:
    lines = file.readlines()

questions = []
i = 0
while i < len(lines):
    