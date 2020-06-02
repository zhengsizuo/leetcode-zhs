
def insert(string, char, pos):
    str_list = list(string)
    print(str_list)
    str_list.insert(pos, char)

    return ''.join(str_list)

string = 'horse'
string = string.replace('h', 'r')
string = string[:2] + string[3:]
string = string[:-1]
print(string)
# print(insert(string, 'h', 0))
