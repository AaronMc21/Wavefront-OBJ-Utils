import os

# Searches through the local directory (does not include subdirectories for now) and finds all .obj files, doesnt get tripped up by .obj appearing earlier and isn't the file extention e.g. cube.obj.txt
# Returns list of .obj files
def getOBJs():
    foundOBJs = []
    files = os.listdir('./')
    for i in files:
        if i.find('.obj', len(i)-4, len(i)) != -1:
            foundOBJs.append(i)
    return foundOBJs

def getComps(objIndex, foundObjs, verts, vertsNormal, faceSets):
    with open(foundObjs[objIndex]) as f:
        lines = f.readlines()
    for line in lines:
        if line.find('v ', 0, 2) != -1:
            verts.append(line)
        elif line.find('vn', 0, 2) != -1:
            vertsNormal.append(line)
        elif line.find('f ', 0, 2) != -1:
            faceSets.append(line)

def main():
    xverts = []
    xvertsNormal = []
    xfaceSets = []
    objs = getOBJs()
    getComps(0, objs, xverts, xvertsNormal, xfaceSets)
    for face in xfaceSets:
        remFace = face.replace('f ', '')
        remFace2 = remFace.replace('//', ' ')
        remFace3 = remFace2.replace('\n', '')
        indexs = remFace3.split(' ')
        actVerts = []
        actNormals = []
        for i in range(len(indexs)):
            if i%2 == 0:
                cleanVerts = xverts[int(indexs[i])-1].replace('v ', '')
                cleanVerts2 = cleanVerts.replace('\n', '')
                splitVerts = cleanVerts2.split(' ')
                actVerts.append((splitVerts[0] + 'f, ' + splitVerts[1] + 'f, ' + splitVerts[2] + 'f, '))
            else:
                cleanNormals = xvertsNormal[int(indexs[i])-1].replace('vn ', '')
                cleanNormals2 = cleanNormals.replace('\n', '')
                splitNormals = cleanNormals2.split(' ')
                actNormals.append((splitNormals[0] + 'f, ' + splitNormals[1] + 'f, ' +splitNormals[2] + 'f,'))

        print(actVerts[0] + actNormals[0])
        print(actVerts[1] + actNormals[1])
        print(actVerts[2] + actNormals[2])

if __name__ == "__main__":
    main()
