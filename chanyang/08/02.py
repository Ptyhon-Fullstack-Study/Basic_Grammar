import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)
for r in result:
    print(r)

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = re.match('[a-z]+', "python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

p = re.compile('a.b')
m = p.match("a\nb")
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match("a\nb")
print(m)

p = re.compile('[a-z]+')
m = p.match('Python')
print(m)

p = re.compile('[a-z]+', re.I)
m = p.match('Python')
print(m)

p = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
