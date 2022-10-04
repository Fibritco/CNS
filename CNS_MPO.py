class CNS_MPO:

    def __init__(self):
        print("Program oblicza CNS_MPO dla badanego związku.")
        print("Proszę o przygotowanie wartości:\npKa, clogP, clogD, MW, TPSA oraz HBD.")
        print()
        
    

    def pKa (self):
        a = float(input("Podaj wartość pKa dla badanego związku: "))
        if a < 8:
            b = 1
        elif a >= 8 and a < 10:
            b = - 0.5 * a + 5
        else:
            b = 0
        print("CNS_MPO pKa = %.2f" %b)    
        return  b
        

    def clogP (self):
        a = float(input("Podaj wartość clogP dla badanego związku: "))
        if a < 3:
            b = 1
        elif a >= 3 and a < 5:
            b = - 0.5 * a + 2.5
        else:
            b = 0
        print("CNS_MPO clogP = %.2f" %b) 
        return  b

    def clogD (self):
        a = float(input("Podaj wartość clogD dla badanego związku: "))
        if a < 2:
            b = 1
        elif a >= 2 and a < 4:
            b = - 0.5 * a + 2
        else:
            b = 0
        print("CNS_MPO clogP = %.2f" %b)
        return  b

    def MW (self):
        a = float(input("Podaj wartość MW (masy molowej) dla badanego związku: "))
        if a <= 360:
            b = 1
        elif a > 360 and a <= 500:
            b = - 0.00714286 * a + 3.57142857
        else:
            b = 0
        print("CNS_MPO clogP = %.2f" %b)    
        return  b

    def TPSA (self):
        a = float(input("Podaj wartość TPSA dla badanego związku: "))
        if a <= 20:
            b = 0
        elif a > 20 and a < 40:
            b = - 0.05 * a - 1
        elif a >= 40 and a <= 90:
            b = 1
        elif a > 90 and a < 120:
            b = -0.03333333 * a + 4
        else:
            b = 0
        print("CNS_MPO clogP = %.2f" %b)    
        return  b

    def HBD (self):
        a = float(input("Podaj wartość HBD dla badanego związku: "))
        if a == 0:
            b = 1
        elif a == 1:
            b = 0.75
        elif a == 2:
            b = 0.5
        elif a == 3:
            b = 0.25
        else:
            b = 0
        print("CNS_MPO clogP = %.2f" %b)
        return b


def main():
    CNS = CNS_MPO()

    d = CNS.pKa()
    e = CNS.clogP()
    f = CNS.clogD()
    g = CNS.MW()
    h = CNS.TPSA()
    i = CNS.HBD()
    
    lista = [d, e, f, g, h, i]
    w = float(sum(lista))
    print("CNS MPO dla badanego związku wyniósł: %.2f" %w)
    
main()