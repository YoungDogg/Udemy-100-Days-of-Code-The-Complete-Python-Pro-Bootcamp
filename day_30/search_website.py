import os.path


class SearchWebsite:
    """
    Handles searching for website data in the JSON file.
    Checks if the file exists and if the website has associated data.
    """

    def __init__(self, json_handelr, file_name):
        """
        Initializes the SearchWebsite class with a JSONData handelr.

        Args:
            json_handelr (JSONData): An instance of JSONData to manage the JSON file
        """
        self.json_handler = json_handelr
        self.__file_name = file_name

    def search_website(self, website):
        """
        Searches for a website in the JSON file.

        Args:
            website (str): The website to search for.

        Returns:
            dict or None: A dictionary containing the website details (Email/Username, Password)
                          or None if the website does not exist
        """
        if not os.path.exists(self.__file_name):
            return {"message":"No Data File Found", "data":None}

        data = self.json_handler.read()
        if website in data['Website'].values:
            row = data.loc[data['Website'] == website]
            result = {
                "Email/Username": row['Email/Username'].values[0],
                "Password": row["Password"].values[0]
            }
            return {"message": None, "data": result}
        else:
            return {"message":"No Details for the website eixsts", "data": None}


if __name__ == '__main__':
    from day_30.json_controller import JSONData
    from search_website import SearchWebsite

    # Initialize JSONData with the JSON file
    file_name = "data.json"
    json_handler = JSONData(file_name)
    # Initialize SearchWebsite
    search = SearchWebsite(json_handler, file_name)

    # Search for a specific website
    result = search.search_website("apple")
    if result:
        print(f"Website details: {result}")
    else:
        print("Website not found or file does not exist.")
