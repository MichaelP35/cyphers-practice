# List of ciphers
class Ciphers:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    

    # Caesar Cipher
    def caesar(self, text: str, shift:int):
        new_text = ''

        # Go through each character in text
        for char in text:
            # Append any non-letter character to the message
            if not char.isalpha():
                new_text += char
            elif char.isupper():
                char = char.lower()
                index = self.alphabet.find(char)
                new_index = (index + shift) % len(self.alphabet)
                new_text += self.alphabet[new_index].upper()
            # If lower case letter, shift letter by inputted offset
            else:
                index = self.alphabet.find(char)
                new_index = (index + shift) % len(self.alphabet)
                new_text += self.alphabet[new_index]
                
        
        return new_text
    

    # Vigenere Cipher
    def vigenere(self, text: str, key:str, direction: int=1):
        key_index = 0
        new_text = ''

        for char in text:
            if not char.isalpha():
                new_text += char
            elif char.isupper():
                char = char.lower()
                key_char = key[key_index % len(key)]
                key_index +=1
                offset = self.alphabet.index(key_char)
                index = self.alphabet.find(char)
                new_index = ((index + offset*direction) % len(self.alphabet))
                new_text += self.alphabet[new_index].upper()
            else:
                key_char = key[key_index % len(key)]
                key_index +=1
                offset = self.alphabet.index(key_char)
                index = self.alphabet.find(char)
                new_index = ((index + offset*direction) % len(self.alphabet))
                new_text += self.alphabet[new_index]
        
        return new_text