items = ['latarka', 'woda', 'namiot', "źdźbło", 'gąbka']
with open('example1.txt', 'w') as fopen:
   for i in items:
       # fopen.write(i +"\n")
        fopen.write('\n'.join(items))

