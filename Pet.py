
class Pet:

    def __init__(self, name, satiety_points, joy_points):
        self.name = name
        self.satiety_points = satiety_points
        self.joy_points = joy_points

    def play(self, additional_joy_points, taken_satiety_points):
        self.joy_points += additional_joy_points
        if self.joy_points > 100:
            self.joy_points = 100
        self.satiety_points -= taken_satiety_points
        if self.satiety_points <= 0:
            self.satiety_points = 0

    def feed(self, additional_satiety_points):
        self.satiety_points += additional_satiety_points
        if self.satiety_points > 100:
            self.satiety_points = 100
