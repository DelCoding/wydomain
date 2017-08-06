#coding:utf-8

#本文件用来测试某些代码，非项目文件

f = open('try2.txt','r')
lines = f.readlines()
ff = open('try3.txt','a+')
for line in lines:
    line = line.strip('\n')
    new = '\t' + '"' + line + '"' + '\n'
    ff.write(new)

f.close()
ff.close()
