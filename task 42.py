user_name = input("Enter you name: ")
has_vowel = False
index = 0

while index < len(user_name):
    if  user_name[index] in 'aeiou': 
        has_vowel = True
        break
    index += 1
print(has_vowel)

