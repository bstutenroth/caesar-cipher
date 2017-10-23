
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 5
new_message = " "
message = raw_input("please enter a message: ")
for letter in message:
    position = alphabet.find(letter)
    new_position = (position + key) % 26
    new_letter = alphabet[new_position]
    new_message += new_letter
print "your original message is: " + (message)
print "your new message is: " + (new_message)

decoded_message = " "
encrypted_message = raw_input("please enter an encrypted message: ")
for letter in encrypted_message:
    position = alphabet.find(letter)
    new_position = (position - key) % 26
    new_letter = alphabet[new_position]
    decoded_message += new_letter
print "the encryped message says: " + (decoded_message)
