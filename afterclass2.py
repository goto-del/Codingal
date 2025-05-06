def shutdown():
    user_input = input("Do you want to shutdown the system? (yes/no): ").strip().lower()

    if user_input == "yes":
        print("Shutting down the system.....")
    elif user_input == "no":
        print("Sorry, Shutdown cancelled")
    else:
         print("Invalid input.Please type yes or no.")

shutdown()