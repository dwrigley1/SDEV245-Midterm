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

print(f"\nOriginal User Input\n{user_input}\n")

hashed_user_input = hashlib.sha256(user_input.encode("utf-8")).hexdigest()
print(f"User Input Hashed via SHA-256\n{hashed_user_input}\n")

generate_encryption_key = Fernet.generate_key() # method to generate the secret key
encryption_key = Fernet(generate_encryption_key) # assignment creates an object

encrypted_text = encryption_key.encrypt(hashed_user_input.encode("utf-8"))
print(f"Encryption Key Generated via Fernet\n{encrypted_text}\n")

decrypted_hashed_user_input = encryption_key.decrypt(encrypted_text).decode()
print(f"Encryption Key Has Been Decrypted, Original Hashed Value Below\n{decrypted_hashed_user_input}\n")

# verify encrypted & decrypted values match
if hashed_user_input == decrypted_hashed_user_input:
    print("Hash Comparison Verified Integrity!")
else:
    print("Something Is Wrong...")