# Put your commands here
COMMAND1 = "who is mr_techie"
COMMAND2 = "talk in binary"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I cannot reveal his identity."
    if command.find(COMMAND2) >= 0:
        response = "10010010 01010101 01010000 11111101 01010110 01010111 01011110 10101010 10101001\n00010111 11110101 01010010!!!"

    return response
