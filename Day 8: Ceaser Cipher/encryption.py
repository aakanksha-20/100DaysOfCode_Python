
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (plain_text, shift_amt):
    cipher = ""
    #shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amt
        new_letter = alphabet[new_position]
        cipher += new_letter
    print(f"The encoded text is {cipher}")

encrypt(plain_text=text, shift_amt=shift)