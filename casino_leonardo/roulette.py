import random
mise=50
nombre_mise=1
rouge = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
noir = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
x=random.randint(0,36)
print(x)
print(nombre_mise)

if nombre_mise > 0 and nombre_mise <=18:
    if nombre_mise < 0:
        print("Ce nombre est négatif")
    if nombre_mise > 36:
        print("Ce nombre est supérieur à 36")
    if x>0 and x<=18:
        mise=mise*2
        print(mise)

if nombre_mise > 18 and nombre_mise <=36:
    if nombre_mise < 0:
        print("Ce nombre est négatif")
    if nombre_mise > 36:
        print("Ce nombre est supérieur à 36")
    if x>18 and x<=36:
        mise=mise*2
        print(mise)
