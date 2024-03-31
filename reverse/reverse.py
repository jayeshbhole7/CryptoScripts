def decrypt_text(ciphertext):
    # pass
    plaintext = reverse_text(ciphertext)
    return plaintext

def reverse_text(message):
    # pass
    reversed = ''
    i = len(message) - 1
    while i >= 0:
        reversed += message[i]
        i -= 1
    
    return reversed

def run():
    ciphertext = input("Enter the text: ")
    choice = input("Do you want to decrypt? (y/n): ")
    if choice == 'y':
        print(decrypt_text(ciphertext))


    

if __name__ == '__main__':
    run()