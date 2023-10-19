
class User:

     def __init__(self, user_id, username):
         # create the constructor by using the special function __init__ to initialize the attribute
          print("new Constructor creating")
          self.id = user_id
          self.username = username
          self.followers = 0
          self.follwing = 0

     def follow(self,user):
         user.followers +=1
         self.follwing +=1


user_1 = User("007","james")
user_2 = User("001","john doe")

user_1.follow(user_2)

print(user_2.followers)
print(user_2.follwing)
print(user_1.follwing)
