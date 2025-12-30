import emoji
import random 

    # Keywords to identify animal emojis in their shortcode names (e.g., ":dog:", ":cat_face:")
animal_keywords = [
        'face', 'animal', 'bird', 'fish', 'bug', 'plant', 'nature', # General categories for comprehensive filtering
        'dog', 'cat', 'lion', 'tiger', 'horse', 'zebra', 'cow', 'pig', 'goat',
        'sheep', 'monkey', 'chicken', 'penguin', 'bird', 'eagle', 'owl',
        'duck', 'snake', 'frog', 'crocodile', 'turtle', 'whale', 'dolphin',
        'shark', 'octopus', 'snail', 'butterfly', 'bug', 'ant', 'bee',
        'spider', 'scorpion', 'mosquito', 'fly', 'worm', 'shell', 'paw',
        'bear', 'koala', 'panda', 'sloth', 'otter', 'skunk', 'badger',
        'beaver', 'hedgehog', 'bat', 'owl', 'camel', 'llama', 'giraffe',
        'elephant', 'rhino', 'hippo', 'kangaroo', 'deer', 'fox', 'racoon',
        'mouse', 'rat', 'hamster', 'rabbit', 'chipmunk'
    ]

print ("Hello, I am EmojiSpeak")
name = input("Enter your name: ")
print("Nice to meet you " + name)
print("Let's play a game! I will give you a emoji and your job is to guess what it is. There will be 5 rounds")
print("Only two rules: respond in lowercase letters and have fun!")
print ("Final thing before we start, if your done playing before all rounds are over, just type 'quit'")
i=1
score=0
while i<=5:
    #emoji1 = "rocket"
    print ("Round " + str(i))
    # get random emoji from animal_keywords
    emoji1 = random.choice(animal_keywords)
    question = emoji.emojize("Guess this:\n :"+emoji1+":")
    print(question)
    inp1 = input("What do you this is?\n")
    #print(inp1 + " doesn't make sense")
    if inp1 == emoji1:
        score = score + 10
        print ("You are correct! Your score is " + str(score))
    else:
        print ("Sorry! Incorrect")
    if inp1 == "quit":
        print ("thank you for playing!")
        break
    #increment counter
    i=i+1

print ("Game Over! Congrats on getting the score of " + str(score))