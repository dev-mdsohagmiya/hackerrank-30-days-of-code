
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#



def product_price(meal_cost,tip_percent,tax_percent):

    tip_percent = (meal_cost /100)*tip_percent
    tax_percent = (meal_cost /100)*tax_percent

    # split 
    return round(meal_cost+tip_percent+tax_percent)




meal_cost = float(input(""))

tip_percent = float(input(""))

tax_percent = float(input(""))

print(product_price(meal_cost,tip_percent,tax_percent))