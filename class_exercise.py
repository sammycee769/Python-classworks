list_one = [1, 2, 3, 4, 5]
list_words = ["hello", "world", "python"]

def sum_of_list(input_list):
    total = 0
    for number in input_list:
        total += number
    return total

def length_of_list(input_list):
    count = 0
    for item in input_list:
        count += 1
    return count

def print_odd_indexed_elements(input_list):
    for index in range(1, length_of_list(input_list), 2):
        print(input_list[index])

def length_of_each_string(input_list):
    lengths = []
    for string in input_list:
        lengths.append(length_of_list(string))
    return lengths

def sort_words(input_list):
    return sorted(input_list)

def enumerate_words(input_list):
    for index, word in enumerate(sort_words(input_list)):
        print(f"Index: {index}, Word: {word}")

print(sum_of_list(list_one))
print(length_of_list(list_words))
print_odd_indexed_elements(list_one)
print(length_of_each_string(list_words))
print(sort_words(list_words))
print(enumerate_words(list_words))