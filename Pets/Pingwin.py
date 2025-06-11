import sys
from pathlib import Path
sys.path.insert(0, str(Path('..', 'source').resolve))

from Pets.Pet import Pet


class Pingwin(Pet):
    def __init__(self,satiety_points, joy_points):
        satiety_points = satiety_points
        joy_points = joy_points
        super().__init__(satiety_points, joy_points)
        self. textureBeforeEvolve= "Assets/Images/PetsTxt/BeforeEvolution/pingwin.png"
        self. textureAfterEvolve = ""
        self. backgroundTexture = "Assets/Images/Backgrounds/AnimalBackgrounds/Antakrtyda.png"



