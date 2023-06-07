class BoundingRectangle:

  def __init__(self):
    self.coord_bottom_y = float('inf')
    self.coord_top_y = -float('inf')
    self.coord_left_x = float('inf')
    self.coord_right_x = -float('inf')
    self.w = 0
    self.h = 0

  def add_point(self, x, y):
    self.coord_left_x = min(self.coord_left_x, x)
    self.coord_right_x = max(self.coord_right_x, x)
    self.w = abs(self.coord_left_x - self.coord_right_x)
    self.coord_bottom_y = min(self.coord_bottom_y, y)
    self.coord_top_y = max(self.coord_top_y, y)
    self.h = abs(self.coord_bottom_y - self.coord_top_y)

  def width(self):
    return self.w

  def height(self):
    return self.h

  def bottom_y(self):
    return self.coord_bottom_y

  def top_y(self):
    return self.coord_top_y

  def left_x(self):
    return self.coord_left_x

  def right_x(self):
    return self.coord_right_x


rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print()