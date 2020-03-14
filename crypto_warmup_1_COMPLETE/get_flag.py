import string
alphabet = string.ascii_lowercase
num_letters = len(alphabet)

message = 'llkjmlmpadkkc'
key = 'thisisalilkey'

# Create Vigenere table
def create_vigenere_table():
    vigenere_table = []
    for increment in range(0, num_letters):
        viginere_row = []
        for i in range(0 + increment, num_letters + increment):
            index = i % num_letters
            viginere_row.append(alphabet[index])
        vigenere_table.append(viginere_row)
    return vigenere_table

def print_table(table):
    for row in table:
        print(' '.join(row))


# El proceso es el siguiente:
# Buscamos en la columna de la T (porque la key empieza por la letra T). Bajamos en la columna de la T hasta que encontremos una L (la primera letra del mensaje).
# Y vamos repitiendo este proceso por toda la key/mensaje
def decrypt_vigenere(message, key):
    print('Message:' + message)
    print('Key:' + key)
    decrypted_message = '' 
    # iterate over each char of the message / key (they have the same length)
    for i in range(len(key)):
        message_letter = message[i]
        key_letter = key[i]

        # search the column of the letter of the key.
        # For example T is in the 19 column
        key_pos = alphabet.find(key_letter)

        # Find in this column the letter of the message
        for y in range(len(vigenere_table)):
            if vigenere_table[y][key_pos] == message_letter:
                decrypted_letter = alphabet[y]
                print(decrypted_letter)
                decrypted_message = decrypted_message + decrypted_letter 
    print(decrypted_message)


vigenere_table = create_vigenere_table()
print_table(vigenere_table)
decrypt_vigenere(message, key)




