import random
import string

def password_generator(length):
    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation 
    if length < 4:
        print("Length of the password should be at least 4 characters.")
        return None
    if length >= 4:
        print("Password on thr way..........")
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the length of the password (minimum 4 characters): "))
    password = password_generator(length)
    if password:
         print("Your generated Password: ", password)
         
if __name__ == "__main__":
    main()