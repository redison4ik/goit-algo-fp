items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# greedy algorithm
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_cost = 0
    total_calories = 0
    selected = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected, total_cost, total_calories

# Dynamic programming 
def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибору
    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            selected.append(name)
            w -= items[name]["cost"]

    total_cost = sum(items[name]["cost"] for name in selected)
    total_calories = dp[n][budget]
    selected.reverse()

    return selected, total_cost, total_calories

budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("🔹 Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0])
print("Загальна вартість:", greedy_result[1])
print("Загальна калорійність:", greedy_result[2])

print("\n🔸 Динамічне програмування:")
print("Вибрані страви:", dp_result[0])
print("Загальна вартість:", dp_result[1])
print("Загальна калорійність:", dp_result[2])
