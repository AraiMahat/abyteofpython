class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('Initializing {}'.format(self.name))

        Robot.population += 1

    def __del__(self):
        print('{} is being destroyed!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working.'.format(Robot.population))

    def say_hi(self):
        print('Greetings, my masters call me {}.'.format(self.name))

    def howMany():
        print('We have {:d} robots.'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.howMany()

print('\nRobots can do some work here.\n')

print('Robots have finished their work. So let\'s destroy them.')

del droid1
del droid2

Robot.howMany()