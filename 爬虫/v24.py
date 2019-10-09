import re
s = r'([a-z]+) ([a-z]+)*'
pattern = re.compile(s, re.I)
str = "Hello World Wide Web"

m = pattern.match(str)
# group(0)表示返回匹配成功的整个字符串
s = m.group(0)
print(s)

a = m.span(0) # 返回匹配成功的整个字符串跨度
print(a)

# group(1)表示返回第一个分组匹配成功的字串
s = m.group(1)
print(s)

a = m.span(1) # 返回匹配成功的第一个字串的跨度
print(a)

s = m.groups()# 等价于m.group(1), m.group(2)........
print(s)
