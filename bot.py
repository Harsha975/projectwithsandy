def chat_box():
  while True:
    user_input = input("User: ")
    if user_input == "exit":
      break
    response = get_response(user_input)
    print("Bot:", response)

def get_response(prompt):
    if "hii" in prompt.lower():
        return "Hello there! how are you??.."
    elif (prompt.lower()=="fine you"or prompt.lower()=="good" or prompt.lower()=="fine") :
        return "Doing great ! how was your day ?"
    elif "great" in prompt.lower():
        return "is there anything that i can do to you!!..(tell a joke/relationship tips  ??)"
    elif "tell a joke" in prompt.lower():
        return "dads joke -- > !(u r 2 6 c) "
    elif "hello" in prompt.lower():
        return "Hello there!"
    elif "how are you" in prompt.lower():
        return "I'm doing well, thank you for asking."
    else:
        return "I'm sorry, I don't understand what you're saying."

chat_box()
#hola
