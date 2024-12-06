from collections import OrderedDict
def first_non_repeating_char(string):
    my_dict = OrderedDict()
    for ch in string:
        my_dict[ch] = string.count(ch) 
    for key in my_dict:
        if my_dict[key] == 1:
            return key
    return None

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )
