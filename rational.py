

"""
class Rational implements rational numbers
for Python. It provides many useful operators,
methods to convert floats or ints to rational
numbers, and vice versa. It includes a 
method to obtain a rational representation
of e (Euler number). 

"""

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
    
# convert number into a list of digits, for example 123 in [1,2,3]
def getDigits(n):
    list = []
    s = str(n)
    for i in range(0, len(s)):     
        list.append(int(s[i]))
    return list
    
# calc number of digits of number, for example, 4355 has 4 digits
def getLength(n):
    return len(getDigits(n))

#check if a number does not contain the digit 0
def checkForValidity(n):
    return not 0 in getDigits(n)
    
# helper function for convertig floats, periods, fractions 
# to rational numbers.
# for example denom(12345) == 99999, denom(2) == 9
def denom(period):
    sum = 0
    for i in range(0, getLength(period)): sum = sum * 10 + 9
    return sum

def fac(n):
    res = 1
    for i in range(2, n+1): res *= i
    return res

class Rational:
    def __init__(self, nom, denom):
        assert denom != 0, "denominator must be <> 0"
        gcd_nd = gcd(nom,denom)
        self.nom = int(nom / gcd_nd)
        self.denom = int(denom / gcd_nd)
        
    def nominator(self):
        return self.nom
        
    def denominator(self):
        return self.denom
        
    def __add__(self, r):
        x = self.nom * r.denom
        y = r.nom * self.denom
        n = x + y
        d = self.denom * r.denom
        return Rational(n, d)
        
    def __mul__(self, r):
        n = self.nom * r.nom
        d = self.denom * r.denom
        return Rational(n, d)
        
    def __truediv__(self, r):
        return self * r.reciprocal()
        
    def reciprocal(self):
        assert self.nom != 0; "Invertion with 0 nominator is not allowed"
        return Rational(self.denom, self.nom)
        
    def __neg__(self):
        return Rational(-self.nom, self.denom)
        
    def __pos__(self):
        return self 
        
    def __sub__(self,r):
        return self + -r
        
    def __eq__(self, r):
        return self.nom == r.nom and self.denom == r.denom
        
    def __ne__(self, r):
        return not self == r
        
    def __gt__(self, r):
        tmp = self - r 
        return tmp.nom > 0 and tmp.denom  > 0 
        
    def __ge__(self, r):
        return self > r or self == r
        
    def __lt__(self, r):
        return r > self
        
    def __le__(self, r):
        return self < r or self == r
        
    def __str__(self):
        if self.denom == 1:
            return str(int(self.nom))
        else:
            return str(int(self.nom)) + " / " + str(int(self.denom))
            
    def __repr__(self):
        return str(self.nom) + " / " + str(self.denom)
        
    def __pow__(self, exp):
        e = int(exp)
        return Rational(pow(self.nom, e), pow(self.denom, e))
        
    def __invert__(self):
        return self.reciprocal()
        
    # converts a rational number to an integer (heavy loss of precision)
    def __int__(self):
        return int(self.nom // self.denom)
        
    # converts a rational to float (mostly harmless, medium loss of precision)    
    def __float__(self):
        return 1.0 * self.nom / self.denom
        
    ################## class functions ##################
        
    def zero():
        return Rational(0, 1)
        
    def one():
        return Rational(1,1)
        
    def onehalf():
        return Rational(1,2)
        
    def onethird():
        return Rational(1,3)
        
        
    # calculates an approximation of Eulers number as rational
    # number. digits: number of Taylor nodes to be calculated
    def e(digits):
        assert digits > 0, "zero digits is not allowed"
        sum = Rational.one()
        for i in range(1,digits + 1): 
            sum += Rational(1,fac(i))
        return(sum)

    
    # convert a period like 3 (equivalent to 0.33333333) to a 
    # rational number. The argument leadingzeroes specifies
    # how many zeros there are between the decimal point and
    # the start of the period. for example, 0.0333333 has a 
    # period of 3 and a leadingzeros of 1
    def periodToRational(period, leadingzeros = 0):
        assert leadingzeros >= 0, "leadingzeros must be >= 0"
        assert checkForValidity(period), "period is not allowed to contain 0"
        return Rational(period, pow(10, leadingzeros)*denom(period))
        
    def intToRational(n):
        return Rational(n, 1)
        
    
    # creates an rational number that has the value 0.fraction
    # Number of leading zeros in leadingzeros: if for example, 
    # the number is 0.000fraction leadingzeros is 3
    def fractionToRational(n, leadingzeros = 0):
        if n == 0: 
            return Rational.zero()
        else:
            list = []
            s = str(n)
            for i in range(0, len(s)): list.append(int(s[i]))
            return Rational(n, pow(10, leadingzeros + len(list)))
        
    def floatToRational(x, digits=0):
        left = abs(int(f))
        right = abs(f - int(f))
        r_left = Rational.intToRational(left)
        zeros = 0
        tmp = right
        while (int(tmp) == 0):
            zeros += 1
            tmp = 10 * tmp
        zeros -= 1
        tmp = tmp / 10 * pow(10, digits)
        r_right = Rational.fractionToRational(int(tmp), leadingzeros = zeros)
        if x >= 0:
            return r_left + r_right
        else:
            return -r_left + r_right
            
            
    # for example, in the float 2.00125879879879 we would use 
    # number = 2, leadingzeros = 2, fraction = 125, period = 879
    def periodicFloatToRational(number, fraction, leadingzeros, period):
        r1 = Rational.intToRational(number)
        if fraction == 0:
            r2 = Rational.periodToRational(period,leadingzeros)
        else:
            r2 = Rational.periodToRational(period, leadingzeros+getLength(fraction))
        r3 = Rational.fractionToRational(fraction, leadingzeros)
        return r1+r2+r3
        
        



