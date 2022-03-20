class User:
    def __init__(self, username):
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, username):
        self.following += 1
        username.followers += 1

    def buy_followers(self, number_of_bought_followers):
        self.followers += number_of_bought_followers


jskolnicki = User('jskolnicki')
zach_spangs_19 = User('zach_spangs_19')

jskolnicki.follow(zach_spangs_19)

print(jskolnicki.following)
print(zach_spangs_19.followers)

zach_spangs_19.follow(jskolnicki)

print(f"Jared just picked up a new follower! He now has: {jskolnicki.followers}")

jskolnicki.buy_followers(10000)

print(f"Jared just bought some followers! He now has: {jskolnicki.followers}")