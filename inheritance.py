# Delivery_Man
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class DeliveryMan(Employee):
    """배달원 클래스"""

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name


taeho = DeliveryMan("성태호", 7000, True)

taeho.raise_pay()
print(taeho.wage)

taeho.deliver("서울시 코드잇로 51 최고 건물 401호")
taeho.deliver("서울시 코드잇로 51 최고 건물 402호")

taeho.back()
taeho.deliver("서울시 코드잇로 51 최고 건물 402호")

print(taeho)

print(DeliveryMan.mro())

# Savings_Account

class BankAccount:
    # 코드를 쓰세요
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return "{}님의 계좌 예치금은 {}원입니다.".format(self.name, self.balance)


class CheckingAccount(BankAccount):
    # 코드를 쓰세요
    def __init__(self, name, balance, max_spending):
        super().__init__(name, balance)
        self.max_spending = max_spending

    def use_check_card(self, amount):
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))

    def __str__(self):
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)


class SavingsAccount(BankAccount):
    # 코드를 쓰세요
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance *= (1 + self.interest_rate)

    def __str__(self):
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)


bank_account_1 = CheckingAccount("성태호", 100000, 10000)
bank_account_2 = SavingsAccount("강영훈", 20000, 0.05)

bank_account_1.withdraw(1000)
bank_account_1.deposit(1000)
bank_account_1.use_check_card(2000)

bank_account_2.withdraw(1000)
bank_account_2.deposit(1000)
bank_account_2.add_interest()

print(bank_account_1)
print(bank_account_2)

print(CheckingAccount.mro())
print(SavingsAccount.mro())
