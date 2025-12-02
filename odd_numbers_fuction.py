def odd_function (number):
    new_number= []

    for count in number:
        if count % 2 != 0:
            new_number.append(True)
        else:
            new_number.append(False)
    return(new_number)

print(odd_function([1,2,3,7,9]))

def triple (numbers):

    output = []

    for counter in numbers:
        output.append(counter)
        output.append(counter **2)
        output.append(counter **3)

    return (output)

print(triple([2,3,4]))
