import random

mine = input("홀/짝을 선택하세요")
com = ""
result = ""

rand = random.random()

if rand < 0.5:
    com = "홀"
else:
    com = "짝"
    
if mine == com:
    result = "WIN"
else:
    result = "LOSE"

print("com:",com)
print("mine:",mine)
print("result:",result)