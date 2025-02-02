import requests

class QuestionData:

    def __init__(self):
        # Index of which set to return next (0-based).
        self.question_set_index = 0

        # We will store all 100 fetched questions in this list
        self.all_questions = []
        # Call the method once here (or you can decide to do it lazily).
        self.fetch_100_questions()

    def fetch_100_questions(self):

        parameters = {
            "amount": 50,
            "type": "boolean"
        }
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()

        # Store the results
        self.all_questions = response.json()["results"]
        print(f"length of fetched question: {len(self.all_questions)}")
        # Reset the index whenever new data is fetched
        self.question_set_index = 0

    def fetch_new_questions(self):
        """
        Returns a set of 10 questions each time it is called.
        Once we reach the end (10th set), we either:
          - Return None to indicate no more sets, OR
          - Optionally fetch another 100 questions again and reset.
        """
        # Each time fetch_new_questions is called, we return a slice of the questions
        # 10 questions per set -> sets are all_questions[0:10], [10:20], [20:30], ...

        # If we've exhausted all sets, we could decide to:
        # just return None.
        if self.question_set_index >= 10:
            return None

        start_idx = self.question_set_index * 10
        end_idx = start_idx + 10
        question_subset = self.all_questions[start_idx:end_idx]

        self.question_set_index += 1    # move to next set
        return question_subset




if __name__ == "__main__":
    q = QuestionData()
    count = 0
    while count < 5:

        print(q.fetch_new_questions())
        count += 1
