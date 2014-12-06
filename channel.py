import os
import zipfile
path = '/home/boxy/Challenge'
zfile = 'channel.zip'

os.chdir(path)
zippy = zipfile.ZipFile(zfile)

seed = '90052'
output = open('channelout.txt', "w")


def loopfile(seed, output, zippy):
	for i in range(2000):
		filename = seed+'.txt'
		line = zippy.read(filename)
		#line = data.readline()
		print line
		seed = line[16:len(line)]
		if not(seed.isdigit()):
			break
		comment = zippy.getinfo(filename).comment
		output.write(comment)
		#data.close()

loopfile(seed, output, zippy)
