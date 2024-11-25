# XOR operation for binary strings


def xor(a, b):
    # Perform XOR between two binary strings of the same length.
    return ["1" if i != j else "0" for i, j in zip(a, b)]


# Perform binary division
def division(divisor, dividend):

    n = len(divisor)  # Length of divisor
    current_target = dividend[0:n]  # Take the first n bits of dividend
    quotient = []

    for i in range(n, len(dividend) + 1):
        # Perform division if the leading bit is 1
        if current_target[0] == "1":
            quotient.append("1")
            current_target = xor(current_target, divisor)
        else:
            quotient.append("0")
            current_target = xor(current_target, ["0"] * n)

        # Drop the first bit and append the next bit from the dividend
        if i < len(dividend):
            current_target.append(dividend[i])

        # Ensure current_target maintains correct size
        current_target = current_target[1:]
    # FOR LOOP END

    # The remainder is the final value of current_target after division
    remainder = current_target
    return quotient, remainder


# Encode the message
def encode_message(data, divisor):

    n = len(divisor) - 1  # Number of zeros to append
    dividend = data + ["0"] * n  # Append n zeros to the data
    _, remainder = division(divisor, dividend)
    return data + remainder  # Add remainder to the original data


# Decode the message
def decode_message(received_data, divisor):

    _, remainder = division(divisor, received_data)
    if all(bit == "0" for bit in remainder):  # If remainder is all zeros
        print("You got the correct message 🥳!")
    else:
        print("Message has been manipulated 💀!")
        print(f"Remainder: {''.join(remainder)}")  # .join()  TO CONVERT LIST INTO STRING.


# Main CRC function
def crc():

    data = list(input("Enter data (binary string): ").strip())  # strip() funct. REMOVES WHITESPACES
    divisor = list(input("Enter divisor (binary string): ").lstrip("0"))  # lstrip('0')  REMOVES STARTING 0's

    # Encode the message
    transmitted_message = encode_message(data, divisor)
    print(f"Transmitted Message: {''.join(transmitted_message)}")

    # Decode the received message
    received_message = list(input("Enter the received message (binary string): ").strip())
    decode_message(received_message, divisor)


# Run the CRC function
crc()
