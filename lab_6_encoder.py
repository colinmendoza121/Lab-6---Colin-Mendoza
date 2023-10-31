# Defines function to encode user's password
def encoder(password):
    string = ''
    for i in range(len(password)):
        # Shifts each digit up by 3 in password
        string = string + str(int(password[i]) + 3)
    return string


while True:
    # Displays menu for user to choose from
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')
    menu_option = input("Please enter an option: ")
    # Encodes user's inputted password
    if menu_option == '1':
        password = input("Please enter your password to encode: ")
        encoded_password = encoder(password)
        print("Your password has been encoded and stored!\n")
    # Decodes encoded password and displays encoded and original password
    elif menu_option == '2':
        decoded_password = decoder(encoded_password)
        print(f"The encoded password is {encoded_password},", end=' ')
        print(f"and the original password is {decoded_password}.\n")
    # Terminates program
    elif menu_option == '3':
        break
    else:
        print("Error! Please enter a valid menu option.")
