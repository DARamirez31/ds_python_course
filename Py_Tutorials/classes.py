import statistics as s

class cricketplayer:
    team_size = 11 #Aplicable for all the players
    def __init__(self, first_name, age, country):
        self.first_name = first_name  #attributes specific for the player
        self.age = age
        self.country = country
        self.scores = [] # List to store scores of the player
    # Method to display player information
    def display(self):
        print(f"First name: {self.first_name}, Age: {self.age}, Country: {self.country}, Scores: {self.scores}")
    # Method to add scores to the players
    def add_score(self, score):
        self.scores.append(score)
    def avg_scores(self):
        return s.mean(self.scores)
    def __str__(self): # String representation of the object
        return f"Player: {self.first_name}, Age: {self.age}, Country: {self.country}, Scores: {self.scores}"
    def get_age(self):
        return self.age

    #OPERATOR OVERLOADING
    def __lt__(self, other):
        self_avg_scores = self.avg_scores()
        other_avg_scores = other.avg_scores()
        return self_avg_scores < other_avg_scores
    def __eq__(self, other):
        self_age = self.get_age()
        other_age = other.get_age()
        return self_age == other_age

# Creating an instance of cricketplayer
player1 = cricketplayer("Virat", 34, "India")
player1.add_score(37)
player1.add_score(47)
player2 = cricketplayer("Joe", 32, "England")
player2.add_score(45)
player2.add_score(55)
print(player1.avg_scores())
print(player2.avg_scores())
player1.display()
player2.display()
print(player1)
print("Team size:", cricketplayer.team_size)
print(player1 < player2)  # Using operator overloading to compare players based on average scores
print(player2 < player1)
print( player1 == player2)  # Using operator overloading to compare players based on age