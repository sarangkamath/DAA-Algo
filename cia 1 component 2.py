def Push(S,N):
    S.append(N)

def Pop(S):
    if S==[]:
        print("Stack is Empty" )
    else:
        return S.pop()

def display(S):
    if S==[]:
        print("Stack is empty")
    else:
        for i in range(len(S)):
            print(S[i])

my_list=[]
ans='y'
while ans.lower()=='y':
    print("\nMenu\n1.Push \n2.Pop \n3.Display")
    choice=int(input("Please enter your choice: "))
    if choice==1:
        num=int(input("Enter the number to be pushed : "))
        Push(my_list,num)
        print("Element pushed successfully")
        ans=input("do you wish to continue(y/n): ")
    elif choice==2:
        result=Pop(my_list)
        print("Element poped is: ",result)
        ans=input("do you wish to continue(y/n): ")
    elif choice==3:
        display(my_list)
        ans=input("do you wish to continue(y/n): ")
    elif choice>3:
        print("Incorrect choice")
        ans=input("do you wish to continue(y/n): ")