earth_seconds = 31557600

class SpaceAge:
    seconds = 0

    def __init__(self, seconds):
        self.seconds = seconds

        space_jam = {
            'earth': earth_seconds,
            'mercury': earth_seconds * 0.2408467,
            'venus': earth_seconds * 0.61519726,
            'mars': earth_seconds * 1.8808158,
            'jupiter': earth_seconds * 11.862615,
            'saturn': earth_seconds * 29.447498,
            'uranus': earth_seconds * 84.016846,
            'neptune': earth_seconds * 164.79132
        }

        for conv_name in space_jam:
           setattr(self,
                   "on_" + conv_name,
                   'return float("{0:.2f}".format(self.seconds / ' + space_jam[conv_name] + ')' )

    # def on_earth(self):
    #     return float("{0:.2f}".format(self.seconds / earth_seconds))
    #
    # def on_mercury(self):
    #     return float("{0:.2f}".format(self.seconds / mercury_conv))
    #
    # def on_venus(self):
    #     return float("{0:.2f}".format(self.seconds / venus_conv))
    #
    # def on_mars(self):
    #     return float("{0:.2f}".format(self.seconds / mars_conv))
    #
    # def on_jupiter(self):
    #     return float("{0:.2f}".format(self.seconds / jupiter_conv))
    #
    # def on_saturn(self):
    #     return float("{0:.2f}".format(self.seconds / saturn_conv))
    #
    # def on_uranus(self):
    #     return float("{0:.2f}".format(self.seconds / uranus_conv))
    #
    # def on_neptune(self):
    #     return float("{0:.2f}".format(self.seconds / neptune_conv))
