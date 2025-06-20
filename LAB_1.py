# Завдання 1: Робота з текстом
def count_words(text):
    words = text.lower().split()  
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1  
        else:
            word_count[word] = 1   

    
    frequent_words = [word for word, count in word_count.items() if count > 3]

    print("Словник частот:", word_count)
    print("Слова, що зустрічаються більше 3 разів:", frequent_words)
    return word_count


text_input = "хліб молоко хліб хліб молоко зефір хліб молоко зефір молоко молоко"
count_words(text_input)


# Завдання 2: Інвентаризація продуктів
inventory = {
    "хліб": 10,
    "зефір": 3,
    "молоко": 7
}

def update_inventory(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

    # Якщо кількість стає менше 0, обнуляємо
    if inventory[product] < 0:
        inventory[product] = 0

    print(f"Оновлений склад: {inventory}")

# Список продуктів, де кількість менше ніж 5
def low_stock():
    low_list = [product for product, count in inventory.items() if count < 5]
    print("Мало на складі:", low_list)
    return low_list

# Приклад використання:
update_inventory("зефір", -1)
update_inventory("кавун", 4)
low_stock()


# Завдання 3: Статистика продажів
sales = [
    {"продукт": "хліб", "кількість": 20, "ціна": 30},
    {"продукт": "молоко", "кількість": 15, "ціна": 40},
    {"продукт": "хліб", "кількість": 10, "ціна": 30},
    {"продукт": "зефір", "кількість": 5, "ціна": 20},
    {"продукт": "молоко", "кількість": 20, "ціна": 40},
]

def calculate_revenue(sales_list):
    revenue = {}
    for sale in sales_list:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        if product in revenue:
            revenue[product] += total
        else:
            revenue[product] = total

    
    profitable = [prod for prod, amount in revenue.items() if amount > 1000]

    print("Загальний дохід:", revenue)
    print("Продукти з доходом > 1000:", profitable)
    return revenue


calculate_revenue(sales)


# Завдання 4: Система управління задачами
tasks = {
    "Написати курсову": "очікує",
    "Приготувати вечерю": "в процесі",
    "Піти в магазин": "виконано"
}

def add_task(name, status):
    tasks[name] = status
    print(f"Задача '{name}' додана зі статусом '{status}'.")

def remove_task(name):
    if name in tasks:
        del tasks[name]
        print(f"Задача '{name}' видалена.")
    else:
        print("Задача не знайдена.")

def change_status(name, new_status):
    if name in tasks:
        tasks[name] = new_status
        print(f"Статус задачі '{name}' змінено на '{new_status}'.")
    else:
        print("Задача не знайдена.")

def waiting_tasks():
    waiting = [name for name, status in tasks.items() if status == "очікує"]
    print("Задачі в статусі 'очікує':", waiting)
    return waiting


add_task("Помити посуд", "очікує")
change_status("Приготувати вечерю", "виконано")
remove_task("Піти в магазин")
waiting_tasks()


# Завдання 5: Аутентифікація користувачів
import hashlib

users = {
    "danylo": {
        "password": hashlib.md5("pass111".encode()).hexdigest(),
        "name": "Ромащенко Данило Валерійович"
    },
    "kyrylo": {
        "password": hashlib.md5("krl123".encode()).hexdigest(),
        "name": "Ключко Кирило Дмитрович"
    }
}

def check_password(login):
    if login not in users:
        print("Користувача не знайдено.")
        return False

    password_input = input("Введіть пароль: ")
    password_hash = hashlib.md5(password_input.encode()).hexdigest()

    if users[login]["password"] == password_hash:
        print("Аутентифікація пройшла успішно!")
        return True
    else:
        print("Невірний пароль.")
        return False


check_password("danylo")  

