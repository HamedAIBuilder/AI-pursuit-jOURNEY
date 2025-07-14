def greet_user():
    """
    Prompts the user for their name and prints a personalized greeting.
    Offers a 'Surprise Me!' option for a random greeting.
    """
    import random

    greetings = [
        'Hello, Universe!',
        'Hi there!',
        'Welcome!',
        'Greetings, Earthling!',
        'Howdy!',
        'Bonjour, le monde!',
        'Hola, Mundo!',
        'Ciao, Mondo!'
    ]

    print("Welcome to the Hello World Greeter!")
    print("Type your name, or type 'surprise' for a random greeting.")
    name = input("Please enter your name (or 'surprise'): ").strip()

    if name.lower() == "hamed":
        print("Hey, it's the awesome AI Director, Hamed!")
        print("Hi Hamed, how are you doing today?")
    elif name.lower() == "surprise":
        print(random.choice(greetings))
    elif name:
        print(f"Hello, {name}!")
        print("Have a nice day!")
    else:
        print("Hello, World!")

# Call the function to run the greeting script
greet_user() 