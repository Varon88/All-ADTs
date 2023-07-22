Stack = [0 for i in range(10)]
BaseOfStackPointer = 0
ElementCount = 0
Max = 11

##Adding elements in to the stack
def Push(Item):
    global Stack,BaseOfStackPointer,ElementCount,Max
    if ElementCount == 11 and BaseOfStackPointer == 10:
        print("Stack limits exceeded.")
    else:
        if ElementCount == 0:
            Stack[BaseOfStackPointer] = Item
            ElementCount += 1
        else:
            BaseOfStackPointer += 1
            Stack[BaseOfStackPointer] = Item
            ElementCount += 1

def Pop():
    global Stack,BaseOfStackPointer,ElementCount,Max
    if ElementCount == 0:
        print("Stack is empty.")
    else:
        print(Stack[BaseOfStackPointer])
        Stack[BaseOfStackPointer] = '0'
        BaseOfStackPointer -= 1
        ElementCount -= 1



##Mains
print("press 1 for elemenets to be pushed.")
print("press 2 for elemenets to be poped.")
print("press 3 to print elements.")
print("press # to terminate task.")
x = str(input("enter the option chosen -->"))
while x != "#":
    if x == "1":
        Item = input("Enter element to be pushed -->")
        Push(Item)
    elif x == "2":
        Pop()
    else:
        print(Stack)
    x = str(input("enter the option chosen -->"))
