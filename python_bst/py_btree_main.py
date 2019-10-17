from py_btree_tree import bstree as bst

BLAH = 7777

def main():
    t1 = bst()

    #test insert
    keys = [21,7,5,11,17,2,14]
    for index, key in enumerate(keys):
        t1.insert((key, index))
    print(t1)
    
    t1.insert((21, BLAH)) #testing insert on existing key
    print(t1)

    #test remove
    t1.remove(7)
    print(t1)
    t1.remove(21)
    print(t1)
    t1.remove(5)
    print(t1)
    t1.remove(BLAH) #testing remove on non-existing key
    print(t1)
    t1.remove(17)
    print(t1)
    
    #testing find
    print 'find(14) result is: ', t1.find(14)
    try:
        print 'find(7) result is: ', t1.find(7)
    except Exception, e:
        print(e)

    #testing repr
    print repr(t1)

    #testing iter
    for pair in t1:
        print(pair),

if __name__ == "__main__":
    main()
