class sort:
    def selection_sort(_marks):
        for i in range(len(_marks)):
            min_id=i
            for j in range(i+1,len(_marks)):
                if _marks[min_id]>_marks[j]:
                    min_id=j
            _marks[j],_marks[min_id]=_marks[min_id],_marks[i]
        print("sorted scores:")
        for i in range(len(marks)):
            print(marks[i])

    def bubble_sort(_marks):
        no=len(_marks)
        for i in range(no-1):
            for j in range(0,no-i-1):
                if _marks[j]> _marks[j+1]:
                    _marks[j],_marks[j+1]= _marks[j+1], _marks[j]
        print("sorted scores:")
        for i in range(len(marks)):
            print(marks[i])

    def top_scores(_marks):
        for i in range(len(_marks)-1):
            for j in range(0,len(_marks)-i-1):
                if _marks[j]> _marks[j+1]:
                    _marks[j],_marks[j+1]=_marks[j+1],_marks[j]
        print("top five scorers:")
        print(*marks[4::-1],sep="\n")

if __name__ =='__main__':
    marks=[]
    n=int(input("no of students:"))
    print("enter marks:")
    for i in range(0,n):
        ele=float(input())
        marks.append(ele)
    print("marks:")
    print(marks)
    print("\n------------MENU-----------\n1.selection sort of marks\n2.bubble sort of marks\n3.fetch top five scorers\n4.EXIT")
    while True:
        ch =int(input("\nchoice:"))
        if ch==1:
            sort.selection_sort(marks)
        elif ch==2:
            sort.bubble_sort(marks)
        elif ch==3:
            sort.top_scores(marks)
        elif ch==4:
            print("exiting...")
            break
        else:
            print("not valid!!!")