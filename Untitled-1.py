def account ( email, password):
    email = input("Enter your email: ")
    if "@" not in email:
        return "error: you need a @ symbol"
    elif not isinstance(email, str):
        print("Invalid input: Input is not a string.")
    else:
        print("nice email now for your password")
        