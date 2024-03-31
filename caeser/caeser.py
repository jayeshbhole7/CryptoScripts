import string

def decrypt_text(ciphertext, key):
	decrypted_plaintext = ''

	for c in ciphertext:
		if c.isupper():
			alphabet = string.ascii_uppercase
		elif c.islower():
			alphabet = string.ascii_lowercase
		else:
			decrypted_plaintext += c
			continue
		
		position = alphabet.find(c)
		shifted_position = (position - int(key)) % 26
		plaintext_letter = alphabet[shifted_position]
		decrypted_plaintext += plaintext_letter

	return decrypted_plaintext


def run():
	# pass
	ciphertext = input("Enter the caeser Ciphertext: ")
	key = input("Enter the key: ")
	plaintext = decrypt_text(ciphertext, key)
	print(f"The decrypted message is: {plaintext}")

if __name__ == '__main__':
	run()
