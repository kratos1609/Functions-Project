
def most_frequent(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

s=input("Please enter a string\n")

print(most_frequent(s))
