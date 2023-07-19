NullPointer = -1

class TreeNode:
    def __init__(self):
        self.TreeData = None
        self.LeftPointer = None
        self.RightPointer = None

Tree = [TreeNode() for i in range(6)]

def InitializeTree():
    global FreePointer, RootPointer
    RootPointer = NullPointer
    FreePointer = 0
    for i in range(6):
        Tree[i].LeftPointer = i + 1
    Tree[5].LeftPointer = NullPointer


def InsertNode(NewItem):
    global FreePointer,RootPointer
    if FreePointer != NullPointer:
        NewNodePointer = FreePointer
        FreePointer = Tree[FreePointer].LeftPointer
        Tree[NewNodePointer].TreeData = NewItem
        Tree[NewNodePointer].LeftPointer = NullPointer
        Tree[NewNodePointer].RightPointer = NullPointer
        if RootPointer == NullPointer:
            RootPointer = NewNodePointer
        else:
            TurnedLeft = False
            ThisNodePointer = RootPointer
            while ThisNodePointer != NullPointer:
                PreviousNodePointer = ThisNodePointer
                if Tree[ThisNodePointer].TreeData > NewItem:
                    TurnedLeft = True
                    ThisNodePointer = Tree[ThisNodePointer].LeftPointer
                else:
                    TurnedLeft = False
                    ThisNodePointer = Tree[ThisNodePointer].RightPointer
            if TurnedLeft == True:
                Tree[PreviousNodePointer].LeftPointer = NewNodePointer
            else:
                Tree[PreviousNodePointer].RightPointer = NewNodePointer


def FindNode(SearchItem):
    global FreePointer, RootPointer
    ThisNodePointer = RootPointer
    while ThisNodePointer != NullPointer and Tree[ThisNodePointer].TreeData != SearchItem:
        if Tree[ThisNodePointer].TreeData > SearchItem:
            ThisNodePointer = Tree[ThisNodePointer].LeftPointer
        else:
            ThisNodePointer = Tree[ThisNodePointer].RightPointer
    return ThisNodePointer



        
InitializeTree()
for j in range(6):
    x = input("Enter element -->")
    InsertNode(x)

for count in range(6):
    print(Tree[count].LeftPointer,Tree[count].TreeData,Tree[count].RightPointer)
