class search:
    a = []

    def accept_info(a):
        n = int(input("\nNo.of students:"))
        for i in range(n):
            print("\ncontact no.", i + 1, ":")
            name = input("name:")
            mob = int(input("mobile no:"))

            x = [name, mob]
            a.append(x)
        print("operation successful\n")
        return n

    def fetch_info(a, n):
        if n == 0:
            print("no records in the database!!")
        else:
            print("\nphonebook:")
            for j in range(n):
                swapped = False
                i = 0
                while i < len(a) - 1:
                    if a[i][0] > a[i + 1][0]:
                        a[i], a[i + 1] = a[i + 1], a[i]
                        swapped = True
                    i = i + 1
                if not swapped:
                    break
            print("contact no.\t\tname\tmobile no.")
            for i in range(n):
                print("\t", i + 1, "\t\t\t",a[i][0],"\t\t", a[i][1])

    def binary_search_iterative(a, x):
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if a[mid][0] < x:
                low = mid + 1
            if a[mid][0] > x:
                high = mid - 1
            if a[mid][0] == x:
                return mid
        return -1

    def binary_search_recursive(a, x, high, low):
        if low < high:
            mid = (high + low) // 2
            if a[mid][0] > x:
                return search.binary_search_recursive(a, x, mid, low)
            if a[mid][0] < x:
                return search.binary_search_recursive(a, x, high, mid)
            else:
                return mid
        return -1

    def fibonacci_search(a, n, x):
        f1 = 0
        f2 = 1
        f3 = f1 + f2
        offset = -1
        while f3 < n:
            f1 = f2
            f2 = f3
            f3 = f1 + f2
        while f3 > 1:
            i = min(offset + f1, n - 1)
            if a[i][0] == x:
                return i
            else:
                if x < a[i][0]:
                    f3 = f1
                    f2 = f2 - f1
                    f1 = f3 - f2
                else:
                    f3 = f2
                    f2 = f1
                    f1 = f3 - f2
                    offset = i
        if f2 == 1 and (offset + 1) < n and a[offset + 1][0] == x:
            return offset + 1
        return -1

    def insert_new(a, n, name):
        mob = int(input("contact no:"))
        x = [name, mob]
        a.append(x)
        j = n - 1
        while j >= 0:
            if a[j][0] <= name:
                break
            else:
                a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = x
        print("operation successful!!")
        search.fetch_info(a, n + 1)


if __name__ == "__main__":
    a = []
    print("1.create database\n2.binary search(non-recursive)\n3.binary search(recursive)\n4.fibonacci search\n5.exit")
    while True:
        ch = int(input("\nchoice:"))
        if ch == 1:
            a = []
            n = search.accept_info(a)
            search.fetch_info(a, n )
        elif ch == 2:
            x = input("enter name:")
            response = search.binary_search_iterative(a, x)
            if response == -1:
                print("\003[91mNot Found!!!\033[0m")
                perm = input("add to the phonebook(y/n)?!")
                if perm.lower() == "y":
                    search.insert_new(a, n, x)
                    n = n + 1
                else:
                    continue
            else:
                print("\033[32mAvailable!!!\033[0m\nname:", x, "\nmobile no:", a[response][1], "\nlocation:",
                      response + 1)
        elif ch == 3:
            x = input("enter name:")
            response = search.binary_search_recursive(a, x, n, 0)
            if response == -1:
                print("\033[31mNot Found!!!\033[0m")
                perm = input("add to the phonebook(y/n)?!")
                if perm.lower() == "y":
                    search.insert_new(a, n, x)
                    n = n + 1
                else:
                    continue
            else:
                print("\033[32mAvailable!!!\033[0m\nName:", x, "\ncontact no:", a[response][1], "\nlocation",
                      response + 1)

        elif ch == 4:
            x = input("enter name:")
            response = search.fibonacci_search(a, n, x)
            if response == -1:
                print("\033[31mNot found!!!\033[0m")
                perm = input("add to phone book(y/n)?!")
                if perm.lower() == "y":
                    search.insert_new(a, n, x)
                    n = n + 1
                else:
                    continue
            else:
                print("\033[32mAvailable!!!\033[0m\nName:", x, "\ncontact no:", a[response][1], "\nlocation:",
                      response + 1)
        elif ch == 5:
            print("exiting!!!")
            exit(0)
        else:
            print("\033[91mWrong choice!!!\033[0m")
