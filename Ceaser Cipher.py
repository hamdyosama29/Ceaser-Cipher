import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation

ciphra = input("Enter the text to encrypt:>> ").lower()
num = int(input("Enter the shift value: "))
action = input("Do you want to Encrypt or Decrypt? (E/D): ").lower()
flash = ''
try:
    if action == "e":
        num = -num
    elif action == "d":
        for char in ciphra:
            if char in lowercase:
                c = lowercase.index(char)
                result = num + c
                index = result % 26
                flash  += lowercase[index] 
            elif char in uppercase:
                c = uppercase.index(char)
                result = num + c
                index = result % 26
                flash  += uppercase[index]
            elif char in punctuation:
                c = punctuation.index(char)
                result = num + c
                index = result % 26
                flash  += punctuation[index]
            else:
                flash += char
except Exception as error:
    print(error)
print(flash)
