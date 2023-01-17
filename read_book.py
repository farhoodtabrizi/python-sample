file = open ('books.txt', 'r')
lines = file.readlines()
n = len (lines)
for i in lines:
    if lines.index(i) != n-1:
      print (i[0]+str((len(i)-1)))
    elif lines.index (i) == n-1:
      print (i[0]+str((len(i))))
file.close()
