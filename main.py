import timeit
import mpmath

def M(a, b, zap):
    while abs(a - b) > mpmath.mpf(10) ** (-zap):
        a, b = (a + b) / 2, mpmath.sqrt(a * b)

    return (a + b) / 2

def N(a, b, zap):
    z = mpmath.mpf(0)
    while abs(a - b) > mpmath.mpf(10) ** (-zap):
        a, b, z = (a + b) / 2, z + mpmath.sqrt((a - z) * (b - z)), z - mpmath.sqrt((a - z) * (b - z))

    return (a + b) / 2

def alternative(t, a, b):
    return 2 * mpmath.pi * N(a ** 2, b ** 2, t) / M(a, b, t)

def toch(t,a,b):
    s = 1
    n = 0
    mpmath.mp.dps = t + 3
    mpmath.mp.pretty = True

    l = mpmath.pi * (a + b)
    sp = -1
    while True:
        n += 1
        s += (((mpmath.fac2(2 * n - 1)) / ((2 * n - 1) * (2 ** n) * mpmath.factorial(n))) * (
                ((a - b) / (a + b)) ** n)) ** 2
        if sp == s:
            return l * s
        sp = s

t = int(input("Введите точность: "))
a = mpmath.mpf(input("Введите а: "))
b = mpmath.mpf(input("Введите b: "))

print("Формула Айвори-Бесселя")
start = timeit.default_timer()
s1 = toch(t,a,b)
end = timeit.default_timer() - start
print("Периметр элипса =",s1,"м")
print("Время выполнения:", end, "с")

print("Альтернативная формула")
start = timeit.default_timer()
s2 = alternative(t,a,b)
end = timeit.default_timer() - start
print("Периметр элипса =",s2,"м")
print("Время выполнения:", end, "с")

print(s2-s1)
