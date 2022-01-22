# Task No. 1: (Files, exceptions, with)
#
# Open a file called "file.txt" (if not existed create a new one and fill it with random numbers)
# save its content in a new file "file1.bin" (binary Bing endian) and in a second file "file2.bin" (in Little endian)
# display "file1.bin" content in the terminal (in the correct way and in the opposite way).

a = 5
b = 13
try:
    with open("file1.bin", "wb") as file:
        file.write(a.to_bytes(4, "big"))
        file.write(b.to_bytes(4, "big"))
except:
    print("Cant open file")

try:
    with open("file2.bin", "wb") as file:
        file.write(a.to_bytes(4, "little"))
        file.write(b.to_bytes(4, "little"))
except:
    print("Cant open file")

try:
    with open("file1.bin", "rb") as file:
        print("file1.bit content: ", file.read())
        file.seek(0, 0)
        a = int.from_bytes(file.read(4), "little")
        b = int.from_bytes(file.read(4), "little")
        print("file1.bit content in little endian: ", a, b)
        file.seek(0, 0)
        a = int.from_bytes(file.read(4), "big")
        b = int.from_bytes(file.read(4), "big")
        print("file1.bit content in big endian: ", a, b)
except:
    print("Cant open file")

try:
    with open("file2.bin", "rb") as file:
        print("file2.bit content: ", file.read())
        file.seek(0, 0)
        a = int.from_bytes(file.read(4), "little")
        b = int.from_bytes(file.read(4), "little")
        print("file2.bit content: ", a, b)
except:
    print("Cant open file")
