
# from operator import itemgetter
#
# transactions = [("Alice", "apple", 2),("Bob", "banana", 3),("Alice", "banana", 1),
# ("Bob", "apple", 4),("Carol", "apple", 1),("Alice", "apple", 1),("Carol", "banana", 2)]
#
# customer_to_fruit = {}
#
# for customer, fruit, count in transactions:
#     if customer not in customer_to_fruit:
#         customer_to_fruit[customer] = {}
#     customer_to_fruit[customer][fruit] = customer_to_fruit[customer].get(fruit, 0) + count
#
# print(customer_to_fruit)


import random


ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def main():

    plaintext_to_cipher = generate_cipher()

    print("The secret code is:", plaintext_to_cipher)

    message = input("Enter the message to encrypt please: ").upper()

    print("Original message:", message)

    encrypted_message = encrypt_message(message, plaintext_to_cipher)

    print("Encrypted:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, plaintext_to_cipher)

    print("Decrypted:", decrypted_message)

def generate_cipher():
    """Shuffle the alphabet."""
    shuffled = ALPHABET.copy()
    random.shuffle(shuffled)
    return {ALPHABET[i]: shuffled[i] for i in range(len(ALPHABET))}
# Alphabet to shuffle, and i iterates through the range length alphabet

def encrypt_message(message, cipher):
    # put the message into the shuffled alphabet cipher
    message_out = []
    for letter in message:
        message_out.append(cipher.get(letter, letter)) # second letter will default if it cant be encrypted, like 0
    return "".join(message_out)
    #out.append(cipher.get(letter.upper(), letter) if letter.isupper() else letter)


def decrypt_message(encrypted, cipher):
    inv = {v: k for k, v in cipher.items()}
    # v:k flips key, value to value, key!
    # normally like {k:v for k, v in d.items()}
    message_out = []
    for letter in encrypted:
        message_out.append(inv.get(letter, letter))
    return "".join(message_out)
main()