class WarlockClass: 
    def __init__(self, Resilience, Discipline):
        self.Resilience = Resilience
        self.Discipline = Discipline

user = WarlockClass(80, 99)
print('Your stats are: ')
print('Resilience: ' + str(user.Resilience), 'Discipline: ' +str(user.Discipline))
