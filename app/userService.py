from app.userRepository import UserRepository

class UserService():
    
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo
    
    def getUser(self):
        return self.repo.fetchAll()
    
    def delUser(self, user):
        return self.repo.deleteUser(user)