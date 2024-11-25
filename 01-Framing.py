#    FUNCTIONS OF ALL METHODS


def character_count():

    frame = int(input("Enter no. of frames:"))
    transmitted_message = ""  # initialize a string variable

    for i in range(0, frame):
        data = input(f"Enter string {i+1}:")  # f"" to incvlude variable output
        char_count = (
            str(len(data)) + ":" + data
        )  # str(len) to convert length into string to concatinate
        transmitted_message += char_count

    return transmitted_message


def byteStuffing():
    startflag = input("enter a start character")
    endflag = input("enter a end character")
    escape = input("enter a escape character")
    msg = input("eneterr the msg to be transmitted: ")
    stuffedmsg = ""
    for i in range(0, len(msg)):
        if msg[i] == startflag or msg[i] == endflag or msg[i] == escape:
            stuffedmsg = stuffedmsg + escape + msg[i]
        else:
            stuffedmsg = stuffedmsg + msg[i]

    return startflag + stuffedmsg + endflag


def bitStuffing():
    data = list(input("enter the data in 0's & 1's: "))
    counter = 0
    i = 0
    while i < len(data):
        if data[i] == "1":
            counter += 1
        else:
            counter = 0         # Reset the counter if the current bit is not '1'

        if counter == 6:            # If six consecutive '1's are found
            data.insert(i, "0")         # Insert '0' before the 6th '1'
            counter = 0         # Reset the counter after stuffing
            # i=i+1         # Skip the inserted '0' to avoid infinite loop
        i += 1
    return "".join(data)            # Join the list to form a string


print("\nCHARACTER COUNT:")
transmitted_message_character_count = character_count()
print("transmitted message character count:" + transmitted_message_character_count)


print("\nBYTE STUFFING:")
transmitted_message_byte_stuffing = byteStuffing()
print("transmitted message byte stuffing:" + transmitted_message_byte_stuffing)


print("\nBIT STUFFING:")
transmitted_message_bit_stuffing = bitStuffing()
print("transmitted message bit stuffing:" + transmitted_message_bit_stuffing)










