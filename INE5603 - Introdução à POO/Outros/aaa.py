import random

def roll_dice(num_rolls):
    results = []
    for i in range(num_rolls):
        result = random.randint(1, 4)
        results.append(result)
    return results

def calculate_average(results):
    return sum(results) / len(results)

num_experiments = 100
num_rolls = 20
experiment_averages = []
for i in range(num_experiments):
    experiment_results = roll_dice(num_rolls)
    experiment_average = calculate_average(experiment_results)
    experiment_averages.append(experiment_average)
    print("Resultados da rolagem {}: {}".format(i + 1, experiment_results))

final_average = calculate_average(experiment_averages)
print("A média final é:", final_average)
