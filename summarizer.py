def read_chat_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

# Step 2: Main execution
if __name__ == "__main__":
    lines = read_chat_file("sample_chat.txt")  
    for line in lines:
        print(line.strip())  