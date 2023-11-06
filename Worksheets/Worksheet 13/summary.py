
def summarise_data(file, col_index):

    with open(file, "r") as fileObject:
        data_summary = []
        line_list = []
        #max = (fileObject.readline()).split(",")[col_index]
        #min = (fileObject.readline()).split(",")[col_index]

        if type(col_index) is not int or col_index > 2:
            return("IndexError - col_index out of range.")
            
        for line in fileObject:
            if not (line.split(",")[col_index]).isnumeric():
                return("ValueError - invalid value in data.")
            else:
                line_list.append(int(line.split(",")[col_index]))
    if bool(line_list):
        data_summary.append(max(line_list))
        data_summary.append(min(line_list))
        data_summary.append(sum(line_list))
        data_summary.append(len(line_list))
        data_summary.append(round((sum(line_list)/len(line_list)), 2))
    else: 
        data_summary = "Empty file"
        
    return(data_summary)
    

if __name__ == "__main__":
    #  test valid arguments
    print(summarise_data("data.txt", 1))

    #  test out of range col_index, data.txt only has 3 columns
    print(summarise_data("data.txt", 5))

    # test invalid col_index, col_index should be integer
    print(summarise_data("data.txt", "a"))

    # test invalid value in file, contains a "abc" in the second column
    print(summarise_data("data2.txt", 1))


