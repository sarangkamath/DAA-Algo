def Enqueue(S,N):
    S.append(N)

def Dequeue(S):
    if S==[]:
        print("Queue is Empty" )
    else:
        return S.pop(0)

def display(S):
    if S==[]:
        print("Queue is empty")
    else:
        for i in range(len(S)):
            print(S[i])

my_list=[]
ans='y'
while ans.lower()=='y':
    print("\nMenu\n1.Enqueue \n2.Dequeue \n3.Display")
    choice=int(input("Please enter your choice: "))
    if choice==1:
        num=int(input("Enter the number to be pushed : "))
        Enqueue(my_list,num)
        print("Element pushed successfully")
        ans=input("do you wish to continue(y/n): ")
    elif choice==2:
        result=Dequeue(my_list)
        print("Element poped is: ",result)
        ans=input("do you wish to continue(y/n): ")
    elif choice==3:
        display(my_list)
        ans=input("do you wish to continue(y/n): ")
    elif choice>3:
        print("Incorrect choice")
        ans=input("do you wish to continue(y/n): ")