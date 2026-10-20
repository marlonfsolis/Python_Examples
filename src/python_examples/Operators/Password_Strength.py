# Password Strength Checker


# Contains criterial function
def contains_criterial(password: str, criterial: str) -> bool:
    count = 0
    pass_index = 0
    pass_len = len(password)
    special_chars = set("!@#$%^&*()_+")

    while count == 0 and pass_index < pass_len:
        char = password[pass_index]
        match criterial:
            case "uppercase":
                if char.isupper():
                    count += 1
            case "lowercase":
                if char.islower():
                    count += 1
            case "number":
                if char.isdigit():
                    count += 1
            case "special":
                if char in special_chars:
                    count += 1
            case "space":
                if char.isspace():
                    count += 1

        pass_index += 1
    
    return count >= 1  




#Password score
score = 0

#Enter your password and I will tell you how strong it is
print("Enter your password and I will tell you how strong it is")
password = input("Password: ")

#The password must be at least 8 characters long
pass_len = len(password)
if pass_len >= 8:
    score += 1
elif pass_len >= 5:
    score += 0.5
else:
    score += 0

#The password must contain at least one uppercase letter
if contains_criterial(password, "uppercase"):
    score += 1

#The password must contain at least one lowercase letter
if contains_criterial(password, "lowercase"):
    score += 1

#The password must contain at least one number
if contains_criterial(password, "number"):
    score += 1

#The password must contain at least one special character
if contains_criterial(password, "special"):
    score += 1

#Return the password strength
if score >= 4:
    print("Strong")
elif score >= 3:
    print("Medium")
elif score >= 2:
    print("Weak")
else:
    print("Very Weak")

     