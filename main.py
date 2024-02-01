import string


# List of ciphers
class Ciphers:
    

    # Create a dictionary that is shifted accordingly
    def dictShiftCreator(self, shift):
        alphabet = string.ascii_lowercase + string.ascii_uppercase

        shifted_lower = string.ascii_lowercase[shift:] + string.ascii_lowercase[0:shift]
        shifted_upper = string.ascii_uppercase[shift:] + string.ascii_uppercase[0:shift]

        shifted_alphabet = shifted_lower + shifted_upper

        return {key: value for key, value in zip(alphabet, shifted_alphabet)}


    def caesar(self, message: str, shift: int):
        # Create the shifted dictionary on start based on shift amount
        shifted_dict = self.dictShiftCreator(shift)
        new_message = ''

        for char in message:
            if not char.isalpha():
                # If the character isn't a letter, add it as is
                new_message += char
            else:
                # Output new letter from shifted dictionary
                new_message += shifted_dict[char]

        return new_message
    

    # Vigenere Cipher
    def vigenere(self, message: str, keyword: str):
        keyword_index = 0
        new_message = ''

        for char in message:
            if not char.isalpha():
                # If the character isn't a letter, add it as is
                new_message += char
            else:
                # Determine the shift for this letter based on the keyword
                shift = string.ascii_lowercase.index(keyword[keyword_index].lower())

                # Create the shifted dictionary based on current shift
                shifted_dict = self.dictShiftCreator(shift)

                # Output new letter from shifted dictionary
                new_message += shifted_dict[char]

                # Move to the next letter in the keyword
                keyword_index = (keyword_index + 1) % len(keyword)

        return new_message