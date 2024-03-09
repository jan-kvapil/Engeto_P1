"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Kvapil
email: kvapil.h@gmail.com
discord: jendakvapil
"""
import string
from task_template import TEXTS, USERS

user_name = str(input("Insert user name:")).lower()
user_password = input("Insert user password:")

if user_name not in USERS:
    print("Unregistered user, terminating the program...")
    exit()
if USERS[user_name] != user_password:
    print("Unregistered user, terminating the program...")
    exit()

print("----------------------------------------")
print(f"Welcome {user_name}")
print("We have 3 texts to be analyzed.")
print("----------------------------------------")
textNumber = int(input("Enter number 1 to 3 to select text:")) - 1
print("----------------------------------------")

if not (-1 < textNumber <= 2):
    print("Wrong number")
    exit()

selected_text = TEXTS[textNumber].split()

# Remove punctuation from selected text
for word in range(len(selected_text)):
    if not selected_text[word].strip(string.punctuation).isdigit():
        selected_text[word] = selected_text[word].strip(string.punctuation)

print("----------------------------------------")
# Number of words
print(f"There are {len(selected_text)} words in the selected text")
# Number of titlecase words
print(f"There are {sum(1 for word in selected_text if (word.isalpha() and word.istitle()))} titlecase words")
# Number of upper case words
print(f"There are {sum(1 for word in selected_text if (word.isalpha() and word.isupper()))} uppercase words")
# Number of lower case words
print(f"There are {sum(1 for word in selected_text if (word.isalpha() and word.islower()))} lowercase words")
# Number of numeric strings
print(f"There are {sum(1 for word in selected_text if word.isdigit())} numeric strings")
# and the sum of the numeric strings
print(f"The sum of all the numbers {sum(int(number) for number in selected_text if number.isdigit())}")
print("----------------------------------------")

# Keys = word lengths
# Values = length occurrence
lens = {}
for word in selected_text:
    if not len(word) in lens:
        lens[len(word)] = 0
    lens[len(word)] += 1

# Find width of the middle column of the final graph
if len("  OCCURRENCES  ") > max(lens.values()):
    center_column_width = len("  OCCURRENCES  ")
else:
    center_column_width = max(lens.values())

print("LEN|", "OCCURRENCES".center(center_column_width, " "), "|NR.", sep="")
print("----------------------------------------")

length = 1
while lens:
    if length in lens.keys():
        print(str(length).rjust(3, " "), "|", ("*" * lens[length]).ljust(center_column_width, " "), "|", lens[length],
              sep="")
        lens.pop(length)
    length += 1
