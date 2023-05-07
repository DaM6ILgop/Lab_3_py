class Fraction(object):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num //= g  # Используем оператор целочисленного деления для получения целого числа
        self.__den //= g  # Используем оператор целочисленного деления для получения целого числа

    def __neg__(self):
        return Fraction(-self.__num, self.__den)

    def __invert__(self):
        return Fraction(self.__den, self.__num)

    def __pow__(self, power):
        if power >= 0:
            return Fraction(self.__num ** power, self.__den ** power)
        else:
            return Fraction(self.__den ** abs(power), self.__num ** abs(power))

    def __float__(self):
        return float(self.__num) / self.__den

    def __int__(self):
        return self.__num // self.__den

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)


frac = Fraction(7, 2)
print(-frac)
print(~frac)
print(frac ** 2)
print(float(frac))
print(int(frac))