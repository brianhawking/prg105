import OfficeFurniture


class Desk(OfficeFurniture.OfficeFurniture):

    def __init__(self, material, length, width, height, price, location_of_drawers, number_drawers):
        OfficeFurniture.OfficeFurniture.__init__(self, "Desk", material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def __str__(self):
        description = f"The desk costs {self.get_price()} and is made of {self.get_material()} with the dimensions length: {self.get_length()}ft, width: {self.get_width()}ft, height: {self.get_height()}ft. It has {self.__number_drawers} drawers located on the {self.__location_of_drawers} side."
        return description

    def get_number_of_drawers(self):
        return self.__number_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def set_number_of_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers
