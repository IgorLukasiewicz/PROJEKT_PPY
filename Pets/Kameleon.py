from Pets.Pet import Pet


class Kameleon(Pet):
    def __init__(self):
        satiety_points = 50
        joy_points = 50
        super().__init__(satiety_points, joy_points)
        self. textureBeforeEvolve= "Assets/Images/PetsTxt/BeforeEvolution/KameleonPrzedEwolucje.png"
        self. textureAfterEvolve = ""
        self. backgroundTexture = "Assets/Images/Backgrounds/AnimalBackgrounds/Dzungla.png"


