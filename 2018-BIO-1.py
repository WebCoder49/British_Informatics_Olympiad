# Debt Repayment

# After marking - this
# Keeping numbers as ints simulating fixed-point 2dp numbers

import math

debt = 100_00 # after-point digits as all multiplied by 100
total_repayed = 0

"""def round_up_2dp(number):

    # Multiply by 100, find ceiling, div by 100
    number *= 100

    # Remove small "impurities" which change ceiling
    # number = (number*10000)//10000

    number = math.ceil(number)

    number /= 100

    return number"""


def calc_percent(number, percentage):
    return math.ceil(number*percentage/100) # Remove one of the 100x


interest_percent = int(input("Interest (%): "))
interest = 1_00+interest_percent
repay_percent = int(input("Repayment (%): "))
repay = repay_percent

while(debt > 0):
    debt = calc_percent(debt, interest) # Add interest - remove one of the 100 times to keep as ordinary int

    repayment = calc_percent(debt, repay)

    if(repayment < 50_00):
        repayment = 50_00
    if(repayment >= debt):
        repayment = debt

    debt -= repayment # Repay

    total_repayed += repayment


print(total_repayed/100)