# Digit Words

# 2022-11-07 Marking (1 right, 0 wrong, * bug):
# 1111111111111 24/24

digits = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
index_progress = [0, 0, 0, 0, 0, 0, 0, 0, 0]

word = input().upper()

done = False
for letter in word:
    for i in range(len(digits)):
        if letter == digits[i][index_progress[i]]:
            index_progress[i] += 1 # Next letter satisfied
            if index_progress[i] == len(digits[i]):
                # Only ever one digit contained - end
                print(i+1) # 1-ind
                done = True
                break
    if done: break
else:
    print("NO") # Not found