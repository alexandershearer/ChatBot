from random import choice

#Setting up function for chatbot response depending on user input
def get_bot_response(user_response):
    #Setting up arrays for the bot to choose from randomly
    bot_response_good = ['Keep it up!', 'Good job!', 'Good Game!', 'GG!']
    bot_response_bad = ['Just a bad game!', 'You will do better in the next one!', 'Put it behind you and do better in the next one!',
    'Don\'t stress it!']

    #A if/else statement for the bot to see which input the user done
    if user_response == "good":
        return choice(bot_response_good)
    elif user_response == "bad":
        return choice(bot_response_bad)
    else:
        return "You're gonna do great in the next game!"

print("Hi, welcome to PostGame Bot!")

#Declaring the user_response variable to use in the future
user_response = " "

#Setting up a loop until the user enters a value
while True:
    user_response = input("How did your last game go??:  ")

    if user_response == "quit":
        break

    bot_response = get_bot_response(user_response)
    print(bot_response)

