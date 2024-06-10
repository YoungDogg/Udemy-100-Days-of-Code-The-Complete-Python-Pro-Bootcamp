import colorgram


class MyColorgram:
    def __init__(self, img='hirst_painting/sample.jpg',extract_num=6):
        """
        Initialize MyColorgram with an image and the number of colors to extract.

        Parameters:
        img (str): Path to the image file.
        extract_num (int): Number of colors to extract.
        """
        self.colors_extracted = colorgram.extract(img, extract_num)
        self.color_list = []
    def append_color_tuple(self):
        """
        Extract RGB tuples from the extracted colors and append them to color_list.
        """
        for i in self.colors_extracted:
            color_tuple = (i.rgb.r,i.rgb.g, i.rgb.b)
            self.color_list.append(color_tuple)

    def display(self):
        print(self.color_list)



