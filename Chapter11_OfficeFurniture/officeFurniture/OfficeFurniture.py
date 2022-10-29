class OfficeFurniture:

    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def __str__(self):
        description = f"{self.__category} costs {self.__price} and is made of {self.__material} with the dimensions length: {self.__length}ft, width: {self.__width}ft, height: {self.__height}ft."
        return description

    def get_material(self):
        return self.__material

    def get_category(self):
        return self.__category

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price
