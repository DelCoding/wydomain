#coding:utf-8

#本文件用来测试某些代码，非项目文件

f = open('e:/1.txt','r')
f_lines = f.readlines()

fd = open('e:/2.txt', 'r')
fd_arr = fd.readline()
arr = []
while fd_arr:
    fd_arr = fd_arr.split(' ')[1]
    arr.append(fd_arr)
    fd_arr = fd.readline()
print len(arr)
ff = open('e:/4.txt','a+')
num = 0
a = 0

for line in f_lines:
    judge = True
    new = line.split(' ')[0]
    for t in arr:
        t = t.rstrip('\n')
        if new == t:
            judge = False
            break
    if judge == True:
        ff.write(line)
        num += 1

fd.close()

print '写入：' + str(num)
f.close()
ff.close()
