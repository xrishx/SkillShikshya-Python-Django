
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated
'''

for char in zen:
    if char not in 'aeiou':
        print(char, end="")
