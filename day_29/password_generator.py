import random
import string


class PasswordGenerator:
    # 12 digits including characters
    def __init__(self):
        self.digits = 12
        self.__pwd_numbers = string.digits
        self.__pwd_lowercase = string.ascii_lowercase
        self.__pwd_uppercase = string.ascii_uppercase
        self.__special = "!@#$%^&*()-_=+"
        self.__pwd_tray = self.__pwd_numbers + self.__pwd_lowercase + self.__pwd_uppercase + self.__special

    def generate_pwd(self):
        password_str = ""
        for _ in range(self.digits):
            password_str += random.choice(self.__pwd_tray)
        return password_str

if __name__ == '__main__':
    p = PasswordGenerator()
    print(p.generate_pwd())
