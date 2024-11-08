import random
import string


class PasswordGenrator:
    # 12 digits including characters
    def __init__(self):
        self.digits = 12
        self.__pwd_numbers = string.digits
        self.__pwd_lowercase = string.ascii_lowercase
        self.__pwd_uppercase = string.ascii_uppercase
        self.__special = "!@#$%^&*()-_=+"
        self.__pwd_tray = self.__pwd_numbers + self.__pwd_lowercase + self.__pwd_uppercase + self.__special

    def generate_pwd(self):
        print('hi')
        password_str = ""
        for _ in range(self.digits):
            password_str += self.__pwd_tray[random.randint(0, len(self.__pwd_tray)-1)]
            print(f'password_str: {password_str}')
        return password_str

if __name__ == '__main__':
    p = PasswordGenrator()
    print(p.generate_pwd())
