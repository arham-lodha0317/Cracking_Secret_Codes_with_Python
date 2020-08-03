# Ceaser Cipher

# Way 1 modular math
# Create a cycle

message = input("What is your message? \n")
key = int(input("What is your key? \n"))

operation = input(
    "What would you like to do?\nFor encrypting data please enter E, else for decrypting data enter D.\n")

while operation is not "E" and operation is not "D":
    operation = input("Please enter a valid input: \n")




result = ""

for character in message:
    #
    # asciiValue = ord(character)
    #
    # startingAscii = 32
    # endingAscii = 126
    #
    # # 32 is the starting ascii value so we start at 0
    # asciiValue -= startingAscii

    if operation == "E":
        # add by the key
        result += chr((ord(character) - 32 + key) % 94 + 32)

    else:
        result += chr((ord(character) - 32 - key) % 94 + 32)
    #
    # # Maximum ascii value we will use is 126 so we do 126 - 32 = 94. We have created a cycle
    # asciiValue %= (endingAscii - startingAscii)
    #
    # result += chr(asciiValue + startingAscii)
    #
    # # One liner

print(result)
