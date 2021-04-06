from class_test.ColorPoint import ColorPoint
from class_test.Point import Point

p1 = Point(10, 20)
p1.draw() # p1의 포인트를 draw함

p2 = ColorPoint('red', 30, 50)
p2.draw()

print(Point.count_of_instance) # 객체가 2개 생겼으니까 2라고 출력됨. (p1.draw, p2.draw)