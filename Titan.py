class TitanClass: 
    def __init__(self, Resilience, Discipline):
        self.Resilience = Resilience
        self.Discipline = Discipline

user = TitanClass(110, 50)
print('Your stats are: ')
print('Resilience: ' + str(user.Resilience), 'Discipline: ' +str(user.Discipline))