import unittest
from rational import Rational, fac, gcd, getDigits, getLength,denom, checkForValidity



class TestEq(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Rational(1,3), Rational(2,6), "Should be equal")

    def test_equality(self):
        self.assertEqual(int(Rational(1,2).reciprocal()), 2,"Should be 2")
        
        

class TestOp(unittest.TestCase):
    def test_sum(self):
        self.assertTrue(Rational(1,2) + Rational(1,3) == Rational(5,6))
    
    def test_mult(self):
        self.assertTrue((Rational(3,6) * Rational(2,1)) == Rational.one())

    def test_float(self):
        self.assertTrue(float(Rational.onehalf()) == 0.5)
        
    def test_gt(self):
        self.assertTrue(Rational.onehalf() > Rational.onethird())
        
    def test_ge(self):
        self.assertTrue(Rational(4,9) >= Rational(3,9))
        
    def test_ne(self):
        self.assertTrue(Rational(3,7) != Rational (2,9))
        
    def test_add(self):
        self.assertEqual(Rational(2,3) + Rational(1,9), Rational(7,9), Rational.zero())
        
    def test_sub(self):
        self.assertTrue(Rational.onehalf() - Rational.onehalf())
        
    def test_mul(self):
        self.assertEqual(Rational(1,3)*Rational(3,1), Rational.one())
        
    def test_div(self):
        self.assertEqual(Rational(2,3) / Rational(2,3), Rational.one())
        
    def test_neg(self):
        self.assertEqual(-Rational(1,4), Rational(-1,4))
        
    def test_neg2(self):
        self.assertEqual(--Rational(1,4), Rational(1,4))
        
    def test_pos(self):
        self.assertEqual(+Rational(1,4), Rational(1,4))
        
    def test_pow(self):
        self.assertTrue(pow(Rational.onehalf(), 3) == Rational(1,8))
        
    def test_pow2(self):
        self.assertTrue(pow(Rational(2,3), 3) == Rational(8,27))
        
    def test_nom_denom(self):
        r = Rational(7,8)
        self.assertTrue(r.nom == 7 and r.denom == 8)
        
        
        
class TestConversion(unittest.TestCase):
    def test_int_to_rational(self):
        self.assertEqual(Rational.intToRational(5), Rational(5,1))
        
    def test_period_to_rational(self):
        self.assertEqual(Rational.periodToRational(3), Rational(1,3))
        
    def test_fraction_to_rational(self):
        self.assertEqual(Rational.fractionToRational(123,2), Rational(123, 100000))
    def test_periodic_float_to_rational(self):
        self.assertEqual(Rational.periodicFloatToRational(2, 125, 2, 879), Rational(33320959, 16650000))

    def test_periodic_float_o_rational2(self):
        self.assertEqual(float(Rational.periodicFloatToRational(2,125,2,879)), 2.0012587987987986)
    
    def test_exception(self):
        with self.assertRaises(Exception) as context:
            f = float(Rational.one()/Rational.zero())
            self.assertTrue('exception' in str(context.exception))
            
            
            
class TestFunctions(unittest.TestCase):
    def test_fac(self):
        self.assertEqual(fac(5), 120)
        
    def test_gcd(self):
        self.assertTrue(gcd(4,6) == 2)
        
    def test_getdigits(self):
        self.assertEqual(getDigits(31415927), [3,1,4,1,5,9,2,7])
        
    def test_getlength(self):
        self.assertEqual(getLength(31415927), 8)
        
    def test_denom(self):
        self.assertEqual(denom(1234), 9999)
        
    def test_checkforvalidity(self):
        self.assertTrue(checkForValidity(1234))
        
    def test_checkforvalidity2(self):
        self.assertFalse(checkForValidity(12034))
        

    
    
if __name__ == '__main__':
    unittest.main()