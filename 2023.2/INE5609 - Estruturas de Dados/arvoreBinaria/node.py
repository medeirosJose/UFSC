# Árvore binária de Busca - No
# def search (key):
#   if root != None:
#       recursiveSearch (root, key)
#   else:
#       return false

# def recursiveSearch (root, key):
# if root != None:
#   if root.value == search:
#       return true
#   else if key < root.value:
#       return recursiveSearch (root.leftRoot, key)
#   else:
#       return recursiveSearch (root.rightRoot, key)
# else:
#   return false


class No:
    def __init__(self, value, leftRoot=None, rightRoot=None):
        self.value = value
        self.leftRoot = leftRoot
        self.rightRoot = rightRoot

    @property
    def leftRoot(self):
        return self.leftRoot

    @property
    def rightRoot(self):
        return self.rightRoot

    @property
    def value(self):
        return self.value

    @leftRoot.setter
    def setleftRoot(self, leftRoot):
        self.leftRoot = leftRoot

    @rightRoot.setter
    def setrightRoot(self, rightRoot):
        self.rightRoot = rightRoot

    @value.setter
    def setValue(self, value):
        self.value = value
