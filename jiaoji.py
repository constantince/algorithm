def find_intersection(origins:list, target:list) -> bool:
    for i in origins:
        if origins[i] in target:
            return True
        else:
            continue
    return False

if __name__ == "__main__":
    result = find_intersection(origins=[1,2,3,4,5,6], target=[6,7,8,9])
    print(result)



