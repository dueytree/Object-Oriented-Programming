# 하나의 클래스로 너무 많은 일을 하지 말고, 딱 한가지 책임만 수행할

class Ship:
    """배 클래스"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        self.fuel_tank = FuelTank(fuel)
        self.crew_manager = CrewManager(num_crew)
        self.supply_hold = SupplyHold(supplies, self.crew_manager)
        self.engine = Engine(self.fuel_tank, fuel_per_hour)


class FuelTank:
    """연료 탱크 클래스"""
    def __init__(self, fuel):
        """연료 탱크에 저장된 연료량을 인스턴스 변수로 갖는다"""
        self.fuel = fuel

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def use_fuel(self, amount):
        """연료 사용 메소드"""
        if self.fuel - amount >= 0:
            self.fuel -= amount
            return True
        print("연료가 부족합니다!")
        return False

    def report_fuel(self):
        """연료량 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다".format(self.fuel))


class Engine:
    """엔진 클래스"""
    def __init__(self, fuel_tank, fuel_per_hour):
        """연료 탱크 인스턴스와 시간당 연료 소비량을 인스턴스 변수로 갖는다"""
        self.fuel_tank = fuel_tank
        self.fuel_per_hour = fuel_per_hour

    def run_for_hours(self, hours):
        """엔진 작동 메소드, 연료 탱크 인스턴스를 사용한다"""
        if self.fuel_tank.use_fuel(self.fuel_per_hour * hours):
            print("엔진을 {}시간 동안 돌립니다!".format(hours))
            return True
        print("연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다")
        return False


class CrewManager:
    """선원 관리 클래스"""
    def __init__(self, num_crew):
        """승선한 선원 수를 인스턴스 변수로 갖는다"""
        self.num_crew = num_crew

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def report_crew(self):
        """선원 수 보고 메소드"""
        print("현재 선원 {}명이 있습니다".format(self.num_crew))


class SupplyHold:
    """물자 창고 클래스"""
    def __init__(self, supplies, crew_manager):
        """물자량과 선원 관리 인스턴스를 인스턴스 변수로 갖는다"""
        self.supplies = supplies
        self.crew_manager = crew_manager

    def load_supplies(self, amount):
        """물자 충전 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드, 각 선원들에게 동일한 양의 물자를 배분한다"""
        if self.supplies >= self.crew_manager.num_crew:
            self.supplies -= self.crew_manager.num_crew
            return True
        print("물자가 부족하기 때문에 배분할 수 없습니다")
        return False

    def report_supplies(self):
        """물자량 보고 메소드"""
        print("현재 물자는 {}명분이 남아 있습니다".format(self.supplies))


ship = Ship(400, 10, 1000, 50)

ship.fuel_tank.load_fuel(10)
ship.supply_hold.load_supplies(10)
ship.crew_manager.load_crew(10)
ship.supply_hold.distribute_supplies_to_crew()
ship.engine.run_for_hours(4)
ship.crew_manager.report_crew()
ship.supply_hold.report_supplies()
ship.crew_manager.report_crew()

# God object 클래스 나누기

class Student:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grades = Grade()

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}" \
              .format(self.name, self.id, self.major, self.grades.get_average_gpa()))


class Grade:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)


younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.grades.add_grade(3.0)
younghoon.grades.add_grade(3.33)
younghoon.grades.add_grade(3.67)
younghoon.grades.add_grade(4.3)

# 학생 성적표
younghoon.print_report_card()