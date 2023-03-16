state = 0
try:
    ocjena = 0
    while True:
        ocjena = float(input())
        if ocjena > 0 and ocjena < 1:
            break
        print("Broj je izvan intervala")
    print("Ocjena: ", ocjena)
except:
    print("Something went wrong")
if not type(ocjena) is float:
    state = 1
    raise TypeError("Not an integer")

if state == 0:

    if ocjena >= 0.9:
        print("Ocjena je A")
    elif ocjena >= 0.8:
        print("Ocjena je B")
    elif ocjena >= 0.7:
        print("Ocjena je C")
    elif ocjena >= 0.6:
        print("Ocjena je D")
    else:
        print("Ocjena je F")
