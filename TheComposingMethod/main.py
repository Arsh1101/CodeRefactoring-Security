from datetime import datetime

class GeneralSampleClass:
    def get_request_list(request:str) -> list:
        return request.split(":")


    def is_authenticated(request):
        temp = GeneralSampleClass.get_request_list(request)
        return True if temp[0] == "user" and temp[1] == "pass" else False


    def is_authorized(request):
        return True if GeneralSampleClass.get_request_list(request)[2] == "admin" else False

    
    def is_valid_request(request):
        temp = GeneralSampleClass.get_request_list(request)
        return True if temp[3] == "http" and temp[4] == "get" else False
    
    
    def process_request(request):
        return "The result of get http request for the admin ✔️"


class BeforeRefactoring:
    def handle_request(request):
        # Simple is better! 💀
        # It is hard to manage; that is why there is high probability of mistake on authentication here.
        if GeneralSampleClass.is_authenticated(request):
            if GeneralSampleClass.is_authorized(request):
                if GeneralSampleClass.is_valid_request(request):
                    return GeneralSampleClass.process_request(request)
                else:
                    return 'Invalid request'
            else:
                return 'Not authorized'
        else:
            return 'Not authenticated'


class AfterRefactoring:
    # Simple is better! 🤓
    def handle_request(request):
        if not GeneralSampleClass.is_authenticated(request):
            return 'Not authenticated'

        if not GeneralSampleClass.is_authorized(request):
            return 'Not authorized'

        if not GeneralSampleClass.is_valid_request(request):
            return 'Invalid request'

        return GeneralSampleClass.process_request(request)


if __name__ == "__main__":
    print("Hi! This is a test for The Composing Method refactoring to check the security: 🧪")
    print("This is example of a module, which responds to a http get to admin user.")
    print("Before refactoring... 🚫🔃")
    username = input("Username:")
    password = input("Password:")
    requestList = [
        'x:y:admin:http:get',
        f'{username}:{password}:admin:http:post',
        f'{username}:{password}:user:http:get',
        f'{username}:{password}:user:http:post',
        f'{username}:{password}:admin:http:get',
    ]
    for request in requestList:
        print(BeforeRefactoring.handle_request(request))
    print("After refactoring... ✅🔃")
    for request in requestList:
        print(AfterRefactoring.handle_request(request))
