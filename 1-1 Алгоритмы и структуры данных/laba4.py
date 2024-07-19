s = input("Введите последовательность: ")
matrix = []
flag = 0
for i in range(len(s)):
    if s[i] == '(':
        element = [1, 0]
        matrix.append(element)
    elif s[i] == ')':
        for j in range(len(matrix)):
            if matrix[j][1] == 0:
                matrix[j][1] = 1
                break
        else:
            print("Последовательность неверна")
            flag = 1
            exit()
for i in range(len(matrix)):
    if matrix[i][0] == 1 and matrix[i][1] == 1:
        continue
    else:
        flag = 1
        print("Последовательность неверна")
        break
if flag == 0:
    print("Последовательность верна")
    
