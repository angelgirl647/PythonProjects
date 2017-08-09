class User:
    # Define the fields and methods for your object here.
    def _init_(self,name,age):
        self.userName = name
        self.age=age
        self.connections=[]

    def add_connections(self,friend):
        self.connections.append(friend)

    def get_user_name(self):
        return self.userName

    def get_connections(self):
        return self.connections

    def get_age(self):
        return self.age

class Network:
    # Define the fields and methods for your object here.
    def _init_(self):
        groupchat=[]

    def add_ppl_in_gc(friends):
        groupchat.append(friends)

def main():
    # Define the program flow for your user interface here.

# Runs your program.
if __name__ == '__main__':
    main():
