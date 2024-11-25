
def byte_stuffing(data, flag, escape):
    """
    Perform byte stuffing on the input data.

    :param data: The input string to be stuffed.
    :param flag: The flag byte.
    :param escape: The escape character.
    :return: Stuffed data as a string.
    """
    stuffed_data = flag  # Start with the flag byte
    for char in data:
        if char == flag or char == escape:  # Check if character is flag or escape
            stuffed_data += escape  # Add escape character before the reserved character
        stuffed_data += char
    stuffed_data += flag  # End with the flag byte
    return stuffed_data




# Taking user inputs for flags and escape character
start_flag = input("Enter the start and end flag character : ")
escape_char = input("Enter the escape character : ")

# Example data input
data = input("Enter the data to be transmitted: ")
print("\nOriginal Data:", data)

# Perform byte stuffing
stuffed = byte_stuffing(data, start_flag, escape_char)
print("Stuffed Data:", stuffed)

