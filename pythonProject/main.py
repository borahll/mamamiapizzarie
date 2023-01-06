import sys


def isvalid(matrixlen, x, y):  # check if the provided x and y are valid in the matrix
    if 0 <= x < matrixlen and 0 <= y < matrixlen:
        return True
    else:
        return False


def findmax(amatrix):  # function to return the maximum number in a matrix
    max1 = amatrix[0][0]
    for row in amatrix:
        for column in amatrix:
            if max1 < amatrix[row][column]:
                max1 = amatrix[row][column]
    return max1


first_line = sys.stdin.readline()
x = first_line.split(' ')
matrix_lenght = x[0]
num_of_pizzarias = x[1]
matrix = [[0] * int(matrix_lenght)] * int(matrix_lenght)
matrix_lenght = int(matrix_lenght)
origin_of_pizzeria_x = ""
origin_of_pizzeria_y = ""
serve_radius = ""

sys.stdin.readline()
for i in range(int(num_of_pizzarias)):
    line = sys.stdin.readline()
    for ch in line:
        if ch == " ":
            break
        origin_of_pizzeria_x += ch
    for ch in line:
        if ch == " ":
            break
        origin_of_pizzeria_y += ch
    for ch in line:
        if ch == " ":
            break
        serve_radius += ch
    origin_of_pizzeria_x = int(origin_of_pizzeria_x) - 1
    origin_of_pizzeria_y = int(origin_of_pizzeria_y) - 1
    print(origin_of_pizzeria_y)
    serve_radius = int(serve_radius)
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
        start_y = origin_of_pizzeria_y + tempserve
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                for b in range(counter):
                    tempxx = tempx
                    tempyy = tempy
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx += 1
                        tempyy -= 1
                tempy -= 1
            first = True
        else:
            tempserve -= 1
    # this following code block is the 2nd part of the catesian coordianate system
    tempserve = serve_radius
    tempx = start_x
    tempy = start_y
    for k in range(serve_radius):
        start_y = origin_of_pizzeria_y + tempserve
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                for b in range(counter):
                    tempxx = tempx
                    tempyy = tempy
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx -= 1
                        tempyy -= 1
                tempy -= 1
            second = True
        else:
            tempserve -= 1
    # this following code block is the 3rd part of the catesian coordianate system
    tempserve = serve_radius
    tempx = start_x
    tempy = start_y
    for k in range(serve_radius):
        start_y = origin_of_pizzeria_y - (tempserve + 1)
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                for b in range(counter):
                    tempxx = tempx
                    tempyy = tempy
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx -= 1
                        tempyy += 1
                tempy += 1
            third = True
        else:
            tempserve += 1
    # this following code block is the 4th part of the catesian coordianate system
    tempserve = serve_radius
    tempx = start_x
    tempy = start_y
    for k in range(serve_radius):
        start_y = origin_of_pizzeria_y - (tempserve + 1)
        if isvalid(matrix_lenght, start_x, start_y):
            for a in range(tempserve):
                for b in range(counter):
                    tempxx = tempx
                    tempyy = tempy
                    if isvalid(matrix_lenght, tempxx, tempyy):
                        matrix[tempxx][tempyy] += 1
                        tempxx += 1
                        tempyy += 1
                tempy += 1
            fourth = True
        else:
            tempserve += 1
    if first and second:
        temp = serve_radius
        for a in range(serve_radius):
            print(serve_radius)
            matrix[origin_of_pizzeria_x][origin_of_pizzeria_y + temp] -= 1
            temp -= 1
    if third and fourth:
        temp = serve_radius
        for a in range(serve_radius):
            matrix[origin_of_pizzeria_x][origin_of_pizzeria_y - (temp + 1)] -= 1
            temp -= 1
print(f' The maximum is  {findmax(matrix)}')
