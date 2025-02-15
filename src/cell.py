import math
from line import Line
from point import Point


class Cell:

    def __init__(
        self,
        has_left_wall: bool,
        has_top_wall: bool,
        has_right_wall: bool,
        has_bottom_wall: bool,
        point1,
        point2,
        win,
    ) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.point_tl = point1
        self.point_br = point2
        self.point_tr = Point(point2.x, point1.y)
        self.point_bl = Point(point1.x, point2.y)
        self.win = win

    def __repr__(self):
        v = lambda x: "|" if x else " "
        h = lambda x: "--------------" if x else ""
        return f"|{self.point_tl}, {self.point_br}|"
        # return f"         {h(self.has_top_wall)}\n" + \
        #        f"cell ->{v(self.has_left_wall)}[{self.point_tl}, {self.point_tr}]{v(self.has_right_wall)}\n" + \
        #        f"       {v(self.has_left_wall)}[{self.point_bl}, {self.point_br}]{v(self.has_right_wall)}\n" + \
        #        f"         {h(self.has_bottom_wall)}"

    def draw(self, fill_color):
        if self.has_left_wall:
            self.win.draw_line(Line(self.point_tl, self.point_bl), fill_color)
        if self.has_top_wall:
            self.win.draw_line(Line(self.point_tl, self.point_tr), fill_color)
        if self.has_right_wall:
            self.win.draw_line(Line(self.point_tr, self.point_br), fill_color)
        if self.has_bottom_wall:
            self.win.draw_line(Line(self.point_bl, self.point_br), fill_color)

    def find_center(self):
        center_x = (self.point_tl.x - self.point_br.x) // 2
        center_y = (self.point_tl.y - self.point_br.y) // 2
        center_point = self.point_br + Point(center_x, center_y)
        return center_point

    def draw_path(self, to_cell, undo=False):
        if not undo:
            color = "red"
        else:
            color = "gray"
        own_center = self.find_center()
        to_cell_center = to_cell.find_center()
        print(to_cell.point_tl)
        self.win.draw_line(Line(own_center, to_cell_center), color)
