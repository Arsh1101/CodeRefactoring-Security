from datetime import datetime


class BeforeRefactoring:
    def login(username: str, password: str) -> str:
        #File access, Debug, Validations on inputs... 💀
        # check user
        with open("users.txt", "r") as file:
            for line in file:
                if f'{username} - {password}' == line.strip():
                    break
            else:
                return "You shall not pass! 🧙‍♂️"
        # add log
        now = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f'{username} - {now.strftime("%Y-%m-%d %H:%M:%S")}\n')

        return "Welcome! 😊"


class AfterRefactoring:
    def login(username: str, password: str) -> str:
        #Solved!🤓
        if AfterRefactoring.is_valid_user(username, password):
            AfterRefactoring.set_log(username)
            return "Welcome! 😊"
        else:
            return "You shall not pass! 🧙‍♂️"


    def is_valid_user(username: str, password: str) -> str:
        result = False
        with open("users.txt", "r") as file:
            for line in file:
                if f'{username} - {password}' == line.strip():
                    result = True
                    break
        return result


    def set_log(username: str) -> None:
        now = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f'{username} - {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


    def is_valid_from_sql():
        #Secrets from Files that are already Ignored by Git
        pass


    def is_valid_from_api():
        pass


    def set_session():
        pass


    def send_api():
        pass


if __name__ == "__main__":
    print("Hi! This is a test for Extract Method refactoring to check the security: 🧪")
    print("Before refactoring... 🚫🔃")
    username = input("Username:")
    password = input("Password:")
    print(BeforeRefactoring.login(username, password))
    print("After refactoring... ✅🔃")
    username = input("Username:")
    password = input("Password:")
    print(AfterRefactoring.login(username, password))