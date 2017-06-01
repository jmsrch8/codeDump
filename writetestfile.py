for number in range(20):
    f = open('test.txt','a')
    f.write(str(number)+'\n')
f.close()
print('done')
