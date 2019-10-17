class node:
    """A single node of a binary tree"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

    def set_key(self, k):
        self.key = k

    def set_value(self, v):
        self.value = v

    def set_right(self, r):
        self.right = r

    def set_left(self, l):
        self.left = l

    def set_parent(self, p):
        self.parent = p

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_parent(self):
        return self.parent

    def __repr__(self):
        return 'key: %s, value: %s, right(key): %s, left(key): %s, parent(key): %s' % (self.get_key(),
           self.get_value(),
           self.get_right().get_key() if self.get_right() != None else None,
           self.get_left().get_key() if self.get_left() != None else None,
           self.get_parent().get_key() if self.get_parent() != None else None)

def main():
    #Some testing
    n1 = node(18, 'Bark')
    n2 = node(12, 'Ken')
    n1.set_left(n2)
    n2.set_parent(n1)

    print 'n1:\t', repr(n1)
    print 'n2:\t', repr(n2)


if __name__ == "__main__":
    main()
