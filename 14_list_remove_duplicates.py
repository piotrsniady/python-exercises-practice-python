def list_remove_duplicates(nums: list) -> set:
    new_nums = set(nums)
    return new_nums


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 1, 2, 3, 4]
    res = list_remove_duplicates(num_list)
    print(res)
