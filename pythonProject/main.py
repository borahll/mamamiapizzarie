import sys


def isvalid(matrixlen, x1, y):  # check if the provided x and y are valid in the matrix
    if 0 <= x1 < matrixlen and 0 <= y < matrixlen:
        return True
    else:
        return False


def findmax(amatrix):  # function to return the maximum number in a matrix
    max1 = amatrix[0][0]
    for row in amatrix:
        for element in row:
            if max1 < element:
                max1 = element
    return max1


def printmatrix(amatrix):
    for row in amatrix:
        print(" ".join(str(element) for element in row))


first_line = sys.stdin.readline()
x = first_line.split(' ')
matrix_lenght = x[0]
num_of_pizzarias = x[1]
matrix = [[0 for j in range(int(matrix_lenght))] for i in range(int(matrix_lenght))]
printmatrix(matrix)
matrix_lenght = int(matrix_lenght)
origin_of_pizzeria_x = ""
origin_of_pizzeria_y = ""
serve_radius = ""


for i in range(int(num_of_pizzarias)):
    line = sys.stdin.readline()
    x = line.split(" ")
    origin_of_pizzeria_x = x[0]
    origin_of_pizzeria_y = x[1]
    serve_radius = x[2]
    origin_of_pizzeria_x = int(origin_of_pizzeria_x) - 1
    origin_of_pizzeria_y = int(origin_of_pizzeria_y) - 1
    serve_radius = int(serve_radius)
    print(f"{origin_of_pizzeria_y} {origin_of_pizzeria_x} {serve_radius}")
    start_x = origin_of_pizzeria_x
    start_y = origin_of_pizzeria_y
    matrix[start_x][start_y] += 1

    start_x = origin_of_pizzeria_x
    start_y = origin_of_pizzeria_y
    counter = 1 + serve_radius
    first = False
    second = False
    third = False
    fourth = False

    # this following code block is the 1st part of the catesian coordianate system
    tempserve = serve_radius
    tempx = start_x
    tempy = start_y
    for k in range(serve_radius):
        start_x = origin_of_pizzeria_x - tempserve
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                tempxx = start_x
                tempyy = tempy
                for b in range(counter):
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx += 1
                        tempyy += 1
                start_x += 1
                printmatrix(matrix)
            first = True
            break
        else:
            tempserve -= 1
    # this following code block is the 2nd part of the catesian coordianate system
    tempserve = serve_radius
    tempx = start_x
    tempy = start_y
    for k in range(serve_radius):
        start_x = origin_of_pizzeria_x - tempserve
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                tempxx = tempx
                tempyy = tempy
                for b in range(counter):
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx -= 1
                        tempyy -= 1
                tempx += 1
                #printmatrix(matrix)
            second = True
            break
        else:
            tempserve -= 1
    # this following code block is the 3rd part of the catesian coordianate system
    tempserve = serve_radius
    tempx = start_x
    tempy = start_y
    for k in range(serve_radius):
        start_x = origin_of_pizzeria_x + (tempserve + 1)
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                tempxx = start_x
                tempyy = tempy
                for b in range(counter):
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx -= 1
                        tempyy -= 1
                start_x -= 1
                #printmatrix(matrix)
            third = True
            break
        else:
            tempserve += 1
    # this following code block is the 4th part of the catesian coordianate system
    tempserve = serve_radius
    tempx = start_x
    tempy = start_y
    for k in range(serve_radius):
        start_x = origin_of_pizzeria_x + (tempserve + 1)
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                tempxx = start_x
                tempyy = tempy
                for b in range(counter):
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx -= 1
                        tempyy += 1
                start_x -= 1
                #printmatrix(matrix)
            fourth = True
            break
        else:
            tempserve += 1
    if first and second:
        temp = serve_radius
        for a in range(serve_radius):
            matrix[origin_of_pizzeria_x][origin_of_pizzeria_y + temp] -= 1
            temp -= 1
    if third and fourth:
        temp = serve_radius
        for a in range(serve_radius):
            matrix[origin_of_pizzeria_x][origin_of_pizzeria_y - (temp + 1)] -= 1
            temp -= 1
print(f" The maximum is  {findmax(matrix)}")
