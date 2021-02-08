import rpack

sizes = [(20, 20), (40, 40), (20, 60), (20, 50), (40, 40), (20, 20), (20, 10), (40, 10), (40, 10)]

positions = rpack.pack(sizes)

file = open("positions.txt", "w")
for i in positions:
    file.write(str(i))
file.close()

file_reader = open("positions.txt", "r")
print(file_reader.read())
