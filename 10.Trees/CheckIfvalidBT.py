# Check if an array of integer pairs can form a binary tree
# 1. Parent node can only have 2 children
# 2.*All the children node should be unique;

from collections import Counter
def TreeConstructor(strArr):
    parents = []
    children = []
    print(strArr)

    for strTup in strArr:
        for i,v in eval(strTup):
            children.append(int(i))
            parents.append(int(v))

        # strTup = eval(strTup)

    print(children,parents)

        # children.append(int(i[1]))
        # parents.append(int(i[3]))


    for k,v in Counter(parents).items():
        if v > 2:
            print('parent problem')
            return False

    for k,v in Counter(children).items():
        if v > 1:
            print('kid problem')
            return False

    return True

print (TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))      # True
print (TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"] ))      # False
