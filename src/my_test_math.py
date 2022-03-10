#!/usr/bin/env python3

"""TESTS
@author Marek Sechra
@date 10.3.2022

subject: IVS
project: projekt 2
"""

import unittest
from my_math import add
from my_math import substract
from my_math import multiply
from my_math import divide

from my_math import power
from my_math import root
from my_math import factorial
from my_math import modulo


class MathTest(unittest.TestCase):
    """ Class MathTest contains methods which are represent unittest cases

        Testing func:
            add()
            substract()
            multiply()
            divide()
            power()
            root()
            factorial()
            mudulo()
    """

    def test_add_int(self):
        a = 256
        b = 256
        self.assertEqual(add(a,b),512)
        
    def test_add_float(self):
        a = 5.055325
        b = 4.465113
        self.assertAlmostEqual(add(a,b),9.520437999999999)

    def test_add_int_float(self):
        a = 2
        b = 0.5
        self.assertEqual(add(a,b),2.5)

    def test_add_int_negative(self):
        a = -5
        b = -15
        c = 10
        self.assertEqual(add(a,b),-20)
        self.assertEqual(add(a,c),5)

    def test_add_float_negative(self):
        a = -0.125
        b = -1.125
        c =  1.125
        self.assertEqual(add(a,b),-1.25)
        self.assertEqual(add(a,c),1.0)
    
    def test_add_string(self):
        a = 5
        b = "nonnumber"
        
        with self.assertRaises(ValueError):
            add(a,b)

        with self.assertRaises(ValueError):
            add(b,a)


    #---------------------------------------------

    def test_substr_int(self):
        a = 5
        b = 4
        self.assertEqual(substract(a,b),1)

    def test_substr_float(self):
        a = 1.075
        b = 0.075
        self.assertEqual(substract(a,b),1.0)

    def test_substr_int_float(self):
        a = 2.5
        b = 5
        self.assertEqual(substract(a,b),-2.5)

    def test_substr_int_negative(self):
        a = -5
        b = -3
        c = 2.0
        self.assertEqual(substract(a,b)-2)
        self.assertEqual(substract(a,c),-7)
        self.assertEqual(substract(c,a),7)

    def test_substr_float_negative(self):
        a = -0.5
        b = -0.6
        c = 1.0
        self.assertAlmostEqual(substract(a,b),0.1)
        self.assertAlmostEqual(substract(a,c),-1.5)
        self.assertAlmostEqual(substract(c,a),1.5)

    def test_substr_string(self):
        a = 5
        b = "nonnumber"
        
        with self.assertRaises(ValueError):
            substract(a,b)

        with self.assertRaises(ValueError):
            substract(b,a)
     
     #---------------------------------------------
    
    def test_multiply_int(self):
        a = 5
        b = 3
        self.assertEqual(multiply(a,b),15)

    def test_multiply_float(self):
        a = 15.52
        b = 1.01
        self.assertEqual(multiply(a,b),15.6752)

    def test_multiply_int_float(self):
        a = 2
        b = 2.23
        self.assertEqual(multiply(a,b),4.46)

    def test_multiply_int_negative(self):
        a = -3
        b = -5
        c = 7
        self.assertEqual(multiply(a,b),15)
        self.assertEqual(multiply(a,c),-27)

    def test_multiply_float_negative(self):
        a = -3.25
        b = -5.0125
        c = 2.1
        self.assertAlmostEqual(multiply(a,b),16.290625000000002)
        self.assertEqual(multiply(a,c),-6.825) 
        
    def test_multiply_string(self):
        a = 5
        b = "nonnumber"
        
        with self.assertRaises(ValueError):
            multiply(a,b)

        with self.assertRaises(ValueError):
            multiply(b,a)
     #---------------------------------------------

    def test_divide_int(self):
        a = 3
        b = 5
        self.assertEqual(divide(a,b),0.6)

    def test_divide_float(self):
        a = 0.5
        b = 0.125
        self.assertEqual(divide(a,b),4.0)

    def test_divide_zero(self):
        a = 2
        b = 0
        with self.assertRaises(ValueError):
            divide(a,b)

    def test_divide_int_float(self):
        a = 5
        b = 2.5
        self.assertEqual(divide(a,b),2.0)


    def test_divide_int_negative(self):
        a = -3
        b = -2
        c = 2
        self.assertEqual(divide(a,b),1.5)
        self.assertEqual(divide(a,c),-1.5)

    def test_divide_float_negative(self):
        a = -1.25
        b = -0.5
        c = 0.5
        self.assertEqual(divide(a,b),2.5)
        self.assertEqual(divide(a,c),-2.5)
     
    def test_divide_string(self):
        a = 5
        b = "nonnumber"
        
        with self.assertRaises(ValueError):
            divide(a,b)

        with self.assertRaises(ValueError):
            divide(b,a)
    
     #---------------------------------------------

    def test_power_int(self):
        x = 2
        n = 3
        self.assertEqual(power(x,n),8)

    def test_power_float(self):
        x = 2.1
        n = 3
        self.assertAlmostEqual(power(x,n),9.261)
        with self.assertRaises(ValueError):
            power(n,x)

    def test_power_zero(self):
        x = -5
        n = 0
        self.assertEqual(power(abs(x),n),1)
        self.assertEqual(power(x,n),1)

    def test_power_int_negative(self):
        x = -2
        n = -3
        self.assertEqual(power(abs(x),n),0.125)
        self.assertEqual(power(x,n),-0.125)
        self.assertEqual(power(x,abs(n)),-8)

    def test_power_float_negative(self):
        x = -2.5
        n = -2.1
        n2 = -2

        self.assertAlmostEqual(power(x,n),-0.1459909658488769)
        #power(x,n)

        self.assertEqual(power(x,n2),-0.16)
        
    def test_power_string(self):
        a = 5
        b = "nonnumber"
        
        with self.assertRaises(ValueError):
            power(a,b)

        with self.assertRaises(ValueError):
            power(b,a)

     #---------------------------------------------
    
    
    def test_root_int(self):
        x = 8
        n = 3
        self.assertEqual(root(x,n),2)

    def test_root_int_float(self):
        x = 98.01
        n = 2
        n2 = 2.5

        self.assertEqual(root(x,n),9.9)
        with self.assertRaises(ValueError):
            root(x,n2)

    def test_root_zero(self):
        x = 9
        n = 0
        n2 = 2

        self.assertEqual(root(n,n2),0.0)
        with self.assertRaises(ValueError):
            root(x,n)

        
    def test_root_int_negative(self):
        x = -8
        n = -3
        with self.assertRaises(ValueError):
            root(x,n)

        self.assertEqual(root(abs(x),n),0.5)

    def test_root_float_negative(self):
        x = -98.01
        n = -2.1

        with self.assertRaises(ValueError):
            root(x,n)

        self.assertAlmostEqual(root(abs(x),n),0.1126616234584776)

    def test_root_string(self):
        a = 5
        b = "nonnumber"
        
        with self.assertRaises(ValueError):
            root(a,b)

        with self.assertRaises(ValueError):
            root(b,a)

     #---------------------------------------------

    def test_factorial_int(self):
        n = 3
        self.assertEqual(factorial(n),6)
        
    def test_factorial_float(self):
        n = 3.5
        with self.assertRaises(ValueError):
            factorial(n)

    def test_factorial_zero(self):
        n = 0
        self.assertEqual(factorial(0),1)

    def test_factorial_negative(self):
        n = -5
        with self.assertRaises(ValueError):
            factorial(n)

#---------------------------------------------

    def test_modulo_int(self):
        x = 5
        n = 4
        self.assertEqual(modulo(x,n),1)

    def test_modulo_float(self):
        x = 5.2
        n = 2.2
        with self.assertRaises(ValueError):
            modulo(x,n)

    def test_modulo_int_float(self):
        x = 2
        n = 2.5
        with self.assertRaises(ValueError):
            modulo(x,n)

        with self.assertRaises(ValueError):
            modulo(n,x)

    def test_modulo_negative_int(self):
        x = -2
        n = 2
        self.assertEqual(modulo(x,n),0)

    def test_modulo_negative_float(self):
        x = -5.2
        n = -1.2
        with self.assertRaises(ValueError):
            modulo(x,n)

    def test_modulo_string(self):
        a = 5
        b = "nonnumber"
        
        with self.assertRaises(ValueError):
            root(a,b)

        with self.assertRaises(ValueError):
            root(b,a)

if __name__ == '__main__':
    unittest.main()
