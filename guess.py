import random


target = list(input("Target:"))
current = list(input("Start From :"))
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
