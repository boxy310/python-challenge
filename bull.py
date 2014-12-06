a = ['1']

def startDict(a,idict,i,idictindex):
    idict.append([])
    idict[idictindex] = [a[i],1]
    return idict

def addEntry(a,idict,i,idictindex):
    idict.append([])
    idict[idictindex+1] = [a[i],1]
    return idict

def descNumber(a):
    idict = []
    idictindex = 0
    for i in range(len(a)):
        if (i == 0):
            idict = startDict(a,idict,i,idictindex)
        elif (i > 0 and i < len(a)):
            if (a[i] == a[i-1]):
                idict[idictindex][1] += 1
            else:
                idict = addEntry(a,idict,i,idictindex)
                idictindex += 1
    return idict

def parseArray (idict):
    outstring = ''
    for i in range(len(idict)):
        outstring += str(idict[i][1])
        outstring += idict[i][0]
    return outstring

for i in range(35):
    seed = a[i]
    dn = descNumber(seed)
    pa = parseArray(dn)
    a.append(pa)

print len(a[30])
