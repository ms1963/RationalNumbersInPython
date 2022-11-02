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
  => 1 / 120

print(r.reciprocal())
  => 120
```
