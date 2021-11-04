data = list(range(20, 241))

new_data = [num for num in data if num % 20 == 0 or num % 21 == 0]

print(new_data)
