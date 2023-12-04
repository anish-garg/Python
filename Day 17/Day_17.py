# OOP in python
# Firstly we have to create a class and then in the class there is function __init__ with the self params

# Creating attributes in the class and methods in the class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

# with the help of 'self' attributes are denoted and with the 'user' itself methods are denoted

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Anish"
# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jack"
# print(user_2.username)

user_1 = User("001", "Anish")
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)
user_2 = User("002", "Jack")

user_1.follow(user_2)
# user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

