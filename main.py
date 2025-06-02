from src.ahp import AHP

criteria = ['Security', 'Performance', 'Usability', 'Maintainability']
pairwise_matrix = [
    [1,     3,     5,     7],
    [1/3,   1,     3,     5],
    [1/5, 1/3,     1,     3],
    [1/7, 1/5, 1/3,     1]
]

model = AHP(criteria, pairwise_matrix)

print("🔹 Normalized Matrix:")
print(model.normalize_matrix(), '\n')

print("🔹 Priority Vector:")
print(model.calculate_priority_vector(), '\n')

print("🔹 Consistency Check:")
print(model.consistency_ratio())
