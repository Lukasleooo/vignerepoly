print("Contoh directory: C:\\uts\\uts.txt")
directory = str(input("Masukkan directory file .txt anda : "))
f = open(directory, "r")
file_content = f.read()
print (file_content)
words = file_content.split()
number_of_words = len(words)
file_contents = file_content.replace(" ", "")
alphabet = "abcdefghijklmnopqrstuvwxyz"

if number_of_words >= 50 :
    #Membuat dictionary dari variabel alphabet
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))


    def encrypt(message, key):
        encrypted = ""
        split_message = [
            message[i : i + len(key)] for i in range(0, len(message), len(key))
        ]

        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                encrypted += index_to_letter[number]
                i += 1

        return encrypted

    message = file_contents
    key = input("Masukkan key : ")
    encrypted_message = encrypt(message, key)
    print("Encrypted message: " + encrypted_message)



    def polybiusEncrypt(encrypted_message):
        # convert each character to its encrypted code
        encpt = ""
        for char in encrypted_message:

            # finding row of the table
            row = int((ord(char) - ord("a")) / 5) + 1

            # finding column of the table
            col = ((ord(char) - ord("a")) % 5) + 1

            # if character is 'k'
            if char == 'k':
                row = row - 1
                col = 5 - col + 1

            # if character is greater than 'j'
            elif ord(char) >= ord("j"):
                if col == 1:
                    col = 6
                    row = row - 1
                col = col - 1
            r = str(row)
            c = str(col)
            encpt = encpt+r+c
        return encpt


    # print the cipher of file contents
    result = polybiusEncrypt(encrypted_message)
    print(result)
    f = open(directory, "w")
    f.write(result)
    f.close()
    import os
    os.system(directory)
else :
    print('File kurang dari 50 kata')