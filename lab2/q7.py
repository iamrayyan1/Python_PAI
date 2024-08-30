# You have a list of daily temperatures recorded over a month. Write code to:
# • Calculate and print the average temperature for the month.
# • Find and print the highest and lowest temperatures.
# • Sort the temperatures in ascending order.
# • Remove the temperature record for a specific day

# daily temperatures for a month
temperatures = [23, 25, 38, 19, 27, 39, 35, 32, 24, 26, 39, 21,
                35, 27, 29, 31, 33, 30, 28, 34, 32, 29, 27, 34,
                31, 29, 27, 35, 34, 23, 18, 22, 16, 28, 10, 12]

#average temperature
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature for the month: {average_temp:.2f}")

# Find and print the highest and lowest temperatures
highest_temp = max(temperatures)
lowest_temp = min(temperatures)
print(f"Highest temperature: {highest_temp}")
print(f"Lowest temperature: {lowest_temp}")

# Sort the temperatures in ascending order
#temperature.sort() -> another way to sort in ascending
temp_in_ascending = sorted(temperatures)
print(f"Temperatures in ascending order: {temp_in_ascending}")

# Removing the temperature record for a specific day
remove_day = 19
if 0 <= remove_day < len(temperatures):
    temp = temperatures.pop(remove_day)
    print(f"Removed temperature record for day {remove_day + 1}: {temp}")
    print(f"Updated list of temperatures: {temperatures}")
else:
    print(f"Day {remove_day + 1} cannot be removed")
