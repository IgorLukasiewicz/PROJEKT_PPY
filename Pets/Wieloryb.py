from Pets.Pet import Pet


class Wieloryb(Pet):
    def __init__(self,satiety_points, joy_points):
        satiety_points = satiety_points
        joy_points = joy_points
        super().__init__(satiety_points, joy_points)
        self. textureBeforeEvolve= "Assets/Images/PetsTxt/BeforeEvolution/wieloryb.png"
        self. textureAfterEvolve = ""
        self. backgroundTexture = "Assets/Images/Backgrounds/AnimalBackgrounds/Ocean.png"


