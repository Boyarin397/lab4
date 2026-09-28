import math


p = 1 

for n in range(1, 21):
    p *= (n**2 + math.sin(n) + 1) / (n**2 + math.cos(n)**2)
print("Произведение =", p)
