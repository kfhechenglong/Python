import sys

print(sys.argv)

old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]

print(old_str, new_str, filename)

f = open(filename, "r+")
data = f.read()
print(data)

old_str_count = data.count(old_str)
new_data = data.replace(old_str, new_str)

f.seek(0)
f.truncate()

f.write(new_data)
# f.close()