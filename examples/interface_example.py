

class Dog(object):

    def __init__(self, name, fur):
        self.name = name
        self.fur = fur

    def speak(self, content, tone):
        if tone == 'good':
            return 'Bark!'
        elif tone == 'bad':
            return 'Growl'


class Person(object):

    def __init__(self, name, mood):
        self.name = name
        self.mood = mood

    def speak(self, content, tone):

        if content == 'What is your name':
            if tone == 'good':
                return self.name
            if tone == 'bad':
                return '{}, why do you care?'.format(self.name)
        else:
            return 'Huh?'
