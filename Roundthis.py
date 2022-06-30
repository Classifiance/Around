import numpy as np

print("Give me a float number")
a = input()
try:
    a = float(a)
except:
    print("Its not afloat number mate")
    quit()

print("Do you want to round up or down ?(u/d)")
b = input()

if b == "u":
    k = np.ceil(a)
elif b == "d":
    k = np.floor(a)
else:
    print("just choose between u and d")

print(k)
