# From 21:10-30: 20min

# Block Palindromes


def num_block_palindromes(word:str,start:int,end:int,level=0):
    # Get num block palindromes w/ word, starting i (included) and end i (not included)
    last_letter = word[end-1]
    result = 1 # Whole word

    print(" " * level, word[start:end])  # -(i-start)-1

    for i in range(start+1, ((start+end)//2)+1): # from len 1 to halfway - finding 2 blocks of equal len
        # print(" "*level, "i", i, word[start:i], word[end-i+start:end], "end letters", last_letter, word[i-1])
        if(last_letter == word[i-1]):
            # Could be block w/ last letter
            if(word[start:i] == word[end-i+start:end]):
                # Block found - check for inside
                result += num_block_palindromes(word, i, end-i+start,level+1)

    return result


word = input()
print(num_block_palindromes(word, 0, len(word))-1) # Don't count 1 block