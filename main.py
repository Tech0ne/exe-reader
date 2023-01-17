#!/usr/bin/python3

from sys import argv

def usage():
    print("USAGE :")
    print(f"\t{argv[0]} [exe file path]")
    print()
    print("\tRead the content of the exe file and display the infos (and theyr meaning)")

def rd(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
        return data
    except:
        return False

def read_2_oct_value(content, i):
    size = int(content[i])
    if int(content[i + 1]):
        size = int(str(int(content[i + 1])) + str(int(content[i])))
    return size

def to_hexa(i):
    x =  hex(i)[2:]
    while len(x) < 4:
        x = '0' + x
    return x

def run_decoder(filename, content):
    try:
        print(f"Filename                                          : {filename}")
        print(f"Is signature valid ?                              : {bool(chr(content[0]) == 'M' and chr(content[1]) == 'Z')}")
        print(f"Signature                                         : {content[0:2].decode()}")
        phrases = [
            "Size of last page                                 :",
            "Number of 512 bytes pages in file                 :",
            "Number of relocation entries                      :",
            "Header size in paragraphs                         :",
            "Minimum additional memory required in paragraphs  :",
            "Maximum additional memory required in paragraphs  :",
            "Initial SS relative to start of file              :",
            "Initial SP                                        :",
            "Checksum (unused)                                 :",
            "Initial IP                                        :",
            "Initial CS relative to start of file              :",
            "Offset within Header of Relocation Table          :",
            "Overlay Number                                    :"
        ]

        index = 2
        for e in phrases:
            size = read_2_oct_value(content, index)
            print(f"{e} {size}{' ' * (8 - len(str(size)))}({to_hexa(size)})")
            index += 2
    except Exception as e:
        print(f"An exception occured : {e}")

if len(argv) == 1:
    usage()
elif argv[1] in ("-h", "--help"):
    usage()
else:
    content = rd(argv[1])
    if content is False:
        usage()
    else:
        run_decoder(argv[1], content)
