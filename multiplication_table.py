fh = open('output.txt','w')

a = int(input("Enter the number : "))
fh.write("The number of table is :" + str(a) + '\n')
i = 1
while i <= 10:
    fh.write(str(a) + "X" + str(i) + "=" + str(a * i )+'\n')
    i += 1

fh.close