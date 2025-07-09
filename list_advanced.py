students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]

grades = [95, 62, 47, 88, 53]

max_grade = max(grades)
top_student = students[grades.index(max_grade)]

passed_students = [students[i] for i in range(len(grades)) if grades[i] > 60]

failed_count = sum(1 for grade in grades if grade < 60)

print(f"Найвища оцінка: {top_student} ({max_grade})")
print(f"Студенти з оцінкою > 60: {passed_students}")
print(f"Не склали: {failed_count} студент(ів)")


logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]

print("📊 Підрахунок:")
for msg in set(logs):
    print(f"{msg}: {logs.count(msg)}")

error_percent = logs.count("error") / len(logs) * 100
print(f"\n⚠️ Відсоток 'error': {error_percent:.2f}%")


expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]

max_day = max(expenses, key=lambda x: x[1])

total = sum(amount for day, amount in expenses)

over_100_days = [day for day, amount in expenses if amount > 100]

print(f"Найбільші витрати були в {max_day[0]}: {max_day[1]} грн")
print(f"Загальні витрати за тиждень: {total} грн")
print(f"Дні з витратами понад 100 грн: {over_100_days}")


products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]

total_sum = sum(qty * price for name, qty, price in products)

most_expensive = max(products, key=lambda x: x[2])[0]

summary = [f"{name} - {qty * price:.2f} грн" for name, qty, price in products]

print(f"Загальна сума чеку: {total_sum:.2f} грн")
print(f"Найдорожчий товар (за одиницю): {most_expensive}")
print("Список покупок:")


squares = [x**2 for x in range(1, 31) if x % 2 == 0 and x % 4 != 0 and x not in [10, 14, 18]]

print(squares)




 