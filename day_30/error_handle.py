class NatoAlphabetErrorHandle:
    @staticmethod
    def check_input_error():
        while True:
            user_input = input("Enter a word: ").upper()

            if len(user_input) < 1:
                print("Error: You didn't type anything. Type a word")
                continue

            if not user_input.isalpha():
                print(f"'{user_input}' included non letters. Try again.")
                continue
            else:
                return user_input


if __name__ == "__main__":
    e = NatoAlphabetErrorHandle()
    print(e.check_input_error())
