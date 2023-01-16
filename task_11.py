class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self) -> True or False:
        if self.name is None and self.calories is None:
            return False
        elif isinstance(self.calories, str):
            return False
        elif self.calories < 200:
            return True
        return False

    def is_delicious(self) -> True or False:
        if self.name is None and self.calories is None:
            return False
        return True
