f = open('newfile.pbtxt', 'w')

for i in range(1, 401):
    data = "item { \n" + "  id: " + str(i) + "\n  name: '" + str(i) + '\'\n}\n'
    f.write(data)
f.close()
