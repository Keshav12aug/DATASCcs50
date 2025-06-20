import re
text = "The quick brown fox jumps over the lazy dog."

#search for a pattern
match = re.search("jumps", text)
print(match)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())

#finding all occurences of a pattern

matches = re.findall("the",text, re.IGNORECASE) #case insensitive search
print("Matches:", matches)
print(matches)

#replacing the text

new_text = re.sub("fox", "cat", text)
print("New_text :", new_text)