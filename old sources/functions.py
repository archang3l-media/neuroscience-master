list = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_list(list):
    for grade in list:
        print(grade)

def list_sum(list):
    total = 0
    for grade in list:
        total += grade
    return total

def list_average(list):
    sum_of_list = list_sum(list)
    average = sum_of_list / float(len(list))
    return average

def list_variance(scores):
    average = list_average(scores)
    variance = 0
    for score in scores:
        variance = variance + ((average - score)**2)
    variance = variance / len(scores)
    return variance
def list_std_deviation(variance):
    return variance ** 0.5
variance = list_variance(list)
print_list(list)
print (list_sum(list))
print (list_average(list))
print (list_variance(list))
print (list_std_deviation(variance))
