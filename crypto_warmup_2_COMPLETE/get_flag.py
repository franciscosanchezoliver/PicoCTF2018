import string

message = "cvpbPGS{guvf_vf_pelcgb!}"
message =  message.lower()
alphabet = string.ascii_lowercase
FACTOR = 13

# ROT13 consiste en mover la letra 13 posiciones
decrypted_message = ''
for i in range(len(message)):
    message_letter = message[i]
    if message_letter not in string.punctuation:
        letter_pos = alphabet.find(message_letter)
        decrypted_message = decrypted_message + alphabet[(letter_pos + FACTOR) % len(alphabet)]
    else:
        decrypted_message = decrypted_message + message_letter

print(decrypted_message)

