

def read_integers():
    integers = input("Enter some integers: ").split()
    print(integers)


def sum_squared_integers(list1: list) -> int:
    out = 0
    for n in list1:
        out += n**2
    return out


def read_from_file_sum_squares():
    str_filename = input("Enter the filename: ")
    input_file = open(str_filename, "r")
    list_lines = input_file.readlines()
    for i in list_lines:
        out = 0
        num_list = i.split()
        for n in num_list:
            out += int(n)**2
        print(out)
    input_file.close()


def read_from_file_table():
    # filename = input("Enter the filename: ")
    # input_file = open(filename, "r")
    input_file = open("file2", "r")
    list_lines = input_file.readlines()
    out_list = []
    for i in list_lines:
        num_list = i.split()
        num_list = [int(i) for i in num_list]
        for n in num_list:
            if int(n) < 0:
                num_list.remove(n)
        out_list.append(num_list)
    return out_list
    input_file.close()
