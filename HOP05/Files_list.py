filename = 'hello.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(lines.rstrip())

    