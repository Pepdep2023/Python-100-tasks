user_name = input("Enter your name: ")
has_vowel =  False

for char in user_name:
    if char.lower() in 'aeiou':
        has_vowels = True
        break
print(has_vowel)

