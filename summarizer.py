import re

def read_chat_file(file_path):
    with open(file_path, 'r') as chat_file:
        return chat_file.readlines()

def split_messages(chat_lines):
    user_lines = []
    ai_lines = []

    for line in chat_lines:
        line = line.strip()
        match = re.match(r"^(user|ai)\s*:\s*(.+)", line, re.IGNORECASE)

        if match:
            sender = match.group(1).lower()
            message_text = match.group(2).strip()

            if sender == 'user':
                user_lines.append(message_text)
            elif sender == 'ai':
                ai_lines.append(message_text)

    return user_lines, ai_lines


if __name__ == "__main__":
    chat_file_path = "sample_chat.txt"
    chat_lines = read_chat_file(chat_file_path)

    user_messages, ai_messages = split_messages(chat_lines)

    print("Messages from User:")
    for text in user_messages:
        print("-", text)

    print("\nMessages from AI:")
    for text in ai_messages:
        print("-", text)
