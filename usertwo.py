class User:

    
    def __init__(self,first_name,last_name,email,age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"Firstname: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"member: {self.is_rewards_member}")
        print(f"points: {self.gold_card_points}")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.is_rewards_member is True:
            print("user already a member.")

    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print("You dont have enough points.")
            return

        self.gold_card_points -= amount

my_user = User("Chris", "smith", "chris.aning@gmail.com", 40)
my_user2 = User("becky", "kim", "becky.kim@gmqail.com", 30)
# my_user1.display_info().enroll().spend_points(50).display_info()
# my_user2.enroll().spend_points(80).display_info()
# my_user1.display_info().enroll().spend_points(50).display_info()
# my_user2.enroll().spend_points(80).display_info()

my_user.enroll()
my_user2.enroll()
my_user.spend_points(50)
my_user2.spend_points(80)
my_user.display_info()
my_user2.display_info()

