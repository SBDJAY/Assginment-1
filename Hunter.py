class HunterClass: 
    def __init__(self, Resilience, Discipline):
        self.Resilience = Resilience
        self.Discipline = Discipline

user = HunterClass(90,75)
print('Your stats are: ')
print('Resilience: ' + str(user.Resilience), 'Discipline: ' +str(user.Discipline))
        