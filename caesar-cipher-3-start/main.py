alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(direction, text, shift):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if(direction == "encode"):
      newPosition = position + shift
    else:
      newPosition = position - shift
    cipher_text += alphabet[newPosition]
  print(cipher_text)

caesar(direction=direction,text=text, shift=shift)
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.