tupla=("a","b","c")
tupla


L=[2,9,13,4,7,5,15,35,25,11]

for x,e in enumerate(L):
    print("%d / %d = %f" % (x, e, x/e))

for x,e in enumerate(L):
    print("%d X %d = %d" % (x, e, x*e))

for x,e in enumerate(L):
    print("%d - %d = %d" % (x, e, x-e))

for x,e in enumerate(L):
    print("%d + %d = %d" % (x, e, x+e))
