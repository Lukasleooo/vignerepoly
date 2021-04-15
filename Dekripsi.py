directory = str(input("Masukkan directory file .txt anda : "))
f = open(directory, "r")
file_contents = f.read()
print(file_contents)
alphabet = "abcdefghijklmnopqrstuvwxyz"

def polybiusDecrypt(file_contents) :
    s1 = list(file_contents)
    decpt = ""

    for i in range(0,len(file_contents),2):
        r = int(s1[i])
        c = int(s1[i+1])
        ch = chr(((r-1)*5+c+96))
        if (ord(ch)-96>=10):
            ch = chr(((r-1)*5+c+96+1))
        ch1 = str(ch)
        decpt = decpt + ch1
    return decpt
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

poly = polybiusDecrypt(file_contents)

def decrypt(poly, key):
    decrypted = ""
    split_encrypted = [
        poly[i : i + len(key)] for i in range(0, len(poly), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted

def main():

    key = input("Masukkan key : ")
    decrypted_message = decrypt(poly, key)
    print("Decrypted message: " + decrypted_message)
    f = open(directory, "w")
    f.write(decrypted_message)
    f.close()

main()
import os
os.system(directory)
