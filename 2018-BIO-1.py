# Debt Repayment
import math

debt = 100
total_repayed = 0

def round_up_2dp(number):

    # Multiply by 100, find ceiling, div by 100
    number *= 100

    # Remove small "impurities" which change ceiling
    number = (number*100)//100

    number = math.ceil(number)

    number /= 100

    return number

interest_percent = int(input("Interest (%): "))
interest = 1+(interest_percent/100)
repay_percent = int(input("Repayment (%): "))
repay = (repay_percent/100)

while(debt > 0):
    debt = round_up_2dp(debt * interest) # Add interest

    repayment = round_up_2dp(repay * debt)
    print(repayment, debt)

    if(repayment < 50):
        repayment = 50
    if(repayment >= debt):
        repayment = debt

    debt -= repayment # Repay

    total_repayed += repayment


print(round_up_2dp(total_repayed))