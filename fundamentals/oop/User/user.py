class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print("User is a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True    

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print("Points spents") 
        else:
            print("Insufficient points")   

# Create a user instance and call the display_info method to the test
user1 = User("Arlette", "Alim", "arlettealim@gmail.com", 25)
user1.display_info()

# call the enroll method on the user
user1.enroll()

# create 2 more instances of the User class
user2 = User("Jane", "Mall", "janemall@gmail.com", 50)
user3 = User("Ana", "Smith", "anasmith@gmail.com", 30)

# Implement the spend_points method
user1.spend_points(50)

# Call the enroll method on the second user.
user2.enroll()

# have the second user spend 80 points
user2.spend_points(80)

# Call the display method on all the users.
user1.display_info()
user2.display_info()
user3.display_info()

# bonus
user1.enroll()

# Bonus
user3.spend_points(40)