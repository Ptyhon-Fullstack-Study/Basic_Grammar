class Mul:
    def __init__(self, m):
        self.m = m

    def __call__(self, n):
        return self.m * n


def mul(m):
    def mulitiplier(n):
        return m * n

    return mulitiplier


if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))  # 30 출력
    print(mul5(10))  # 50 출력

    mul7 = mul(7)
    print(mul7(10))
