# List of ciphers
class Ciphers:
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Caesar Cipher
    def caesar(self, text: str, offset:int):
        new_text = ''

        # Make text all lowercase. Temporary workaround.
        for char in text.lower():
            # Append any non-letter character to the message.
            if not char.isalpha():
                new_text += char
            # If letter, shift letter by inputted offset.
            else:
                index = self.alphabet.find(char)
                new_index = (index + offset) % len(self.alphabet)
                new_text += self.alphabet[new_index]
        
        return new_text