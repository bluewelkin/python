#!/usr/bin/python
import urllib2
import sys
 
def stock_data(stock_id, stock_num, purchase_price):
    url = 'http://hq.sinajs.cn/list=%s%06d' % ((stock_id == 1 or stock_id > 600000) and 'sh' or 'sz', stock_id)
    page = urllib2.urlopen(url)
    stock_data = page.read().split('"')[1]
    name = stock_data.split(',')[0]
    name = name.decode('gb2312').encode('utf-8')
    opening_price = float(stock_data.split(',')[1])
    closing_price = float(stock_data.split(',')[2])
    price = float(stock_data.split(',')[3])
    high = float(stock_data.split(',')[4])
    low = float(stock_data.split(',')[5])
    print '%-10s' % name,
    print '\033[%dm' % (price > closing_price and 31 or 32),
    print '%10.2f' % price,
    print '%10.2f' % (price - closing_price),
    print '%9.2f%%' % ((price - closing_price) * 100 / closing_price),
    print '\033[0m',
    print '%6.2f%%' % ((high - closing_price) * 100 /closing_price),
    print '%6.2f%%' % ((low - closing_price) * 100 / closing_price),
    print '%6.2f%%' % ((high - low) * 100 / closing_price),
    if stock_num > 0:
        #print '%10d' % stock_num,
        #print '%10.3f' % purchase_price,
        print '\033[%dm' % (price > purchase_price and 31 or 32),
        print '%10.2f' % ((price - purchase_price) * stock_num),
        print '%9.2f%%' % ((price - purchase_price) * 100 / purchase_price),
    print '\033[0m'
    return (price - purchase_price) * stock_num
 
if len(sys.argv) != 2:
    print "Usage : sys.argv[0] <stock_list_file>"
    sys.exit(1)
 
total = 0
 
f = file(sys.argv[1], 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    line = line.split('\n')[0]
    line = line.split('\r')[0]
    line = line.split('#')[0]
    if len(line) > 0:
        args = line.split(' ')
        if len(args) == 3:
            total += stock_data(int(args[0]), int(args[1]), float(args[2]))
        if len(args) == 1:
            stock_data(int(args[0]), 0, 0)
f.close()
 
print "\033[1;37;4%dm%.2f\033[0m" % (total > 0 and 1 or 2, total)