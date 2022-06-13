# https://docs.google.com/spreadsheets/d/1TZh4jWrx4h9zzpYUI9aYXMl1fYOiqu-xVuOOMqagxrs/edit#gid=0

raw_inputs = [
["Send 17C",                   "10100100 10000010 01001101 01111111 00010010"],
["Send 18C",                   "10100100 10000010 01001101 01111111 00010011"],
["Send 19C",                   "10100100 10000010 01001101 01111111 00010100"],
["Send 20C",                   "10100100 10000010 01001101 01111111 00010101"],
["Send 21C",                   "10100100 10000010 01001101 01111111 00010110"],
["Send 22C",                   "10100100 10000010 01001101 01111111 00010111"],
["Send 23C",                   "10100100 10000010 01001101 01111111 00011000"],
["Send 24C",                   "10100100 10000010 01001101 01111111 00011001"],
["Send 25C",                   "10100100 10000010 01001101 01111111 00011010"],
["Send 26C",                   "10100100 10000010 01001101 01111111 00011011"],
["Send 27C",                   "10100100 10000010 01001101 01111111 00011100"],
["Send 28C",                   "10100100 10000010 01001101 01111111 00011101"],
["Send 29C",                   "10100100 10000010 01001101 01111111 00011110"],
["Send 30C",                   "10100100 10000010 01001101 01111111 00011111"],

["Mode Auto - Fan Auto - 17C", "10100001 10000010 01000000 11111111 11111111"],
["Mode Auto - Fan Auto - 18C", "10100001 10000010 01000001 11111111 11111111"],
["Mode Auto - Fan Auto - 19C", "10100001 10000010 01000010 11111111 11111111"],
["Mode Auto - Fan Auto - 20C", "10100001 10000010 01000011 11111111 11111111"],
["Mode Auto - Fan Auto - 21C", "10100001 10000010 01000100 11111111 11111111"],
["Mode Auto - Fan Auto - 22C", "10100001 10000010 01000101 11111111 11111111"],
["Mode Auto - Fan Auto - 23C", "10100001 10000010 01000110 11111111 11111111"],
["Mode Auto - Fan Auto - 24C", "10100001 10000010 01000111 11111111 11111111"],
["Mode Auto - Fan Auto - 25C", "10100001 10000010 01001000 11111111 11111111"],
["Mode Auto - Fan Auto - 26C", "10100001 10000010 01001001 11111111 11111111"],
["Mode Auto - Fan Auto - 27C", "10100001 10000010 01001010 11111111 11111111"],
["Mode Auto - Fan Auto - 28C", "10100001 10000010 01001011 11111111 11111111"],
["Mode Auto - Fan Auto - 29C", "10100001 10000010 01001100 11111111 11111111"],
["Mode Auto - Fan Auto - 30C", "10100001 10000010 01001101 11111111 11111111"],

["Mode Cool - Fan Auto - 17C", "10100001 10000000 01000000 11111111 11111111"],
["Mode Cool - Fan Auto - 18C", "10100001 10000000 01000001 11111111 11111111"],
["Mode Cool - Fan Auto - 19C", "10100001 10000000 01000010 11111111 11111111"],
["Mode Cool - Fan Auto - 20C", "10100001 10000000 01000011 11111111 11111111"],
["Mode Cool - Fan Auto - 21C", "10100001 10000000 01000100 11111111 11111111"],
["Mode Cool - Fan Auto - 22C", "10100001 10000000 01000101 11111111 11111111"],
["Mode Cool - Fan Auto - 23C", "10100001 10000000 01000110 11111111 11111111"],
["Mode Cool - Fan Auto - 24C", "10100001 10000000 01000111 11111111 11111111"],
["Mode Cool - Fan Auto - 25C", "10100001 10000000 01001000 11111111 11111111"],
["Mode Cool - Fan Auto - 26C", "10100001 10000000 01001001 11111111 11111111"],
["Mode Cool - Fan Auto - 27C", "10100001 10000000 01001010 11111111 11111111"],
["Mode Cool - Fan Auto - 28C", "10100001 10000000 01001011 11111111 11111111"],
["Mode Cool - Fan Auto - 29C", "10100001 10000000 01001100 11111111 11111111"],
["Mode Cool - Fan Auto - 30C", "10100001 10000000 01001101 11111111 11111111"],

["Mode Cool - Fan Low - 17C",  "10100001 10001000 01000000 11111111 11111111"],
["Mode Cool - Fan Low - 18C",  "10100001 10001000 01000001 11111111 11111111"],
["Mode Cool - Fan Low - 19C",  "10100001 10001000 01000010 11111111 11111111"],
["Mode Cool - Fan Low - 20C",  "10100001 10001000 01000011 11111111 11111111"],
["Mode Cool - Fan Low - 21C",  "10100001 10001000 01000100 11111111 11111111"],
["Mode Cool - Fan Low - 22C",  "10100001 10001000 01000101 11111111 11111111"],
["Mode Cool - Fan Low - 23C",  "10100001 10001000 01000110 11111111 11111111"],
["Mode Cool - Fan Low - 24C",  "10100001 10001000 01000111 11111111 11111111"],
["Mode Cool - Fan Low - 25C",  "10100001 10001000 01001000 11111111 11111111"],
["Mode Cool - Fan Low - 26C",  "10100001 10001000 01001001 11111111 11111111"],
["Mode Cool - Fan Low - 27C",  "10100001 10001000 01001010 11111111 11111111"],
["Mode Cool - Fan Low - 28C",  "10100001 10001000 01001011 11111111 11111111"],
["Mode Cool - Fan Low - 29C",  "10100001 10001000 01001100 11111111 11111111"],
["Mode Cool - Fan Low - 30C",  "10100001 10001000 01001101 11111111 11111111"],

["Mode Cool - Fan High - 17C", "10100001 10011000 01000000 11111111 11111111"],
["Mode Cool - Fan High - 18C", "10100001 10011000 01000001 11111111 11111111"],
["Mode Cool - Fan High - 19C", "10100001 10011000 01000010 11111111 11111111"],
["Mode Cool - Fan High - 20C", "10100001 10011000 01000011 11111111 11111111"],
["Mode Cool - Fan High - 21C", "10100001 10011000 01000100 11111111 11111111"],
["Mode Cool - Fan High - 22C", "10100001 10011000 01000101 11111111 11111111"],
["Mode Cool - Fan High - 23C", "10100001 10011000 01000110 11111111 11111111"],
["Mode Cool - Fan High - 24C", "10100001 10011000 01000111 11111111 11111111"],
["Mode Cool - Fan High - 25C", "10100001 10011000 01001000 11111111 11111111"],
["Mode Cool - Fan High - 26C", "10100001 10011000 01001001 11111111 11111111"],
["Mode Cool - Fan High - 27C", "10100001 10011000 01001010 11111111 11111111"],
["Mode Cool - Fan High - 28C", "10100001 10011000 01001011 11111111 11111111"],
["Mode Cool - Fan High - 29C", "10100001 10011000 01001100 11111111 11111111"],
["Mode Cool - Fan High - 30C", "10100001 10011000 01001101 11111111 11111111"],

["Mode Dry",                   "10100001 10000001 01001000 11111111 11111111"],

["Mode Fan - Fan Auto",        "10100001 10100100 01011110 11111111 11111111"],
["Mode Fan - Fan Low",         "10100001 10001100 01011110 11111111 11111111"],
["Mode Fan - Fan High",        "10100001 10011100 01011110 11111111 11111111"],

["Turn off",                   "10100001 00001100 01011110 11111111 11111111"]
]

