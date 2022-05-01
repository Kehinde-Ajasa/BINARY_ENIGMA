# Thhis code is used to decrypt a binary encrypted message in the ascii format
import time
while True:
    print('Please make sure it is in a 8-digit binary format')
    print('')
    ascii_code_input = (input('Enter binary numbers to decrypt: '))


    def open_ascii_values_database():
        """function to help open up the edited format of  the ascii values"""

        with open('C:\\Users\\MY PC\\Desktop\\PYTHON PROJECTS\\ASCII-BINARY.WORD converter\\ENCRYPTION-CODE.txt',
                  'r') as words_numbers:
            ascii_values = words_numbers.readlines()  # getting the values of the ascii_values_file in a list format(readlines)
            return ascii_values


    ascii_values_file = (open_ascii_values_database())



    def extract_binary_numbers(ascii_code_input):
        global ascii_values_file
        """function to help extract binary numbers that can be converted to letters"""

        bin_numbers = []
        val_list = []
        decrypted_message = ''
        count = 0
        for i in range(len(ascii_code_input)):
            binary_number = ascii_code_input[count : (count + 8)]
            count += 8
            if binary_number.isdigit():
                bin_numbers.append(binary_number)
        for i in bin_numbers:
            val = 0
            list_i = list(str(i))
            for m in range(len(list_i)):
                split_m = list_i.pop()
                if split_m == '1':
                    val += pow(2, m)
            val_list.append(val)
        for i in val_list:
            for (w) in ascii_values_file:
                index_of_binary_number = ascii_values_file.index((str(i) + '\n'))
                if (w) == (str(i) + '\n'):
                    decrypted_message += ascii_values_file[(index_of_binary_number + 1)]
        print('CONVERTING..........')
        time.sleep(2)
        print(decrypted_message)
    print(extract_binary_numbers(ascii_code_input), end = '')


    retry_code = input('Do you want to decrypt another message(y/n): ')
    if retry_code == 'y':
        continue
    else:
        break
