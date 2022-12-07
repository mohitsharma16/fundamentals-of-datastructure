class Library:
    name = []
    book_id = []
    cost = []
    new_book_list = []

    def get_data(self):
        for i in range(n):
            self.name.append(input("\033[1m\nName:"))
            self.book_id.append(int(input("ISBN Code:")))
            self.cost.append(int(input("Price:\033[0m")))

    def duplicate(self):
        temp_list = []
        for x in self.name:
            if x not in temp_list:
                temp_list.append(x)
        self.name = temp_list
        print("List after deleting duplicate values is", temp_list)

    def cost_check(self):
        cost_less = []
        cost_high = []
        for j in self.cost:
            if j < 500:
                cost_less.append(j)
            else:
                cost_high.append(j)
        print("The total count of books with price greater than 500 is:", len(cost_high))

    def cost_value(self):
        cost_less = []
        for j in self.cost:
            if j < 500:
                cost_less.append(j)
        if len(cost_less) == 0:
            print("No book available with price less than 500")
        else:
            for x in cost_less:
                print("Cost of books less than 500 is:", x)

    def ascending_order(self):  # Function for ascending order
        self.cost.sort()
        print("Cost of books in ascending order is", self.cost)

    def display_data(self):  # Function for displaying data
        print("\nName\t\t\tISBN Code\t\t\tCost")
        for i in range(n):
            print(self.name[i], "\t\t", self.book_id[i], "\t\t\t₹", self.cost[i])


if __name__ == "__main__":
    n = int(input("Enter number of books:"))
    l = Library()
    l.get_data()
    l.display_data()
    while True:
        choice = int(input('\na) Delete the duplicate entries\nb) Display books in ascending order based on cost of '
                           'books\nc) Count number of books with cost more than 500\nd) Copy books in a new list '
                           'which has cost less than 500.\ne)Exit\nEnter choice code:'))
        if choice == 1:
            Library().duplicate()
        elif choice == 2:
            l.ascending_order()
        elif choice == 3:
            l.cost_check()
        elif choice == 4:
            l.cost_value()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("\033[91mChoose valid choice!!\033[0m")

