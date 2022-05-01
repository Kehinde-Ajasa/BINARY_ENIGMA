#  This code is used to create an encrypted binary message i.e. it helps covert letters to binary

while True:
    word_or_sentence_to_encrypt = input('Enter the word you would like to convert to binary:  ')


    def open_ascii_values_database():
        """function to help open up the edited format of  the ascii values"""

        with open('C:\\Users\\MY PC\\Desktop\\PYTHON PROJECTS\\ASCII-BINARY.WORD converter\\ENCRYPTION-CODE.txt',
                  'r') as words_numbers:
            ascii_values = words_numbers.readlines()  # getting the values of the ascii_values_file in a list format(readlines)
            return ascii_values


    ascii_values_file = (open_ascii_values_database())


    def convert_to_binary(word_or_sentence_to_encrypt):
        """function to check the number of a letter in the ascii format and convert to binary"""

        global ascii_values_file  # Calling the variable from outer scope
        for i in word_or_sentence_to_encrypt:
            index_of_letters = ascii_values_file.index((i + '\n'))
            if (i + '\n') in ascii_values_file:
                number_to_convert = int(ascii_values_file[(index_of_letters - 1)])
                binary_format = (bin(number_to_convert))
                ascii_format = binary_format[2:]
                eight_letter_format = (8 - len(ascii_format)) * '0'
                print(f'{eight_letter_format + ascii_format}', end='')
                continue
        return ''


    print(convert_to_binary(word_or_sentence_to_encrypt))

    encrypt_new_word_or_sentence = input('Would you like to encrypt another word?(y/n):  ').lower()
    if encrypt_new_word_or_sentence == 'y':
        new_word = input('Enter new word:  ')
        print(convert_to_binary(new_word))
    else:
        print('PROGRAM FINISHED!!!')
        break
