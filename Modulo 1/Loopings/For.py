'''
L=[8,9,15]
for sarah in L:
    print(sarah)


L=["comida","compras","roupas novas"]
for s in L:
    for letra in s:
        print(letra)
'''
def exibe_maximo():
    L=[1,7,2,4]
    maximo=L[0]
    for e in L:
        if e > maximo:
            maximo = e
    print(maximo)
exibe_maximo()

for v in range (5,8):
    print(v)

    for t in range (3,33,3):
        print(t, end="")
print("")
nome="sarah"
idade=15
grana=51.34
print("%50s tem %010d anos e %5.2f no bolso."%(nome, idade, grana))
print("")

def divide(x,y):
    try:
        result= x/y
    except ZeroDivisionError:
        print("por favor,nao ultilize zeros")
    except:
        print("\033[91m algo deu erraado...]")
    else:
        print(f"seu resultado e: {result}")
    finally:
        print("\033[92m vamos de novo?]")
divide(13,0)
divide("a","q")

value=2

match value:
    case 0:
        print("zero")
    case 1:
        print("um")
    case 2:
        print("dois")