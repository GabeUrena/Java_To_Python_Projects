from atm2 import withdraw,deposit
import unittest

class test_atm2:
    
    
    def test_withdraw(self):
        self.assertEqual(withdraw(100,0),0,"Balance can't go below 0")
        self.assertEqual(withdraw(-1, 100),100,"Amount can't be negative")
        self.assertEqual(withdraw(100,1000),900, "Incorrect balance")
        self.assertEqual(withdraw(1000,1000),0, "Incorrect balance")
        self.assertEqual(withdraw(895,1000),105, "Incorrect balance")
        self.assertEqual(withdraw(500.41,1000),499.59, "Incorrect balance")
        
    def test_deposit(self):
        self.assertEqual(deposit(-1,100),100,"Amount can't be negative")
        self.assertEqual(deposit(100,0),100,"Incorrect balance")
        self.assertEqual(deposit(100.41,100),200.41,"Incorrect balance")
        self.assertEqual(deposit(1,51661),51662,"Incorrect balance")
        self.assertEqual(deposit(0.52,6162),6162.52,"Incorrect balance")
        
        
if __name__ == '__main__':
    unittest.main()