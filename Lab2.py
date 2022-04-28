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
    calc_min_max_temperature(num_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    my_list = input('Enter the numbers that you want to input : ')
    hi = my_list.split(",")
    return [float(x) for x in hi]


def calc_average_temperature(list_calc):
    return (sum(map(float, list_calc)))/len(list_calc)


def calc_min_max_temperature(num_list):
    print("maximum is : ")
    print(max(num_list))
    print("Minimum is : ")
    print(min(num_list))


if __name__ == "__main__":
    main()



