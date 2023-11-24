num_list = []
for i in range(10):
    num_list.append(int(input("Please input your next number")))


print("The sum is",sum(num_list),"The mean is",(sum(num_list)/len(num_list)))
