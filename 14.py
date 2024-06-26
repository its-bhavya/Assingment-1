''''program that reads multiple lines of input from the user until they
enter an empty line, then prints all the lines.'''
message = []
print("Enter your message below: ")
while True:
    line = input()
    if line == '':
        break
    message.append(line)
                   
for line in message:
    print(line)