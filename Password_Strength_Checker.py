import string

print()
print("*** PASSWORD STRENGTH CHECKER ***")
print() 

password = input("Enter the password: ")

upper_case = any(1 if c in string.ascii_uppercase else 0 for c in password)
lower_case = any(1 if c in string.ascii_lowercase else 0 for c in password)
speciel = any(1 if c in string.punctuation else 0 for c in password)
digits = any(1 if c in string.digits else 0 for c in password)

characters = [upper_case, lower_case, speciel, digits]

lenght = len(password)

score = 0

if lenght > 8:
    score += 1
if lenght > 12:
    score += 1
if lenght > 17:
    score += 1
if lenght > 20:
    score += 1

print(f"password lenght is {str(lenght)}, adding {str(score)} points!")

if sum (characters) > 1:
    score += 1
if sum (characters) > 2:
    score += 1
if sum (characters) > 3:
    score += 1

print(f"password has {str(sum(characters))} different character types, adding {str(sum(characters) -1)} points!")

if score < 4:
    print(f"The password is weak! Score: {str(score)} /7")
elif score == 4:
    print(f"The password is ok! Score: {str(score)} /7")
elif 4 < score < 6: 
    print(f"The password is pretty good! Score: {str(score)} /7")
elif score > 6:
    print(f"The password is Strong! Score: {str(score)} /7")