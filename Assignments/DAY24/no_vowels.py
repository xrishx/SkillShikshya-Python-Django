para = """
This is a paragraph.
We are going to print this paragraph,
but without any vowels.
"""

for char in para:
    if char not in "aeiou":
        print(char, end="")
        