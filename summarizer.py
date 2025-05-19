# summarizer.py

def read_chat_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

if __name__ == "__main__":
    lines = read_chat_file("sample_chat.txt")
    for line in lines:
        print(line.strip())
