import datetime

class Player:
    def __init__(self, fname, lname, birth_year):
        self.fname = fname
        self.lname = lname
        self.birth_year = birth_year

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.birth_year

class tennisplayer(Player):
    def __init__(self, fname, lname, birth_year):
        Player.__init__(self, fname, lname, birth_year) # Call the constructor of the base class using the class name, mandatory to add self
        self.sport = "Tennis"
        self.aces = []

    def get_avg_aces_per_match(self):
        if len(self.aces) == 0:
            return 0
        return sum(self.aces) / len(self.aces)

class cricketplayer(Player):
    def __init__(self, fname, lname, team, birth_year):
        super().__init__(fname, lname, birth_year) # Call the constructor of the base class using super(), not needed to add self
        self.sport = "Cricket"
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

roger  =  tennisplayer("roger", "federer", 1981)
rafael = tennisplayer("rafael", "nadal", 1986)
virat = cricketplayer("virat", "kohli",  "my team",1988)
print(roger.get_age())
virat.add_score(100)