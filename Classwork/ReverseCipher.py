#Reverse Cipher
#This cipher reverse a string.


# message = input("What is your message?\n")
message = "Arham Lodha"
translated = ""

#Way 1:
for i in message:
    translated = i + translated
    print(translated)



# #Way 2:
# translated = ""
# index = len(message) - 1
#
# while index >= 0:
#     translated = translated + message[index]
#     index -= 1
#
# print(translated)

