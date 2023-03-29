# Lexical Connections

# S>T if, setwise, add 1 letter, remove 1 letter, or replace 1 letter (could be w/ itself)
# Join together w/ connections, and store connected groups (undirected as works in both directions)
# Output num groups and size of largest group

words = input().split()

words = tuple(map(set, words)) # Turn each word into a set

def connected(a:set, b:set):
    """Are words a and b lexically connected?"""
    b = b.copy()
    one_added = False
    one_removed = False
    for letter in a:
        if letter in b:
            # Don't count in reverse direction
            b.remove(letter)
        else: # In a, not b so removed
            if one_removed:
                # One already removed - cannot remove 2
                return False
            one_removed = True
    # Should only have one max char left added to b
    return len(b) <= 1

def fill_groups_return_next_word_i_and_group_size(node_word_i:set, is_in_group:list, next_word_i:int):
    """Traverse from the 'node word', and fill in the is_in_group boolean array in place; return the i for the next word i in a different group, group size"""
    is_in_group[node_word_i] = True

    group_size = 0
    for i in range(len_words):
        if i != node_word_i and is_in_group[i] is False and connected(words[node_word_i], words[i]):
            # Can add to group
            group_size += 1
            if i == next_word_i:
                next_word_i += 1

            # Try to traverse from here
            next_word_i, add_group_size = fill_groups_return_next_word_i_and_group_size(i, is_in_group, next_word_i)
            group_size += add_group_size

    return next_word_i, group_size

len_words = len(words)

is_in_group = [False for _ in range(len_words)] # Boolean array for each word
word_i = 0 # Index to traverse from + find group

max_group_size = 0

num_groups = 0
while word_i < len_words:
    word_i, group_size = fill_groups_return_next_word_i_and_group_size(word_i, is_in_group, word_i+1)
    group_size += 1
    if group_size > max_group_size:
        max_group_size = group_size
    num_groups += 1
    # print(is_in_group, word_i)

print(num_groups, max_group_size)