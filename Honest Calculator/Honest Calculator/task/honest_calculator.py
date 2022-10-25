class HonestCalculator:
    def __init__(self):
        self.data: list = []
        self.operators: list = ["+", "-", "*", "/"]
        self.operand_1: (int, float) = None
        self.operand_2: (int, float) = None
        self.memory: (int, float) = 0

    def start(self) -> None:
        self.read_user_input()
        self.execute_equation()

    def read_user_input(self) -> None:
        self.data = input("Enter an equation\n").split(" ")

    def execute_equation(self) -> None:
        flag: bool = True

        while True:
            if self.check_memory_variable():
                if self.data[1].__eq__("/") and self.operand_2 == 0:
                    self.divide_by_zero()

                    flag = False
                else:
                    self.handle_print_data()
            elif self.check_operands(self.data[0]) and self.check_operands(self.data[2]) and self.check_operator():
                if self.data[1].__eq__("/") and self.operand_2 == 0:
                    self.divide_by_zero()

                    flag = False
                else:
                    self.operand_1 = self.get_operand_type(self.data[0])
                    self.operand_2 = self.get_operand_type(self.data[2])

                    self.handle_print_data()
            else:
                if not self.check_operands(self.data[0]) or not self.check_operands(self.data[2]):
                    print("Do you even know what numbers are? Stay focused!")
                elif not self.check_operator():
                    print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")

            if flag:
                continue_execution = input("Do you want to continue calculations? (y / n):\n")

                if continue_execution.__eq__("y"):
                    self.read_user_input()
                else:
                    break
            else:
                self.read_user_input()

                flag = True

    @staticmethod
    def check_operands(operand: str) -> bool:
        try:
            if "." in operand and isinstance(float(operand), float):
                return True
            if isinstance(int(operand), int):
                return True

            return False
        except ValueError:
            return False

    def check_operator(self) -> bool:
        return self.data[1] in self.operators

    @staticmethod
    def get_operand_type(operand: str) -> (int, float):
        if "." in operand and isinstance(float(operand), float):
            return float(operand)
        if isinstance(int(operand), int):
            return int(operand)

    def print_result(self) -> (int, float):
        self.check()

        match self.data[1]:
            case "+":
                return float(self.operand_1 + self.operand_2)
            case "-":
                return float(self.operand_1 - self.operand_2)
            case "*":
                return float(self.operand_1 * self.operand_2)
            case "/":
                return self.operand_1 / self.operand_2

    def check_memory_variable(self) -> bool:
        if self.data[0].__eq__("M") and self.data[2].__eq__("M"):
            self.operand_1 = self.memory
            self.operand_2 = self.memory

            return True
        elif self.data[0].__eq__("M"):
            self.operand_1 = self.memory
            self.operand_2 = self.get_operand_type(self.data[2])

            return True
        elif self.data[2].__eq__("M"):
            self.operand_1 = self.get_operand_type(self.data[0])
            self.operand_2 = self.memory

            return True
        else:
            return False

    def store_result_in_memory(self, result: (int, float)) -> None:
        store: str = input("Do you want to store the result? (y / n):\n")

        if store.__eq__("y"):
            if self.is_one_digit(result):
                question_1: str = input("Are you sure? It is only one digit! (y / n)\n")

                if question_1.__eq__("y"):
                    question_2: str = input("Don't be silly! It's just one number! Add to the memory? (y / n)\n")

                    if question_2.__eq__("y"):
                        question_3: str = input("Last chance! Do you really want to embarrass yourself? (y / n)\n")

                        if question_3.__eq__("y"):
                            self.memory = result
            else:
                self.memory = result

    def check(self):
        msg: str = ""

        if self.is_one_digit(self.operand_1) and self.is_one_digit(self.operand_2):
            msg += " ... lazy"
        if (self.operand_1 == 1 or self.operand_2 == 1) and self.data[1].__eq__("*"):
            msg += " ... very lazy"
        if (self.operand_1 == 0 or self.operand_2 == 0) and (
                self.data[1].__eq__("*") or self.data[1].__eq__("+") or self.data[1].__eq__("-")):
            msg += " ... very, very lazy"
        if not msg.__eq__(""):
            msg = "You are" + msg

            print(msg)

    @staticmethod
    def is_one_digit(v: (int, float)) -> bool:
        return -10 < v < 10 and float(v).is_integer()

    def divide_by_zero(self):
        self.check()

        print("Yeah... division by zero. Smart move...")

    def handle_print_data(self):
        result: (int, float) = self.print_result()

        print(result)

        self.store_result_in_memory(result)
