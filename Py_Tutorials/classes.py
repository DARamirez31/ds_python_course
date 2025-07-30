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
        return print(s.mean(self.scores))
    def __str__(self): # String representation of the object
        return f"Player: {self.first_name}, Age: {self.age}, Country: {self.country}, Scores: {self.scores}"

# Creating an instance of cricketplayer
player1 = cricketplayer("Virat", 34, "India")
player1.add_score(37)
player1.add_score(47)
player2 = cricketplayer("Joe", 32, "England")
player2.add_score(45)
player2.add_score(55)
player1.avg_scores()
player2.avg_scores()
player1.display()
player2.display()
print(player1)
print("Team size:", cricketplayer.team_size)