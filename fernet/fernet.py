from cryptography.fernet import Fernet

def load_key(key_location):
	key = open(key_location, "rb").read()

	return key

def decrypt_file(file_location, key):
	f = Fernet(key)
	with open(file_location, "rb") as file:
		encrypted_data = file.read()
		decrypted_data = f.decrypt(encrypted_data)

	with open("./decrypted.txt", "wb") as file:
		file.write(decrypted_data)

def run():
	file_location = input("Enter the location of the encrypted file: ")
	key_location = input("Enter the location of the key: ")
	key = load_key(key_location)
	decrypt_file(file_location, key)

if __name__ == '__main__':
	run()