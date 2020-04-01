import random
import string

class Robot():
    name = ""
    priors = set()  # To avoid collisions

    def __init__(self):
        self.reset()

    def reset(self):
        new_name = ""
        name_is_new = False

        while not name_is_new:
            new_name = self.generate_new_robot_name()
            if new_name not in self.priors:
                self.priors.add(new_name)
                name_is_new = True

        self.name = new_name

    def generate_new_robot_name(self):
        robot_letters = random.choices(string.ascii_uppercase, k=2)
        robot_number = str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9))
        return "".join(robot_letters) + robot_number
