from matplotlib import pyplot as plt
from matplotlib import style
def Student(Se,N,Cl):
    print("Hi",N,", You are currently in class :",Cl,"and your session is :",Se)
    print("How'd you like to see your performance ?? ")
    print("Press 1: for subject wise performance graph")
    print("Press 2: for overall performance graph in each examination")
    n=int(input("Enter your choice..."))
    if n==2:
        style.use('ggplot')
        Data={}
        num=int(input("How many examinations have you given : "))
        for i in range (num):
            name=input("Enter your examination name : ")
            mark=float(input("Enter its total marks : "))
            Data[name]=mark
        Examname=list(Data.keys())
        Exammarks=list(Data.values())
        plt.ylabel("Marks scored")
        plt.xlabel("Examinations")
        plt.title("Overall Performance analysis")
        plt.bar(Examname,Exammarks,color="green",width=0.2)
        plt.show()
    elif n==1:
        style.use('ggplot')
        n=int(input("How many subjects ? "))
        data={}
        for i in range (n):
            sub=input("Enter subject : ")
            a="y"
            l=[]
            while a=="y":
                marks=float(input("Enter marks : "))
                l.append(marks)
                a=input("Want to enter more ?")
                data[sub]=l
            Marks=list(data.values())
        for i in range (len(data.values())):
            size=len(Marks[i])
            lst=[j+1 for j in range (size)]
            Markslist=Marks[i]
            Subject=list(data.keys())
            plt.margins(x=0, y=0)
            plt.xticks(lst)
            plt.title("Subject Wise Analysis")
            plt.ylabel("Marks Secured")
            plt.xlabel("Number of examinations")
            plt.plot(lst,Markslist,label=Subject[i])
            plt.legend()
        plt.show()
    else:
        print("Please, press a valid key...")
    return 
N=input("What's your name ? ")
Cl=input("Which class do you study ? ")
Se=input("Enter your session: ")
Student(Se, N, Cl)