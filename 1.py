""" PlanCDEFGHIJKLMNOPQRSTUVWXYZ """
def main():
    """ Main Function """
    text = str(input())
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    total = (num_1 > num_2)*num_1+(num_2 > num_1)*num_2+(num_1 == num_2)*num_1
    highest = (total > num_3)*total+(num_3 > total)*num_3+(total == num_3)*total
    lower = (num_1 < num_2)*num_1+(num_2 < num_1)*num_2+(num_1 == num_2)*num_1
    lower = (lower < num_3)*lower+(num_3 < lower)*num_3+(lower == num_3)*lower
    middle = (num_1+num_2+num_3)-highest-lower
    if text == "Ascend":
        print("%.2f, %.2f, %.2f" %(lower, middle, highest))
    if text == "Descend":
        print("%.2f, %.2f, %.2f" %(highest, middle, lower))
main()
