class User:
    # Define the fields and methods for your object here.
    def __init__(self,first,last,username,age):
        self.firstname=first
        self.lastname=last
        self.username = username
        self.age=age
        self.friends=[]

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

# entire network i.e all users
class Network:

    # Define the fields and methods for your object here.
    def __init__(self):
        self.users=[]

    def checkUsername(self, username):
        taken=True
        while taken:
            if username in self.users:
                print("that username is already taken. Choose another one")
            else:
                self.users.append(username)
                taken=False

    def getTotalUsers(self):
        return len(self.users)

    def checkUsersExist(self,username):
        exist=False
        if username in self.users:
            exist=True
        else:
            print("This user does not exist. Add someone else")
            return False

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
        y=Network()
        first=input("first name:")
        last=input("last name:")
        username=input("username:")
        y.checkUsername(username)
        age=input("age:")
        y.profileInfo()

    def profileInfo(self):
        x= User(first,last,username,age)
        print("Profile:")
        print(x.getFullName())
        print(x.getUserName())
        print(x.getAge())

def mainPage():
    y=Network()
    action=input("What do you want to do today? (a) add a new user, (b) add friends, (c)view profile, (d)see total users, (e)exit")
    if action == "a":
        y.makeAcc()
        mainPage()
    elif action=="b":
        friend=input("who?")
        y.addConnections(friend)
        mainPage()
    elif action=="c":
        y.profileInfo()
        mainPage()
    elif action=="d":
        y.getTotalUsers
    else:
        print("BYE")


def main():
    mainPage()



main()
