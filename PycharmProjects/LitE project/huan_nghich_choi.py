def main():
    # Bai 1
    print("Bài 1: ")
    bai_1()

def bai_1():
    # Input:
    arr_input = input("Input: ")
    int_list = list(map(int, arr_input.strip("[]").split(",")))

    # Handle Logic
    result = handle_logic_bai_1(int_list)

    # Output
    print("Output:", result)

def handle_logic_bai_1(arr):
    my_set = {}

    for num in arr:
        if num in my_set:
            my_set.remove(num)
        else:
            my_set.add(num)

    for result in my_set:
        return result

# Kiểm tra nếu tệp đang được chạy trực tiếp
if __name__ == "__main__":
    main()