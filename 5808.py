import Image

imgfile = '~/Challenge/cave.jpg'

im = Image.load(imgfile)
pix_val = list(im.getdata())
pix_mat = []
pix_ind = 0

for i in range(640):
    pix_matr.append([])
    for j in range(840):
        pix_matr[i].append(pix_val[pix_ind])
        pix_ind += 1

