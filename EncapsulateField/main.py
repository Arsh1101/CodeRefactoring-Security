from datetime import datetime


class BeforeRefactoring:
    #Every one can change the flow! 💀
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.is_valid_user():
            self.set_log()
            return "Welcome! 😊"
        else:
            return "You shall not pass! 🧙‍♂️"


    def is_valid_user(self):
        result = False
        with open("users.txt", "r") as file:
            for line in file:
                if f'{self.username} - {self.password}' == line.strip():
                    result = True
                    break
        return result


    def set_log(self):
        now = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f'{self.username} - {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


class AfterRefactoring:
   # The code flow is protected by protected access to the components of the class 🤓
   # The magical '_' in Python! 🪄🐍
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def login(self):
        if self._is_valid_user():
            self._set_log()
            return "Welcome! 😊"
        else:
            return "You shall not pass! 🧙‍♂️"


    def _is_valid_user(self):
        result = False
        with open("users.txt", "r") as file:
            for line in file:
                if f'{self._username} - {self._password}' == line.strip():
                    result = True
                    break
        return result


    def _set_log(self):
        now = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f'{self._username} - {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


    def get_username(self):
        return self._username


    def get_password(self):
        return self._password


if __name__ == "__main__":
    print("Hi! This is a test for Encapsulate Field refactoring to check the security: 🧪")
    print("Before refactoring... 🚫🔃")
    username = input("Username:")
    password = input("Password:")
    bfr = BeforeRefactoring(username, password)
    print(bfr.login())
    #OR you can do this:
    if(bfr.is_valid_user()):
        print("User loged in but we did not make a log! 😲")
    # Even you can change the username and password: 😵‍💫
    bfr.username = "no user"
    bfr.password = "no pass"
    print(bfr.login())
    print("After refactoring... ✅🔃")
    username = input("Username:")
    password = input("Password:")
    afr = AfterRefactoring(username, password)
    print(afr.login())
