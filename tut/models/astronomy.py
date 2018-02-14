class Planet:
    def __init__(self, name: str, dist: float):
        """
        Creates a planet with the following parameters
        :param name: the name of planet
        :param dist: the distance of (AU) the planet from it's sun
        """
        self.name = name
        self.dist = dist
