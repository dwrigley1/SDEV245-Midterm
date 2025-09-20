import hashlib
from cryptography.fernet import Fernet

# set minimum so we can see the hashing take place
char_minimum = 5 
user_input = input("Enter a message to be hashed: ")

# keep user in a loop until the minimum character limit is satisfied
while len(user_input) < char_minimum:
    print("Sorry, does not meet the minimum requirement of 5 characters: ")
    user_input = input("Try again: ")
    if len(user_input) >= char_minimum:
        break

hashed_user_input = hashlib.sha256(user_input.encode("utf-8")).hexdigest()
print(hashed_user_input,"\n")

encryption_key = Fernet.generate_key() # method to generate the secret key
f = Fernet(encryption_key) # assignment creates an object
f_text = f.encrypt(hashed_user_input.encode("utf-8"))
print(f_text, "\n")

unhashed_user_input = f.decrypt(f_text).decode()
print(unhashed_user_input, "\n")

# verify encrypted & decrypted values match
if hashed_user_input == unhashed_user_input:
    print("Integrity Verified!")
else:
    print("Something is wrong...")