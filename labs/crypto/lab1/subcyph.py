alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encoder(key):    
    message = input("Message to encode: ")
    code = []
    for i in message:
        if i.strip() and i in alphabet:
            code.append(alphabet[(alphabet.index(i) + key) %26])
        else:
            code.append(i)
    
    output = ''.join(code)
    return output

def decode(key):    
    message = input("Message to decode: ")
    code = []
    for i in message:
        if i.strip() and i in alphabet:
            code.append(alphabet[(alphabet.index(i) - key) %26])
        else:
            code.append(i)
    
    output = ''.join(code)
    return output

def main():
    key = 0
    key = int(input("Key(int 1-26): "))

    print(encoder(key))
    print(decode(key))

main()