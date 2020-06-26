def list_ends(nums: list) -> list:
    num_list = [nums[0], nums[-1]]
    return num_list


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    res = list_ends(numbers)
    print(res)
