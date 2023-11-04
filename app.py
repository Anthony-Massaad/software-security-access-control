from constants.permisions import user_permisions, read
from constants.roles import Roles

class App: 

    def __init__(self): 
        ...
    
    def run(self): 
        print("hit")
        print(user_permisions.get(Roles.REGULAR_CLIENT)[read])


if __name__ == "__main__":
    app = App()
    app.run()