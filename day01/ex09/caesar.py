import sys 

def caesar_cipher(word, num):
    result = []
    for ch in word:
        if ch.islower():
            result.append(chr((ord(ch) - 97 + num) % 26 + 97))
        elif ch.isupper():
            result.append(chr((ord(ch) - 65 + num) % 26 + 65))
        else:
            result.append(ch)
    return ''.join(result)

def main(action, input_string, shift):
    if action.lower() == 'encode':
        encoded_string = caesar_cipher(input_string, shift)
        print(encoded_string)
    elif action.lower() == 'decode':
        decoded_string = caesar_cipher(input_string, -shift)
        print(decoded_string)
    else:
        raise Exception("Use 'encode' or 'decode' only.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Usage: python3 caesar.py <mode> <string> <shift>")
    action = sys.argv[1]
    input_string = sys.argv[2]
    if any([char in "йфячыцувсмакепитрнгоьблшщдюжзхэъё" for char in input_string]):
        raise Exception("The script does not support your language yet.")
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Error. Usage INT(like: 5)")

    main(action, input_string, shift)