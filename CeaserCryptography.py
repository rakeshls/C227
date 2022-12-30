print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    msg = input("Enter your message-") 
    key = int(input("Enter your key-(1-94)"))
    etext=""
    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if temp>126:
            temp=temp-127+32
        etext+=chr(temp)
    print("Encryptted:- "+etext)

def decryption():
    print("Decryption")
    encryptmsg = input("Enter the encrypted text")
    decryptedKey = int(input("Enter the key-(1-94)")) 
    decryptedtext=""
    for i in range(len(encryptmsg)):
        temp=(ord(encryptmsg[i])-decryptedKey)
        if temp>126:
            temp=temp-127+32
        decryptedtext+=chr(temp)
    print("Decryptted:- "+decryptedtext)
        
if __name__ == "__main__":
    main()