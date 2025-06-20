import socket

def main():
    ip = input("ENTER IP: ")
    checkclass = ip.split('.')[0]

    cc = int(checkclass)
    mask = None
    if cc > 0:
        if cc <= 127:
            mask = "255.0.0.0"
            print("Class A IP Address")
            print("SUBNET MASK:\n" + mask)
        elif 128 <= cc <= 191:
            mask = "255.255.0.0"
            print("Class B IP Address")
            print("SUBNET MASK:\n" + mask)
        elif 192 <= cc <= 223:
            mask = "255.255.255.0"
            print("Class C IP Address")
            print("SUBNET MASK:\n" + mask)
        elif 224 <= cc <= 239:
            mask = "255.0.0.0"
            print("Class D IP Address Used for multicasting")
        elif 240 <= cc <= 254:
            mask = "255.0.0.0"
            print("Class E IP Address Experimental Use")

    networkAddr = ""
    lastAddr = ""
    ipAddrParts = ip.split(".")
    maskParts = mask.split(".")

    for i in range(4):
        x = int(ipAddrParts[i])
        y = int(maskParts[i])
        z = x & y
        networkAddr += str(z) + "."
        w = z | (y ^ 255)
        lastAddr += str(w) + "."

    print("First IP of block: " + networkAddr)
    print("Last IP of block: " + lastAddr)

if __name__ == "__main__":
    main()

