# Print out each element of the following array on a separate line:

# ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# create var for arr
our_arr = ['Joe', 2, 'Ted', 4.98, 14, 'Sam',
           'void *', '42', 'float', 'pointers', 5006]

# loop thru our arr
for i in range(0, len(our_arr)):
    # print each index in the loop
    print(our_arr[i])
### END OF PART 1 ##
print("""
********
END OF PART 1
********
""")
### PART 2 ###
# Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:
# ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
# For the above input, the expected output is:
# Bob
# Slack
# reddit
# 89
# 101
# alacritty
# (brackets)
# 5
# 375
# 0
# {slice, owned}
# 22
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

arrie = ['Bob', 'Slack', ['reddit', '89', 101, [
    'alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]


def flattenArray(arr):

    # flat_arr = []

    for i in arr:
        # print(i)
        if type(i) is list:
            flattenArray(i)
            # print(i)
        elif type(i) is not list:
            print(i)

    return 'EoFn()'


print(flattenArray(arrie))
