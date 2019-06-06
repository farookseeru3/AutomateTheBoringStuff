# Take a list value as an argument and returns a string with all items separated by
# a comma and a space, with and inserted before the last item.
# author: Sooyong Lee


def separate(list):
    string = ''
    for i in range(len(list)-1):
        string = string + list[i] +  ", "
    string = string + "and " + list[-1]
    return string


def test():
    testList = ['apples', 'bananas', 'tofu', 'cats']
    print(separate(testList))


test()




