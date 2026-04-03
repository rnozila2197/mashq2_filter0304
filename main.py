# 16
roy = ["apple", "banana", "kiwi", "strawberry"]

natija = list(filter(lambda el: len(el) > 5, roy))
print(natija)

# 17
roy = ["apple", "pear", "grape", "plum"]

natija = list(filter(lambda x: 'a' in x, roy))
print(natija)

# 18
roy = ["Ali", "vali", "Sardor", "john"]

natija = list(filter(lambda x: x[0].isupper(), roy))
print(natija)

# 19
roy = ["", "hello", "world", "python"]
print(roy)

res = list(filter(lambda x: x == x.isdigit, roy))
print(res)

# 20
roy = ["", "hello", "", "world"]

res = list(filter(lambda s: s != "", roy))
print(res)

# 21
roy = ["hi", "hello", "world", "python"]

res = list(filter(lambda s: len(s) % 2 == 0, roy))
print(res)

# 22
roy = ["java", "python", "javascript", "c++"]
print(roy)

res = list(filter(lambda a: len(a) > 6, roy))
print(res)

# 23
roy = ["python", "java", "kotlin", "go"]
print(roy

res = [s for s in roy if s.endswith('n')]
print(res)

# 24
roy = ["abc1", "hello", "test2", "world"]
print(roy)

res = list(filter(lambda s: (c.isdigit() for c in s), roy))

print(res)

# 25
roy = ["abc", "123", "hello1", "world"]
print(roy)

res = list(filter(lambda s: s.isalpha(), roy))
print(res)

# 26
roy = [None, 1, 2, None, 3, 4]
print(roy)

res = list(filter(lambda x: x is not None, roy))
print(res)

# 27
roy = [None, 1, 2, None, 3, 4]
print(roy)

res = list(filter(lambda x: x is not None, roy))
print(res)

# 28
roy = [0, 1, False, 2, "", 3]
print(roy)

res = list(filter(bool, roy))
print(res)

# 29
roy = [1, 2.5, 3, "4", 5]
print(roy)

res = list(filter(lambda x: isinstance(x, int), roy))
print(res)

# 30
roy = [1, 2.5, 3.0, "4", 5]
print(roy)

res = list(filter(lambda x: isinstance(x, float), roy))
print(res)
