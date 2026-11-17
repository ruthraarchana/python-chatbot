print("Bot: hello, I am bot?")

while True:
    you = input("You: ").lower().strip()

    if "how are you" in you:
        print("Bot: fine, what's up")
    elif "bye" in you or "byee" in you:
        print("Bot: byee! take care da!")
        break
    elif "hi" in you or "hello" in you:
        print("Bot: hello da! how are you?")
    else:
        print("Bot: puriyala da, 'hello, how are you?' nu kelu paakalam")
