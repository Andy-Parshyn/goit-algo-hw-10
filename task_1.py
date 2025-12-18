import pulp

model = pulp.LpProblem('Maximize_production', pulp.LpMaximize)
lemomade = pulp.LpVariable('Lemonade', lowBound=0,cat='Integer')
juice = pulp.LpVariable('Juice', lowBound=0, cat='Integer')
model += lemomade + juice, 'Total_Products'

# constraints
model += 2 * lemomade + 1 * juice <= 100, 'Water_Constraint'
model += 1 * lemomade <= 50, 'Sugar_Constraint'
model += 1 * lemomade <= 30, 'Lemon_Juice_Constraint'
model += 2 * juice <= 40, 'Puree_Constraint'

model.solve()

print(f'Статус: {pulp.LpStatus[model.status]}')
print("-" * 30)
print(f"Кількість Лимонаду: {lemomade.varValue}")
print(f"Кількість Фруктового соку: {juice.varValue}")
print("-" * 30)
print(f"Всього вироблено продукції: {pulp.value(model.objective)}")