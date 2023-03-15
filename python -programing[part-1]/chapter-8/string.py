# python3 chapter-8/string.py

# s = 'hello'
# print(len(s))

s = "Dimik' s"
s = 'Dimik\' s'
print(len(s))

country = 'Bangladesh'
print(country[0])

# for c in country:
#     print(c)

c = ['A', 'B', 'C']
print(c)
c[0] = 'a'
print(c)

country = 'Bangla' + 'desh'
print(country)
print(country.find('Bengla'))
print(country.find('desh'))

new_country = country.replace('desh','Bangali')
print(new_country)
print(country)

text = ' this is a string. '
print(text.lstrip())
print(text.rstrip())
print(text.strip())
print(text)

print(country.upper())
print(country.lower())
print(country.capitalize())

str = 'I    am  a programmer.'
words = str.split()
print(words)
for word in words:
    print(word)

str = 'This is'
print(str.count('is'))


print(country.startswith("Ban"))
print(country.startswith("ban"))
print(country.endswith("desh"))

str = 'a quick brown fox jumps over the lazy dog'
for c in 'abcdefghijklmnopqrstuvwxyz':
    print(c, str.count(c))