import emoji
print ("Hello, I am EmojiSpeak")
name = input("Enter your name: ")
print("Nice to meet you " + name)
print("Let's play a game! I will give you a certain amount of emojis and your job is to guess what I mean")
print("Only two rules: respond in lowercase letters and have fun!")
print ("Final thing before we start, whenever your done playing, just type 'quit'")
i=0
while i<=4:
    inp1 = input("Say something:\n")
    print(inp1 + " doesn't make sense")
    i=i+1
    if inp1 == "quit":
        break

print ("Thank you for playing")