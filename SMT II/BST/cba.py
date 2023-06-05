import math

def calculate_mean(data):
    if len(data) == 0:
        return 0
    sum_values = sum(data)
    mean = sum_values / len(data)
    return mean

def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_diff_sum / len(data)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

# Contoh penggunaan
data = [47, 21, 76]
standard_deviation = calculate_standard_deviation(data)
print(f"Standar deviasi: {standard_deviation}")
