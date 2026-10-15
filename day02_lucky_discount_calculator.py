"""
Day 2 Mini Project: Simple Lucky Discount Calculator
Concepts used: input(), float(), random module, basic subtraction, f-strings
"""

import random

# Step 1: Take bill amount from the user

bill_amount = float(input("Enter bill amount (Rs.): "))

# Step 2: Generate a random 4-digit bill number

bill_no = random.randint(1000, 9999)

# Step 3: Pick a random flat discount from a list

discount_options = [50, 100, 150, 200]
lucky_discount = random.choice(discount_options)

# Step 4: Calculate final amount to pay
final_bill = bill_amount - lucky_discount

# Step 5: Print the simple receipt

print("\n--- Lucky Receipt ---")
print(f"Bill No  : #{bill_no}")
print(f"Original Bill : Rs. {bill_amount}")
print(f"Lucky Discount : Rs. {lucky_discount}")
print(f"Final Payable  : Rs. {final_bill}")