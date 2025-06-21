import random
import matplotlib.pyplot as plt
import pandas as pd

# симуляція кидків
N = 100_000
sums_counter = {i: 0 for i in range(2, 13)}

for _ in range(N):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    sums_counter[total] += 1

# Обчислення ймовірностей
probabilities = {k: round((v / N) * 100, 2) for k, v in sums_counter.items()}

# таблиця результатів
df = pd.DataFrame({
    "Сума": list(sums_counter.keys()),
    "Імовірність (%)": list(probabilities.values()),
    "Частота": [f"{sums_counter[k]}/{N}" for k in sums_counter]
})

print(df.to_string(index=False))

# графік
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), color='skyblue', edgecolor='black')
plt.xlabel("Сума очок")
plt.ylabel("Імовірність (%)")
plt.title("Імовірність сум при киданні двох кубиків (Метод Монте-Карло)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(range(2, 13))
plt.show()
