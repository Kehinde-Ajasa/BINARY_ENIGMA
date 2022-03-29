#  This code is used to create an encrypted binary message i.e it helps cocert letters to binary
word_to_encrypt = input('Enter the word you would like to convert to binary:  ')


def open_encrypt_database():
    with open('C:\\Users\\MY PC\\Desktop\\PYTHON PROJECTS\\ASCII-BINARY.WORD converter\\ENCRYPTION-CODE.txt',
              'r') as encode:
        encryption_file = encode.readlines()
        return encryption_file


open_encrypt_file = (open_encrypt_database())


def get_number_to_convert(word_to_encrypt):
    global open_encrypt_file
    for i in word_to_encrypt:
        index_of_letters = open_encrypt_file.index((i + '\n'))
        if (i + '\n') in open_encrypt_file:
            number_to_convert = int(open_encrypt_file[(index_of_letters - 1)])
            binary_format = (bin(number_to_convert))
            ascii_format = binary_format[2:]
            if ascii_format == '100000':
                print(f'|{ascii_format}|', end='')
                continue
            print(f'({ascii_format})', end='')
            continue
    return 'ENCRYPTED'


print(get_number_to_convert(word_to_encrypt))

encrypt_new_word = input('Would you like to encrypt another word?(y/n):  ')
if encrypt_new_word == 'y':
    new_word = input('Enter new word:  ')
    print(get_number_to_convert(new_word))
else:
    print('PROGRAM FINISHED!!!')
