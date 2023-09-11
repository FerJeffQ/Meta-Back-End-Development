# The below script will ask for 3 inputs. Each input will be based
# 1- the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modify the line below
coffee = round(float(input('1 coffee @: $ ')),2)

# Modify the line below
sandwich = round(float(input('1 sandwich @: $ ')),2)

# Modify the line below
cake = round(float(input('1 cake @: $ ')),2)

bill_total = round(coffee + sandwich + cake,2)

print('Your total bill is $', bill_total)