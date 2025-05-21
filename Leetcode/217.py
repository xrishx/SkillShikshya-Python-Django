array_list = [1, 2, 3, 4, 5]


def duplicates(array_list):
    seen = set()
    for i in array_list:
        if i in seen:
            return "Duplicates Exists"
        seen.add(i)
    return "Duplicates Dont Exist"

print(duplicates(array_list))