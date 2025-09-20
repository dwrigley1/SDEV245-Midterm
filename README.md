This script is an example of using SHA256 hashing & generating an encryption key.

A pre-set input value of a 5 character minimum is set & keeps the user in a "while" loop until that minimum requirement is satisifed.

Once the minimum requirements are met, the user's input is hashed via the use of the hashlib library & its encode() method.

An encryption key is generated, by the use of the cryptography.fernet library.

The afforementioned key then encrypts the hashed text.

Then it goes on to decrypt the key, resulting in the original hashed text. 

Finally, an if/else conditional is used to validate whether or not the pre & post encrypted texts are the same.
