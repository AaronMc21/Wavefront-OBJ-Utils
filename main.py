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

def main():
    print("Hello OBJ")
    objs = getOBJs()
    with open(objs[0]) as f:
        lines = f.readlines()
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
