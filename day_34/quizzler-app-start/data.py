import requests

class QuestionData:

    def __int__(self):
        self.question_set = 0

    def fetch_100_questions(self):

        parameters = {
            "amount": 100,
            "type": "boolean"
        }
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()

        return response.json()["results"]

    def fetch_new_questions(self):
        while self.question_set < 10:
            self.question_set += 1
        self.fetch_100_questions()


if __name__ == "__main__":
    import time

    count = 0
    while count < 3:

        print(fetch_new_questions())
        count += 1
        time.sleep(7)
