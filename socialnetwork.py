class User:
    # Define the fields and methods for your object here.
    def __init__(self,first,last,username,age):
        self.firstname=first
        self.lastname=last
        self.username = username
        self.age=age
        self.friends=["Masfi"]

    def addFriend(self,friend):
        self.friends.append(friend)

    def getFullName(self):
        return self.firstname + " " + self.lastname

    def getUserName(self):
        return self.username

    def getAge(self):
        return self.age

    def getConnections(self):
        return self.friends

    def printUser(self):
        print (self.getFullName())
        print (self.getUserName())
        print (self.getAge())
# entire network i.e all users
class Network:

    # Define the fields and methods for your object here.
    def __init__(self):
        self.users=["Masfi", "Yuki", "Lena", "Leyla", "Nick"]

    def checkUsername(self, username):
        if username in self.users:
            print("that username is already taken. Choose another one")
            self.makeAcc()
        else:
            self.users.append(username)
            taken=False

    def getUsersList(self):
        return self.users

    def getTotalUsers(self):
        print (len(self.users))
        print (self.users)

    # def checkUsersExist(self,username):
    #     exist=False
    #
    #     if username in self.users:
    #
    #
    #     else:
    #         print("This user does not exist. Add someone else")


    def addConnections(self,user2):
        for i in range(len(self.friends)):
            checkUsersExist()
            if user2 in self.friends:
                print("You are already connected")
            else:
                self.friends.append(user2)
                user2.friends.append(self)
                print("You are now friends")

    def makeAcc(self):
        first=input("first name:")
        last=input("last name:")
        username=input("username:")
        self.checkUsername(username)
        age=input("age:")


def mainPage():
    y=Network()
    x=User("Yuki", "Fang", "beep", "17")
    action=input("What do you want to do today? (a) add a new user, (b) add friends, (c)view profile, (d)see total users, (e)exit")
    if action == "a":
        y.makeAcc()
        print(y.getUsersList())
        mainPage()
    elif action=="b":
        friend=input("who?")
        x.addFriend(friend)
        print(x.getConnections())
        mainPage()
    elif action=="c":
        x.printUser()
        mainPage()
    elif action=="d":
        y.getTotalUsers()
    else:
        print("BYE")


def main():
    mainPage()



main()
