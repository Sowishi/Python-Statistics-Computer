def weight_mean(weight,data):
    sum = 0
    weight_sum = 0
    print("Data: \n")
    #Display data
    for i in data:
        s = i.split("=")
        print(f"{s[0]}: {s[1]}")
    print("")
    print("Criteria: \n")
    #Display carteria and add to the var above
    for i in range(len(weight)):
        w = weight[i].split("=")
        d = data[i].split("=")
        sum += int(w[1])*int(d[1])
        weight_sum += int(w[1])
        print(f"{w[0]}: {w[1]}%")
    #print the mean avg
    print("")
    mean = sum / weight_sum
    print(f"The weighted mean for this data is: {mean}%")
#Taking the input
weight = input("Type the criteria (seperate it with equal sign): ")
data =  input("Type the data (seperate it with equal sign): ")
w = weight.split()
d = data.split()
weight_mean(w,d)
