import unittest

from classe.demo import Demo
from classe.demo2 import Demo2

class TestAssert(unittest.TestCase):
    
    def setUp(self):
        self.nbr1 = 5
        self.nbr2 = 3
        self.nom = "MARIE"
        self.demo = Demo()
        self.demo2 = Demo()
        self.listNom = ["Pierre", "Anne", "Jeanne"]
    
    def tearDown(self) -> None:
        pass
    
    def test_equal(self):
        # tester l'egalité
        self.assertEqual(self.nbr1 + self.nbr2, 8)
        
    def test_notEqual(self):
        # tester l'inegalité
        self.assertNotEqual(self.nbr1 + self.nbr2, 10)
        
    def test_gt(self):
        # tester le > que
        self.assertGreater(self.nbr1, self.nbr2)
        
    def test_lt(self):
        # tester le < que
        self.assertLess(self.nbr2, self.nbr1)
        
    def test_true(self):
        # tester que le retour est vrai
        self.assertTrue(self.nom.isupper())
        
    def test_false(self):
        # tester que le retour est faux
        self.assertFalse(self.nom.islower())
        
    def test_is(self):
      # tester que deux objets sont inegaux
      self.assertIsNot(self.demo, self.demo2)  
          
    def test_in(self):
        # tester si un conteneur contient ma valeur
        self.assertIn("Jeanne",self.listNom)
        
    def test_isInstance(self):
        # tester qu'un objet est bien une instance de classe
        self.assertIsInstance(self.demo2, Demo)
        
    def test_raise(self):
        # tester raise sur une exception
        with self.assertRaises(Exception) as context:
            self.demo.add("azer",45)
            
        self.assertTrue("err" in str(context.exception))