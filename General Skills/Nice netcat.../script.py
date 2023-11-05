
with open('output.txt') as f:
    for line in f:
        print(chr(int(line.strip())),end='')