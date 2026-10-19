import random

# Converts ASCII into invisible Unicode where each 
# U+200C (Zero Width Non-Joiner aka ZWNJ) and U+200D (Zero Width Joiner aka ZWJ) are not displayed 
# Take user input, convert char to hex, convert hex to binary bits, map 0 to U+200C and 1 to U+200D
# returns encoded_value aka the invisible unicode
def encode_sentence(sentence):
    encoded_value = "" #will be the sentence encoded 
    
    for c in sentence.encode('utf-8'):
        hex_value = f'{c:02x}' 
         
        decimal_value = int(hex_value, 16)
        binary_value = format(decimal_value, '08b')
        
        for bit in binary_value:
            if bit == '0':
                encoded_value += '\u200c'
            else: #bit is 1
                encoded_value += '\u200d'

        encoded_value += '\u200c'
    return encoded_value  


# Tests invisible unicode characters within input text (potential use case: detecting 'hidden text' inputs)
# So above would do something like show ZQNJ/ZWJ only 
# encode_ascii_tags will have something like U+E0041
# the ascii range starts at 32 (space) to 126 (tilde)
# it's always going to be 0xE0000 with the hex ASCII value as the offset so for example A is U+E0041
def encode_ascii_tags(sentence):
    encoded_value = ""
    for c in sentence: 
        ascii_value = ord(c) 
        if ascii_value < 32 or ascii_value > 126:
            raise ValueError("String contains a non-printable ASCII value.")
        invisible_char = chr(0xE0000 + ascii_value)
        encoded_value += invisible_char 
    return encoded_value

# Generates amount of bytes (n) specified by user to encode
# Outer loop for n amount of bytes, inner loop to put random bits
# Attaches \u200c after each encoded byte as a separator (to represent Zero Width Non-Joiner,akin to spaces in laymans terms)
def generate_bytes(n):
    encoded_value = ""

    for i in range(n):
        for bit in range(8):         
            encoded_value += random.choice(['\u200c', '\u200d'])

        encoded_value += '\u200c'
   
    return encoded_value

