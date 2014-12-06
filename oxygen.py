import Image

imgfile = '~/Challenge/oxygen.png'

oxyim = Image.load(imgfile)
pix_val = list(oxyim.getdata())
pix_mat = []
pix_ind = 0

for i in range(95):
    pix_matr.append([])
    for j in range(629):
        pix_matr[i].append(pix_val[pix_ind])
        pix_ind += 1

for i in range(40,55):
    print "Row "+str(i)
    for j in range(40):
        print pix_matr[i][j]
# first repeating line is 43

testrow = pix_matr[43]
for i in range(0, 608, 7):
    output.append(testrow[i][0])

decoded = ''
for i in range(len(output)):
    decoded += chr(output[i])
print decoded

recode = [105, 110, 116, 101, 103, 114, 105, 116, 121]
redecoded = ''

for i in range(len(recode)):
    redecoded += chr(recode[i])
    
print redecoded

