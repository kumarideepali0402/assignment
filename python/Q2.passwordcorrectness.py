def hasUpperCase(s):
    for c in s:
        if c.isupper():
            return True
    return False

def hasLowerCase(s):
    for c in s:
        if c.islower():
            return True
    return False

def hasDigit(s):
    for c in s:
        if c.isdigit():
            return True
    return False

def hasSpecialChar(s):
    special_chars = "!@#$%^&*"
    for c in s:
        if c in special_chars:
            return True
    return False

def isValidPassword(password, username, lastThreePasswords):
   
    if len(password) < 10:
        print("Password must be at least 10 characters long.")
        return False
    
   
    if not hasUpperCase(password):
        print(" at least two uppercase letters.")
        return False
    if not hasLowerCase(password):
        print(" at least two lowercase letters.")
        return False
    if not hasDigit(password):
        print(" at least two digits.")
        return False
    if not hasSpecialChar(password):
        print("at least two special characters.")
        return False
    
   
    for i in range(len(password) - 2):
        if password[i] == password[i+1] and password[i] == password[i+2]:
            print(" Character should  not repeat more than three times in a row.")
            return False
    
    if username:
        for i in range(len(username) - 2):
            if username[i:i+3] in password:
                print("Password should not contain sequences from the username.")
                return False
    
  
    if password in lastThreePasswords:
        print("Password cannot be the same as  the last three passwords.")
        return False
    
    return True

def main():
    username = input("Username: ")
    lastThreePasswords = [] 
    
    while True:
        password = input("Enter password: ")
        if isValidPassword(password, username, lastThreePasswords):
            print("Password is valid.")
            break

if __name__ == "__main__":
    main()

