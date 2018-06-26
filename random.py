import random

names = ["fred","mary","thomas","kevin","mike","june"]

print(random.choice(names)) #picks out names randomly

random.shuffle(names)#randomly shuffles in it.
print(names)

print(random.randrange(1,1000,10))#last value is step that a random should run for 10 steps to find a random number



