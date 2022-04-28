def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(type(num_list))
    average = calc_average_temperature(num_list)
    print("Average is : ")
    print(average)
    print("The minimum and maximum is : ")
    print(calc_min_max_temperature(num_list))
    print("The median is : ")
    print(calc_median_temperature(num_list))


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    my_list = input('Enter the numbers that you want to input : ')
    hi = my_list.split(",")
    return [float(x) for x in hi]


def calc_average_temperature(list_calc):
    return (sum(map(float, list_calc)))/len(list_calc)


def calc_min_max_temperature(num_list):
    mini = min(num_list)
    maxi = max(num_list)
    return [mini, maxi]


def calc_median_temperature(lst):
    slst = sorted(lst)
    if (len(slst)) % 2 == 0:
        return int((slst[len(slst) / 2] + slstint[(len(slst) - 1) / 2]) / 2)
    else:
        # If length is odd then get middle value
        return slst[int(len(slst) / 2)]


if __name__ == "__main__":
    main()



