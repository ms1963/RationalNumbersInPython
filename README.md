# Rational Numbers in Python
This class implements rational numbers in Python.

It provides the most important operators and functions.
It allows to convert periodic decimal numbers into rational numbers as well as other conversions to and from int and float.
The method e(digits) calculates the Taylor series of exp(x) at x = 1 with digits specifying the number of Taylor iterations. It returns a rational number that approximates the Euler number e.

A unit test file is available as well.

```
r = Rational.one()
for i in range(1,6):
    r *= Rational(1,i)
print(r)
print(r.reciprocal())
  => 1 / 120
     120
  
print((-Rational(1,2)+Rational(1,3)).reciprocal() * Rational(1,6)+Rational(3,2))
  => 1 / 2


  
print(Rational.periodToRational(6)) # 0.6666666....
  => 2 / 3
  
print(Rational.periodToRational(9)) # 0.9999999....
  => 1
  
print(float(Rational.periodicFloatToRational(123, 456, 0, 789))) # 123.456789789789...., r = 41111111 / 333000
  => 123.4567897897898
  
print(float(Rational.periodicFloatToRational(123, 456, 1, 789))) # 123.045678978978...., r = 409742111 / 3330000
  => 123.04567897897898
  
print(Rational.e(20))
  => 6613313319248079872 / 2432902008176640000 # e in float: 2.718281828459045
 
 
 
```