commands = []

for input in raw_inputs:

    b0, b1, b2, b3, b4 = input[1].split()

    r0 = b4[::-1]
    r1 = b3[::-1]
    r2 = b2[::-1]
    r3 = b1[::-1]
    r4 = b0[::-1]

    reverse_sum = int(r0, 2) + int(r1, 2) + int(r2, 2) + int(r3, 2) + int(r4, 2)

    sum_subtract = 256 - reverse_sum

    modulo = sum_subtract % 256

    checksum = '{0:08b}'.format(modulo)[::-1]

    commands.append([input[0], input[1] + " " + checksum])



preamble = "Freq=38000Hz[+4525,-4525,"
middle = "+500,-4525,+4525,-4525,"
end = "-101502][][]"

start = "+500,"
data_zero = "-500,"
data_one = "-1600,"

for row in commands:
    command = row[0]
    binary_string = row[1].replace(" ", "")
    binary = int(binary_string, 2)
    hex_string = str(hex(binary))[2::].upper()

    reverse_string = ""
    for character in binary_string:
        if character == "0":
            reverse_string = reverse_string + "1"
        else:
            reverse_string = reverse_string + "0"

    reverse = int(reverse_string, 2)
    reverse_hex_string = str(hex(reverse))[2::].upper()

    irp_notation = preamble

    for bit in binary_string:
        if bit == "0":
            irp_notation = irp_notation + start + data_zero
        else:
            irp_notation = irp_notation + start + data_one


    irp_notation = irp_notation + middle

    for bit in reverse_string:
        if bit == "0":
            irp_notation = irp_notation + start + data_zero
        else:
            irp_notation = irp_notation + start + data_one
    
    irp_notation = irp_notation + start + end

    print(command + ":")
    print(binary_string + " - " + hex_string)
    print(reverse_string + " - " + reverse_hex_string)
    print(irp_notation)
    print("")