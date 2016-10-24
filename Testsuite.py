#!/usr/bin/python3
import unittest
from   Reaction import Reaction

class TestObject:
    def __init__(self, a):
        self.a = a

    def getA(self):
        return self.a
   
    def setA(self, a):
        self.a = a
        
    def setDivers(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

def fkt_1(a="A", b="B"):
    return "a: %s, b: %s" % (a,b)

def fkt_2(a="A", b="B",c="C"):
    return "a: %s, b: %s, c: %s" % (a,b,c)


class ReactionModuleTestCase(unittest.TestCase):    
    def setUp(self):
        self.R = Reaction()
    
    def test_f1(self):
        self.R.add_action('f1',fkt_1)
        assert self.R.react('f1',1,2,3,4,5,6) == "a: 1, b: 2"

    def test_f2(self):
        self.R.add_action('f2',fkt_2)
        assert self.R.react('f2',1,2,3,4,5,6) == "a: 1, b: 2, c: 3"

    def test_Exception(self):
        assert self.R.react('Ex',1,2,3,4,5,6) == "EXCEPTION: Ex handler not found!"

    def test_method(self):
        self.A = TestObject('AAA')
        self.R.add_action('gA',self.A.getA)
        self.R.add_action('sA',self.A.setA)
        self.R.add_action('d', self.A.setDivers) 
        assert self.A.getA() == 'AAA'
        assert self.R.react('gA') == 'AAA'        
        
        self.R.react('sA','BBB')
        assert self.R.react('gA') == 'BBB'
        
        self.R.react('d', 1,2,3,4,5)
        assert self.A.e == 5

if __name__ == "__main__":
    unittest.main() # run all tests

