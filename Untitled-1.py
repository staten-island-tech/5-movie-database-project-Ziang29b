def account ( email, password):
    email = input("Enter your email: ")
    if "@" not in email:
        print ( "error: you need a @ symbol")
    if not isinstance(email, str):
        print ("Invalid input: Input is not a string.")
    else:
        print ("nice email now for your password")
    
    password = input ("enter your password:")

    if not isinstance(password, str):
        print ("the password must be a string.")

    if len(password) <= 8:
        print ("The password must be at least 8 characters long.")

    if not any(char.isdigit() for char in password):
        print ("The password must include at least one number.")

    if not any(char.isupper() for char in password):
        print ("The password must include at least one uppercase letter.")
    else:
        print (" okay email and password valid")
        print (email, password)