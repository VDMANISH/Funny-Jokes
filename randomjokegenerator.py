import pyjokes
def tell_me_a_joke():
    joke = pyjokes.get_joke()
    print("\nHere's a joke for you:")
    print(joke)
while True:
    user_input = input("\nDo you want to hear a joke? (yes/no): ").lower()
    if user_input == 'yes':
        tell_me_a_joke()
    elif user_input == 'no':
        print("Okay, no more jokes for now! Have a great day!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
