import random

responses = {
    "hi": ["Hello! Ready for some movie magic?", "Hey there! Want a movie suggestion?"],
    "hello": ["Hi! Looking for something to watch?", "Hello! Let's find your next favorite movie."],
    "recommend a movie": ["Sure! What genre are you in the mood for?", "Of course! Do you like action, comedy, drama, or something else?"],
    "i like action": ["try 'Mad Max: Fury Road'" , "John Wick'!", "Gladiator", " Die Hard is a classic!"],
    "i like comedy": ["How about 'The Hangover' " , "Superbad", "'Step Brothers' always brings the laughs!"],
    "i like drama": ["You might enjoy 'The Shawshank Redemption'" , "Forrest Gump", "'The Godfather' is a masterpiece!"],
    "thank you": ["You're welcome! Enjoy your movie!", "Anytime! Grab some popcorn!"],
    "bye": ["Goodbye! See you at the movies!", "Catch you later, movie buff!"],
    "default": ["Can you tell me what kind of movies you like?", "I'm not sure I got that. Could you rephrase?"]
}

def generate_responses(user_input):
    user_input = user_input.lower()
    chatbot_response = responses.get(user_input, responses["default"])
    return random.choice(chatbot_response)

while True:
    user_input = input("User: ")
    chatbot_response = generate_responses(user_input)
    print("Chatbot:", chatbot_response)
    if user_input.lower() == "bye":
        break



