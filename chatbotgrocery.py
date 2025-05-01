import re  # Import the regular expressions module to use pattern matching

# Function to generate chatbot responses based on user input
def chatbot_response(user_input):
    # Convert user input to lowercase for consistent pattern matching
    user_input = user_input.lower()

    # Dictionary containing regex patterns and their corresponding chatbot responses
    responses = {
        r"\b(1|hello|hi|hey)\b": " Hello! Welcome to our grocery store. How can I help you today?",
        r"\b(2|how are you)\b": "I'm just a bot, but I'm here to assist you with groceries!",
        r"\b(3|order status|track order)\b": "Please provide your order ID to check the status.",
        r"\b(4|shipping time|delivery time)\b": "We offer same-day delivery and standard shipping (3-5 business days).",
        r"\b(5|return policy)\b": "You can return items within 7 days if unopened. Would you like help with a return?",
        r"\b(6|thank you|thanks)\b": " You're welcome! Let me know if you need anything else.",
        r"\b(7|price|cost)\b": "Please specify the product name to check its price.",
        r"\b(8|milk)\b": "Milk is 30rs per liter.",
        r"\b(9|eggs)\b": "A dozen eggs cost 80rs.",
        r"\b(10|rice)\b": "Rice is 50rs per kg.",
        r"\b(11|vegetables|veggies)\b": "We have fresh vegetables available. What are you looking for?",
        r"\b(12|fruits)\b": "We have apples, bananas, and oranges in stock. Which one do you need?",
        r"\b(13|snacks)\b": "We have chips, biscuits, and chocolates available.",
        r"\b(14|beverages|drinks)\b": "We have soft drinks, juices, and bottled water. What would you like?",
        r"\b(15|buy|order)\b": "You can place an order on our website or visit our store.",
        r"\b(16|payment methods)\b": "We accept cash, credit/debit cards, and UPI payments.",
        r"\b(17|store hours|timing)\b": "Our store is open from 8 AM to 10 PM every day.",
        r"\b(18|location|address)\b": "We are located at XYZ Market, Main Street, City.",
        r"\b(19|bye|exit)\b": "Goodbye! Happy shopping! 🛍"
    }

    # Iterate over the dictionary to find a matching pattern in the user's input
    for pattern, response in responses.items():
        # If a pattern matches, return the associated response
        if re.search(pattern, user_input):
            return response
   
    # If no patterns match, return a default fallback message
    return "I am sorry, I didn't understand that. Can you rephrase or ask about a specific grocery item?"

# Display welcome message when chatbot starts
print("Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.")

# Start an infinite loop to simulate ongoing chat
while True:
    # Take user input from the console
    user_message = input("You: ")
    
    # If the user types 'bye' or 'exit', end the chat
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Happy shopping! 🛍")
        break  # Exit the loop and stop the chatbot
    
    # Call the response function and print the chatbot's reply
    response = chatbot_response(user_message)
    print("Chatbot:", response)
