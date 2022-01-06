import unittest
from unittest import result
from unittest.mock import MagicMock
from app.userRepository import UserRepository
from app.userService import UserService

class TestUser(unittest.TestCase):
    
    def testGetUser(self):
        # j'instancie le repo
        repo = UserRepository()
        
        # on modifie le retour du repo via magicMock
        repo.fetchAll = MagicMock(return_value=["jean", "marie"])
        
        # j'appelle le service
        service = UserService(repo)
        
        # on appelle le repo
        result = service.getUser()
        
        # on va tester unitairement
        self.assertEqual(result, ["jean", "marie"])
        
        
    def testSupprUser(self):
        # on peut tester qu'une méthode est appelée
        repo = UserRepository()
        repo.deleteUser = MagicMock()
        
        service = UserService(repo)
        service.delUser("paul")
        
        repo.deleteUser.assert_called_once_with("paul")
        
        
if __name__ == "__main__":
    unittest.main()