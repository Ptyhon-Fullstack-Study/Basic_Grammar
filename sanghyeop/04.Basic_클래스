
# Class
# Class란 똑같이 무언가를 계속 만들어 낼 수 있는 도면 (과자 틀 같은것)
print()

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator() # 여기서 cal1,cal2를 객채라고 한다. (과자임)
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


# example
print()
class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
     def div(self):
         result = self.first / self.second
         return result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
answer=a.add()
print(answer)


# 생성자(constructor)란 객체가 생성될 때 자동으로 호출되는 메서드 활용 (__init__)
print()
class FourCal:
     def __init__(self, first, second):
         self.first = first
         self.second = second
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
     def div(self):
         result = self.first / self.second
         return result



a = FourCal(4, 2)
print(a.first)
print(a.div())



# Class의 상속
class MoreFourCal(FourCal):  # 상속의 문법은 이렇게
     def pow(self):
         result = self.first ** self.second
         return result

a = MoreFourCal(4, 2)
print(a.pow())
print(a.add()) # 원래 class의 기능은 그대로 사용가능

















