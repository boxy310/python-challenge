import codecs
import os

fpath = '~/Challenge'
os.chdir(fpath)

un = u'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = u'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

writefile = codecs.open('integrity.txt', mode='w', encoding='utf-16')
writefile.write(un)
writefile.write(pw)
writefile.close()

readfile = codecs.open('integrity.txt', mode='r', encoding='utf-16')

for line in readfile:
    print repr(line)

