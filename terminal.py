class Terminal:
    def __init__(self, id_acc):
        self.id_acc = id_acc
        self.balance = 0
        self.val = "rubles"
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
 
    def withdraw(self, amount):
        if amount <= balance and balance > 0:
            self.balance -= amount
 
    def view(self):
        print(f"ID: {self.id_acc}")
        print(f"Balance: {self.balance}")
 
    def start(self):
        print("Вы авторизованы")
        while True:
            self.view()
            print("1. Пополнить баланс")
            print("2. Снять деньги")
            print("3. Обмен валюты")
            print("4. Выйти")
 
            choice = int(input("Выберите действие:"))
            if choice == 1:
                amount = float(input("Введите сумму для пополнения: "))
                self.deposit(amount)
                print(f"Баланс пополнен на {amount} рублей")
            elif choice == 2:
                amount = float(input("Введите сумму для снятия: "))
                self.withdraw(amount)
                print(f"С баланса было снято {amount} рублей")
            elif choice == 3:
                self.exchange()
            elif choice == 4:
                break
            else:
                print("Неверный выбор, попробуйте еще раз")
 
    def exchange(self):
        sp = ["rubles", "dollars"]
        want = input("На какую валюту вы хотите обменять свои деньги?")
        if want in sp and want != self.val:
            if want == "dollars":
                self.balance /= 80
            elif want == "rubles":
                self.balance *= 80
            self.val = want
        elif want != self.val:
            print("Такой валюты у нас нет")
        else:
            print(f"Счет уже в {self.val}")
 
q = Terminal("2023")
q.start()