def sort_by_age(person_list):
    sorted_list = sorted(person_list, key=lambda x: x[1])
    return sorted_list