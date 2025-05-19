import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

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


#  Count and show message statistics
def print_message_stats(user_msgs, ai_msgs):
    total = len(user_msgs) + len(ai_msgs)
    print("\n--- Message Statistics ---")
    print(f"Total messages: {total}")
    print(f"User messages: {len(user_msgs)}")
    print(f"AI messages: {len(ai_msgs)}")
    
# keywords extraction
def extract_keywords(user_msgs, ai_msgs, top_n=5):
    all_text = " ".join(user_msgs + ai_msgs).lower()
    
    # Remove punctuation
    all_text = all_text.translate(str.maketrans("", "", string.punctuation))
    
    # Tokenize the text
    tokens = word_tokenize(all_text)
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    keywords = [word for word in tokens if word not in stop_words and word.isalpha()]
    
    # Count most common words
    keyword_counts = Counter(keywords)
    top_keywords = keyword_counts.most_common(top_n)

    print("\n--- Top Keywords ---")
    for word, freq in top_keywords:
        print(f"{word}: {freq}")
        
    return top_keywords


# summary generation
def generate_summary(user_msgs, ai_msgs, top_keywords):
    total_exchanges = len(user_msgs) + len(ai_msgs)
    keywords_only = [word for word, _ in top_keywords]

    print("\n================= Summary =================")
    print(f"- The conversation had {total_exchanges} exchanges.")

    if keywords_only:
        topic_guess = " and ".join(keywords_only[:2])
        print(f"- The user asked mainly about {topic_guess}.")
    else:
        print("- Could not determine the conversation topic.")

    print(f"- Most common keywords: {', '.join(keywords_only)}")
    print("==========================================")
        
def process_chat_folder(folder_path):
    # Get all .txt files from the folder
    chat_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    # Process each chat file
    for chat_file in chat_files:
        print(f"\nProcessing {chat_file}...")
        chat_path = os.path.join(folder_path, chat_file)
        
        # Use your existing functions to process the file
        chat_lines = read_chat_file(chat_path)
        user_messages, ai_messages = split_messages(chat_lines)
        
        # Print results for this file
        print(f"\n=== Summary for {chat_file} ===")
       

        print("Messages from User:")
        for text in user_messages:
            print("-", text)

        print("\nMessages from AI:")
        for text in ai_messages:
            print("-", text)

        print_message_stats(user_messages, ai_messages)
        top_keywords = extract_keywords(user_messages, ai_messages)
        generate_summary(user_messages, ai_messages, top_keywords)

#if __name__ == "__main__":
#    chat_file_path = "sample_chat.txt"
#    chat_lines = read_chat_file(chat_file_path)

if __name__ == "__main__":  
    chat_folder = "chat_logs"  # folder containing your chat logs
    process_chat_folder(chat_folder)