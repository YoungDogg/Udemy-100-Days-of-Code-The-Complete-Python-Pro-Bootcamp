import colorgram
from typing import List, Tuple


class MyColorgram:
    def __init__(self, img:str='hirst_painting/sample.jpg',extract_num:int=6):
        """
        Initialize MyColorgram with an image and the number of colors to extract.

        Parameters:
        img (str): Path to the image file.
        extract_num (int): Number of colors to extract.
        """
        try:
            self.colors_extracted = colorgram.extract(img, extract_num)
        except Exception as e:
            raise ValueError(f"Error extracting colors: {e}")

        self.color_list: List[Tuple[int,int,int]] = []
    def append_color_tuple(self):
        """
        Extract RGB tuples from the extracted colors and append them to color_list.
        """
        for color in self.colors_extracted:
            color_tuple = (color.rgb.r,color.rgb.g, color.rgb.b)
            self.color_list.append(color_tuple)

    def display(self):
        """
        Display the list of extracted color tuples
        """
        print(self.color_list)



# Example usage:
# colorgram_instance = MyColorgram()
# colorgram_instance.append_color_tuple()
# color_instance.display()






