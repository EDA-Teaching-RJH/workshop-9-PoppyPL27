import re

def main():
    testEmail = input("give an email you would like to test: ")
    test = CheckEmailValid("testEmail");

def CheckEmailValid(email):
    responseMessage = ""
    if re.search(r"^[a-zA-Z0-0_]+@[a-zA-Z0-9_]+\.(ac.uk|gov.uk|nhs.net)$", email):
        emailHalves = email.split(".")
        if emailHalves[1] == "ac" and emailHalves[2] == "uk":
           responseMessage = "Valid Academic Email"
        elif emailHalves[1] == "gov" and emailHalves[2] == "uk":
           responseMessage = "Valid Government Email"
        elif emailHalves[1] == "nhs" and emailHalves[2] == "net":
            responseMessage = "Valid NHS Email"
    else:
        if re.search(r"^[a-zA-Z0-0_]+@", email):
            responseMessage = "invalid due to unaccepted email type"
        if re.search(r"\.(ac.uk|gov.uk|nhs.net)$", email):
            responseMessage = "invalid due to unaccepted character"
    
    print(responseMessage)
    return responseMessage

if __name__ == "__main__":
    main()