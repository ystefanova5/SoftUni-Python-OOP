from project.cat import Cat


class Tomcat(Cat):
    GENDER = "Male"
    SOUND = "Hiss"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.GENDER)
