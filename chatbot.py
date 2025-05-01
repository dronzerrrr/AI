def chatbot():
    print("Bot: Hello! Welcome to our store. How can I help you today?")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Bot: Hello! How can I assist you?")
        elif "payment" in user_input:
            print("Bot: We accept credit cards, debit cards, and UPI payments.")
        elif "delivery" in user_input or "shipping" in user_input:
            print("Bot: Delivery takes 3-5 business days.")
        elif "return" in user_input:
            print("Bot: You can return products within 10 days of delivery.")
        elif "contact" in user_input or "customer care" in user_input:
            print("Bot: You can reach us at support@example.com or call 1800-123-456.")
        elif user_input == "exit":
            print("Bot: Thank you for chatting! Have a great day 😊")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
chatbot()
