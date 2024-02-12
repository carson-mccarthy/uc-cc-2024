from collections import Counter
import re
import socket
import os

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            word_count = len(contents.split())
        return word_count
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None

def get_top_3(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read().lower()
            words = re.findall(r'\b\w+\b', contents)
            top3 = Counter(words).most_common(3)
        return top3
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None

def get_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error as err:
        print(f"Unable to get IP Address: {err}")

def write_to_file(filename, files, wordcount, top3, ip):
    try:
        with open(filename, 'w') as file:
            file.write(f"The files in /home/data are {files}\n")
            file.write(f"There are {wordcount} total words in the two files\n")
            file.write(f"The top three words in IF.txt were {top3}\n")
            file.write(f"The IP of this machine is {ip}\n")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None
    
def print_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    pwd = os.getcwd()
    datpath = pwd+"/data"
    files = os.listdir(datpath)
    wc1 = count_words("/home/data/IF.txt")
    wc2 = count_words("/home/data/Limerick-1.txt")
    top3 = get_top_3("/home/data/Limerick-1.txt")
    ip = get_ip()
    os.makedirs("/home/output")
    write_to_file("/home/output/result.txt", files, wc1+wc2, top3, ip)
    print_file("/home/output/result.txt")