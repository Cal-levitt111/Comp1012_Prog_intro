nested_list = [[1, 4, 0, 1, 3, 1], 
               [2, 2, 4, 2, 2, 3], 
               [1, 0, 1, 0, 1, 0]]

averaged_list = []

for i in range(0, len(nested_list)):

    averaged_list.append([])

    for j in range(0, len(nested_list[i])):

    
        if i == 0:
            if j == 0:
                average = (nested_list[i][j] + nested_list[i + 1][j] + nested_list[i][j + 1]) / 3


            elif j == len(nested_list[i]) - 1:
                average = (nested_list[i][j] + nested_list[i + 1][len(nested_list[i+1]) - 1] + nested_list[i][j-1]) / 3
            

            else:
                average = (nested_list[i][j] + nested_list[i + 1][j] + nested_list[i][j + 1] + nested_list[i][j - 1]) / 4


        elif i == (len(nested_list) - 1):
            if j == 0:
                average = (nested_list[i][j] + nested_list[i - 1][j] + nested_list[i][j + 1]) / 3


            elif j == len(nested_list[i]) - 1:
                average = (nested_list[i][j] + nested_list[i - 1][len(nested_list[i-1]) - 1] + nested_list[i][j-1]) / 3
            

            else:
                average = (nested_list[i][j] + nested_list[i - 1][j] + nested_list[i][j + 1] + nested_list[i][j - 1]) / 4
            
        
        else:
            if j == 0:
                average = (nested_list[i][j] + nested_list[i + 1][j] + nested_list[i - 1][j] + nested_list[i][j + 1]) / 4


            elif j == len(nested_list[i]) - 1:
                average = (nested_list[i][j] + nested_list[i + 1][len(nested_list[i+1]) - 1] + nested_list[i - 1][len(nested_list[i-1]) - 1] + nested_list[i][j-1]) / 4
            

            else:
                average = (nested_list[i][j] + nested_list[i + 1][j] + nested_list[i - 1][j] + nested_list[i][j + 1] + nested_list[i][j - 1]) / 5


        averaged_list[i].append(int(round(average, 0)))

print(averaged_list)
        


            
