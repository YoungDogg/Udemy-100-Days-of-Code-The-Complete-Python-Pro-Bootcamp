from day_26.NatoAlphabet import NatoAlphabet
from error_handle import ErrorHandle


class Main:
    def __init__(self):
        self.n_alphabet = NatoAlphabet()
        self.e_handle = ErrorHandle()


if __name__ == '__main__':
    m = Main()
    m.n_alphabet.setup()
    word = m.e_handle.check_input_error()
    result = m.n_alphabet.result(word)
    print(result)
