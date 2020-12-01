"""
One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago.
Each day thereafter, you go out double the number of bills.
How long does it take for the stack of bills to exceed the height of the tower?
Height of the tower: 442 m
"""

bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    # It will execute as long as the expression after the while is true.
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final Height', num_bills * bill_thickness)
