

def func():
    for a in range(1, 1000):
        for b in range(a+1, 1001):
            c = 1000 - a - b
            if ( a*a + b*b == c*c ):
                print("a: " + str(a))
                print("b: " + str(b))
                print("c: " + str(c))
                print("abc : " + str(a*b*c))
                return
    return


func()
