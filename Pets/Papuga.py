from Pets.Pet import Pet
import sys
from pathlib import Path
sys.path.insert(0, str(Path('..', 'source').resolve))

class Papuga(Pet):
    def __init__(self,satiety_points, joy_points):
        satiety_points =satiety_points
        joy_points = joy_points
        super().__init__( satiety_points, joy_points)
        self. textureBeforeEvolve= "Assets/Images/PetsTxt/BeforeEvolution/papuga.png"
        self. textureAfterEvolve = ""
        self. backgroundTexture = "Assets/Images/Backgrounds/AnimalBackgrounds/Dzungla.png"



