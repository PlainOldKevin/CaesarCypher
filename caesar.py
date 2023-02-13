# Import logo and print for start of game
from art import logo
print(logo)

# Alphabet for iterating through
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to calculate new message
def caesar(txt, shft, dir):
    # Empty string for end result
    end_text = ""
    # Check if user wants to decode
    # The shift amount will change based on this information
    if dir == "decode":
        # Instead of going forward a certain amount (say 5), go backwards (-5)
        shft *= -1
    # Loop thru original word
    for char in txt:
        # Ignore numbers/letters/symbols
        if char not in alphabet:
            end_text += char
        # Insert new letter into word
        else:
            # Find position of given letter (a=0, b=1, ...)
            position = alphabet.index(char)
            # Find position of letter after shifting (ex. shift=5, then 'a' becomes 'f')
            new_position = position + shft
            # Add letter to the end of the new string created before the for loop
            end_text += alphabet[new_position]

    # Print result
    print(f"Here's the {dir}d result: {end_text}\n")


# Variable for end of game condition
end = 'yes'

while end == 'yes':
    # Prompt the user for data entry
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # If the shift number is greater than 26 it will cause an IndexOutOfRange
    # The '%26' makes the dunction work the same way (encoding or decoding )
    if shift > 26:
        shift %= 26

    # Calculate new string
    caesar(txt=text, shft=shift, dir=direction)
    end = input("Would you like to restart the program? Type 'yes' to continue.\n")
