import re

regex = re.compile('[^a-zA-Z]')

print("Is an anagram." if sorted(list(regex.sub('', input().lower().replace(" ", "")))) == sorted(list(regex.sub('', input().lower().replace(" ", "")))) else "Is not an anagram.")
