def binary_to_octal(binary):
    return "".join(oct(binary)[2:])

def octal_to_binary(octal):
    return bin(octal).replace("0b", "")


if __name__ == "__main__":
    octal = int(input(), 8)
    ans = octal_to_binary(octal)
    print(ans)
    