#!/usr/bin/env python3

class Footwear:
    def __init__(self, brand_name, shoe_size):
        self.brand_name = brand_name
        self._shoe_size = shoe_size
        self.state = "Brand New"

    def get_shoe_size(self):
        return self._shoe_size

    def set_shoe_size(self, size):
        if not isinstance(size, int):
            print("Error: Size must be an integer.")
        else:
            self._shoe_size = size

    def repair(self):
        print("The footwear has been expertly repaired and is ready to wear!")

    shoe_size = property(get_shoe_size, set_shoe_size)

# Example usage
nike_footwear = Footwear("Nike", 9)
nike_footwear.shoe_size = '10'  # This will print an error message
print(nike_footwear.shoe_size)  # This will print the original size (9)
print(nike_footwear.repair())  # This will print the repair message
