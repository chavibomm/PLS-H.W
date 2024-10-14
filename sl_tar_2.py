import math
from functools import reduce
import time
from datetime import datetime, timedelta

#1
func1 = lambda x: x / 2 + 2

#1.1
numbers = list(range(10001))  # יצירת רשימה מ-0 עד 10,000
new_list = list(map(func1, numbers))  # החלת פונקציית למבדה על כל איבר

#1.2
sum_new_list = reduce(lambda x, y: x + y, new_list)

#1.3

start_time = time.time()
sum_imperative = 0
for num in new_list:
    sum_imperative += num
imperative_time = time.time() - start_time

start_time = time.time()
sum_functional = reduce(lambda x, y: x + y, new_list)
functional_time = time.time() - start_time

print(imperative_time)#יצא לי 0.0263
print(functional_time)#יצא לי 0.0132

#1.4
total_sum = reduce(lambda x, y: x + y, map(func1, numbers))

#2
numbers = list(range(1, 1001))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # רשימת מספרים זוגיים
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))   # רשימת מספרים אי זוגיים

#2.1
func_for_even = lambda lst: reduce(lambda acc, x: acc + [acc[-1] * x], lst[2:], [lst[0]*lst[1]])
func_for_odd = lambda lst: reduce(lambda acc, x: acc + [func1(sum(acc)) + x], lst[2:], [func1(lst[0])+lst[1]])

#2.2
even_func_list = func_for_even(even_numbers)
odd_func_list = func_for_odd(odd_numbers)

#print(even_func_list)
#print(odd_func_list)

#2.3
sum_even_list=sum(even_func_list)
sum_odd_list=sum(odd_func_list)

#3
def generate_dates(start , num, skip):
     start_date = datetime.strptime(start , "%Y-%m-%d")
     return list(map(lambda x: start_date + timedelta(days=x *  skip), range(num)))

#4
#4.1
def power_function(exponent):
    return lambda base: base ** exponent

#4.2
def power_map(n):
    return  map(lambda exponent: power_function(exponent), range(n))
#4.3
def taylor(x, n):
    return sum((f(x)/math.factorial(i)) for i,f in enumerate(power_map(n+1)))
print(taylor(3, 100))


#5
def task_manager():
    tasks = {}

    def add_task(task_name, status="incomplete"):
        tasks[task_name] = status

    def get_tasks():
        return tasks

    def complete_task(task_name):
        if task_name in tasks:
            tasks[task_name] = "complete"

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }
