# Block-chain

# Depth-first search
alphabet = "ABCDEFGHIJKLMNOPQRST"
alphabet_dict = {}
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]] = i

def to_letters(chain):
    result = ""
    for n in chain:
        result += alphabet[n]
    return result
def from_letters(chain):
    result = []
    for letter in chain:
        result.append(alphabet_dict[letter])
    return result

def block_chains(chain:list, length:int):
    if(len(chain) == length):
        # print(to_letters(chain), ": Found a block-chain!")
        return 1 # Found a blockchain!
    else:
        min_first = length # First of two adjacent letters, any larger letter after indicates 2-in-a-row
        min_second = length  # Second of two adjacent letters, any larger letter after indicates 3-in-a-row
        for block in chain:
            # Check first number, find lowest
            if(block < min_first):
                min_first = block
            elif(block > min_first):
                # Check second number larger than first, find lowest
                if (block < min_second):
                    min_second = block
                elif (block > min_second):
                    # Third in a row
                    # print(to_letters(chain), ": Three-in-a-row - dead end")
                    return 0
        # print(to_letters(chain), ": Any letter up to", to_letters([min_second]))

        chains = 0
        for i in range(min_second):
            # Third < min_second, to prevent 3-in-a-row
            if(not i in chain):
                # Possible chain
                chains += block_chains(chain + [i], length)
        return chains


chain = from_letters(input("Chain: "))
for i in range(len(chain)):
    chain[i] = int(chain[i])
length = int(input("No. of letters: "))
print("Answer:", block_chains(chain, length))