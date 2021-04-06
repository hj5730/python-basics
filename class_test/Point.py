class Point:
    count_of_instance = 0  # 객체의 개수 세기 위해서

    def __init__(self, x, y): # 클래스 생성. (self를 제외한 인자가 def 아래에 반드시 나와야 함)
        Point.count_of_instance += 1
        self.x = x
        self.y = y

    def draw(self):
        print(f'x={self.x}, y={self.y} 에 점을 그렸습니다.') # 객채에 있는 것을 써야하므로 self.x, self.y