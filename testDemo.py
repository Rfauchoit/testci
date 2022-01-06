import unittest
from classe.demo import Demo

class TestDemo(unittest.TestCase):
    
    def setUp(self) -> None:
        # se lance à chaque test
        self.demo = Demo()
        
    def tearDown(self) -> None:
        # se lance à chaque test
        del self.demo
    
    def test_add(self):        
        self.assertEqual(self.demo.add(1,3), 4, "le résultat n'égal pas 4")        
        self.assertEqual(self.demo.add(5,5), 10, "le résultat n'égal pas 10")
        
        with self.assertRaises(Exception) as context : 
            self.demo.add("m", 45)
        self.assertTrue("error" in str(context.exception))