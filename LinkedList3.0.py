NullPointer = -1 
class LinkListNode:
    def __init__(self):
        self.Data = None
        self.Pointer = None
        
LinkedList = [LinkListNode() for i in range(6)]

def InitializeLinkList():
    global NullPointer,LinkedList,StartPointer,FreeListPointer
    StartPointer = NullPointer
    FreeListPointer = 0
    for index in range(6):
        LinkedList[index].Pointer = index + 1
    LinkedList[5].Pointer = NullPointer


def InsertNewNode(NewItem):
    global NullPointer,LinkedList,StartPointer,FreeListPointer
    if FreeListPointer != NullPointer:
        NewNodePointer = FreeListPointer
        LinkedList[NewNodePointer].Data = NewItem
        FreeListPointer = LinkedList[FreeListPointer].Pointer
        ##Insertion point
        ThisNodePointer = StartPointer
        PreviousNodePointer = NullPointer
        while ThisNodePointer != NullPointer and LinkedList[ThisNodePointer].Data < NewItem:
            PreviousNodePointer = ThisNodePointer
            ThisNodePointer = LinkedList[ThisNodePointer].Pointer
        if ThisNodePointer == StartPointer:
            LinkedList[NewNodePointer].Pointer = StartPointer
            StartPointer = NewNodePointer
        else:
            LinkedList[NewNodePointer].Pointer = LinkedList[PreviousNodePointer].Pointer
            LinkedList[PreviousNodePointer].Pointer = NewNodePointer
    else:
        print("Sorry no space!")



def DeleteItem(DeleteItem):
    global NullPointer,LinkedList,StartPointer,FreeListPointer
    ThisNodePointer = StartPointer
    PreviousNodePointer = NullPointer
    while ThisNodePointer != NullPointer and LinkedList[ThisNodePointer].Data != DeleteItem:
        PreviousNodePointer = ThisNodePointer
        ThisNodePointer = LinkedList[ThisNodePointer].Pointer
    if ThisNodePointer != NullPointer:
        if ThisNodePointer == StartPointer:
            StartPointer = LinkedList[ThisNodePointer].Pointer
            LinkedList[ThisNodePointer].Data = None
        else:
            LinkedList[PreviousNodePointer].Pointer = LinkedList[ThisNodePointer].Pointer
            LinkedList[ThisNodePointer].Data = None 
        LinkedList[ThisNodePointer].Pointer = FreeListPointer
        FreeListPointer = ThisNodePointer
    for i in range(6):
        print(i,LinkedList[i].Data,LinkedList[i].Pointer)


    
InitializeLinkList()

for count in range(6):
    x = str(input("Enter string -->"))
    InsertNewNode(x)

for i in range(6):
    print(i,LinkedList[i].Data,LinkedList[i].Pointer)

for count in range(3):
    y = str(input("Enter string to be deleted --->"))
    DeleteItem(y)
        
for i in range(6):
    print(i,LinkedList[i].Data,LinkedList[i].Pointer)
    
    

   
