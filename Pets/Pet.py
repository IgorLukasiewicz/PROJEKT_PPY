class Pet:

    def __init__(self, satiety_points, joy_points):
        self._name = None  # na początku brak imienia
        self.satiety_points = satiety_points
        self._joy_points = joy_points
        self.textureBeforeEvolve = ""
        self.textureAfterEvolve = ""
        self.backgroundTexture = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value.strip()
        else:
            raise ValueError("Imię musi być niepustym tekstem.")

    @property
    def joy_points(self):
        return self._joy_points

    @joy_points.setter
    def joy_points(self, value):
        if value < 0:
            self._joy_points = 0
        elif value > 100:
            self._joy_points = 100
        else:
            self._joy_points = value

    def play(self, additional_joy_points, taken_satiety_points):
        self.joy_points += additional_joy_points  # używa settera
        self.satiety_points -= taken_satiety_points
        if self.satiety_points <= 0:
            self.satiety_points = 0

    def feed(self, additional_satiety_points):
        self.satiety_points += additional_satiety_points
        if self.satiety_points > 100:
            self.satiety_points = 100
