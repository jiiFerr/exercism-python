earth_seconds = 31557600
mercury_conv = earth_seconds * 0.2408467
venus_conv = earth_seconds * 0.61519726
mars_conv = earth_seconds * 1.8808158
jupiter_conv = earth_seconds * 11.862615
saturn_conv = earth_seconds * 29.447498
uranus_conv = earth_seconds * 84.016846
neptune_conv = earth_seconds * 164.79132


class SpaceAge:
    seconds = 0

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return float("{0:.2f}".format(self.seconds / earth_seconds))

    def on_mercury(self):
        return float("{0:.2f}".format(self.seconds / mercury_conv))

    def on_venus(self):
        return float("{0:.2f}".format(self.seconds / venus_conv))

    def on_mars(self):
        return float("{0:.2f}".format(self.seconds / mars_conv))

    def on_jupiter(self):
        return float("{0:.2f}".format(self.seconds / jupiter_conv))

    def on_saturn(self):
        return float("{0:.2f}".format(self.seconds / saturn_conv))

    def on_uranus(self):
        return float("{0:.2f}".format(self.seconds / uranus_conv))

    def on_neptune(self):
        return float("{0:.2f}".format(self.seconds / neptune_conv))
