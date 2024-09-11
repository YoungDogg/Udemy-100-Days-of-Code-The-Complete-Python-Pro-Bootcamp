import pandas
# get number of how many each color squirrels are and make it as csv file


def squirrel():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240830.csv")

    color_diversity_list = list(data["Primary Fur Color"].dropna().unique())

    number_list = []
    for color in color_diversity_list:
        number_list.append(len(data[data["Primary Fur Color"] == color]))

    data_dict = {
        "color":coolr_diversity_list,
        "number":number_list
    }

    data_csv = pandas.DataFrame(data_dict).to_csv("squirrel_fur_population")



if __name__ == '__main__':
    squirrel()
