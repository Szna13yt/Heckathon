with open('./input.txt', 'r') as f:
  input = [[int(i) for i in _.strip().split()] for _ in f.readlines()]
dices = {"d20": 20, "d10": 10, "d8": 8, "d6": 6, "d4": 4, "d3": 3, "d2": 2}
for i in input:
  for j in i:

