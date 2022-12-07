"""
Write a Python Program for magic square. A magic square is an n * n matrix of the integers 1 to n2 such that the sum of
each row, column, and diagonal is the same.
"""


class magicsquare:
    def generateSquare(n):
        magicSquare = [[0 for x in range(n)]
                       for y in range(n)]

        i = n / 2
        j = n - 1

        num = 1
        while num <= (n * n):
            if i == -1 and j == n:
                j = n - 2
                i = 0
            else:
                if j == n:
                    j = 0
                if i < 0:
                    i = n - 1

            if magicSquare[int(i)][int(j)]:
                j = j - 2
                i = i + 1
                continue
            else:
                magicSquare[int(i)][int(j)] = num
                num = num + 1

            j = j + 1
            i = i - 1

        print("Magic Squre for n =", n)
        print("Sum of each row or column",
              n * (n * n + 1) / 2, "\n")

        for i in range(0, n):
            for j in range(0, n):
                print('%2d ' % (magicSquare[i][j]),
                      end='')

                if j == n - 1:
                    print()

    def num():
        n = int(input("Enter any odd number: "))
        if n % 2 == 0:
            while n != 0:
                n = input("Entered number was even, Please enter odd number: ")
                for no in n:
                    if int(no) % 2 != 0:
                        return int(no)
        else:
            return int(n)


if __name__ == "__main__":
    sq = magicsquare
    n = sq.num()
    sq.generateSquare(n)

