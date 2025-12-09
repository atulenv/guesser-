import random


target = list("ashwin sir")
current = list("0000000000") 
alphabet = " abcdefghijklmnopqrstuvwxyz"
attempts = 0


def get_random_char():
    return random.choice(alphabet)
while current != target:
    attempts += 1 
    for i in range(len(target)):
        if current[i] != target[i]:
 	        current[i] = get_random_char()
    
print(*current,sep='')
print(attempts)    
