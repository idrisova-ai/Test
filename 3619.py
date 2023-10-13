def function(a, b, c):
    if a == 0:
        if b != 0:
            x1 = -(c / b)
            print(1, x1)
            return
        if b == 0 and c != 0:
            print(0)
            return
        if b == 0 and c == 0:
            print(3)
            return
    else:
        D = (b ** 2) - (4 * a * c)
        if D > 0:
            x1 = ((-b) - (D ** 0.5)) / (2 * a)
            x2 = ((-b) + (D ** 0.5)) / (2 * a)
            if x1 < x2:
                print(2, x1, x2)
            else:
                print(2, x2, x1)
            return
        elif D == 0:
            x1 = (-b) / (2 * a)
            print(1, x1)
            return
        elif D < 0:
            print(0)
            return


a = float(input())
b = float(input())
c = float(input())
(function(a, b, c))
