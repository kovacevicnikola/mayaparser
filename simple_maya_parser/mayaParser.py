import os
import sys
from copy import deepcopy
from pprint import pprint


def parse(filePath):
    meshList = list()
    currentMeshObject = dict()
    prevLine = None
    if not os.path.isfile(filePath):
        print('File path {} does not exist. Exiting...'.format(filePath))
        sys.exit()
  
    with open(filePath) as fp:
        for line in fp:
            line = line.strip()
            if not currentMeshObject and line.startswith('createNode mesh'):
                currentMeshObject['name'] = line.split(' ')[3].strip('"')
                position = list()
                for linePart in prevLine.split():   
                    try:
                    
                        position.append(float(linePart))
                    except ValueError:
                        continue
                currentMeshObject['position'] = tuple(position)
            elif currentMeshObject and line.startswith('rename'):
                currentMeshObject['uid'] = line[line.find('"'): -3]
                meshList.append(deepcopy(currentMeshObject))
                currentMeshObject = dict()

            prevLine = line
    pprint(meshList)