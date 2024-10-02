from manim import *

class raycast(Scene):
    def construct(self):
        raycast_color = ManimColor.from_rgb((248, 96, 96))
        red_Rectangle_1 = Rectangle(color=raycast_color, height=0.36, width=3.6, fill_color=raycast_color, fill_opacity=1).shift(1.6*UP)
        red_Rectangle_2 = Rectangle(color=raycast_color, height=0.36, width=3.6, fill_color=raycast_color, fill_opacity=1).shift(0.8*UP)
        red_Rectangle_3 = Rectangle(color=raycast_color, height=0.36, width=3.6, fill_color=raycast_color, fill_opacity=1)
        red_Rectangle_4 = Rectangle(color=raycast_color, height=0.36, width=3.6, fill_color=raycast_color, fill_opacity=1).shift(0.8*DOWN)
        red_Rectangle_5 = Rectangle(color=raycast_color, height=0.36, width=3.6, fill_color=raycast_color, fill_opacity=1).shift(1.6*DOWN)
        Rectangle_shadow = Rectangle(color=BLACK, height=0.36, width=2.7, fill_color=BLACK, fill_opacity=1).shift(0.4*DOWN)
        
        red_square_mini = Square(side_length=1.9, color=raycast_color, fill_color=raycast_color, fill_opacity=1).rotate(PI/4).shift(0.4*DOWN)
        red_square_mini_shadow = Square(side_length=1.88, color=BLACK, fill_color=BLACK, fill_opacity=1).rotate(PI/4).shift(0.4*DOWN)
        dot = Dot(color=raycast_color).shift(2.7*LEFT).scale(0)
        
        self.play(FadeIn(red_Rectangle_1), FadeIn(red_Rectangle_2), FadeIn(red_Rectangle_3), FadeIn(red_Rectangle_4), FadeIn(red_Rectangle_5), FadeIn(Rectangle_shadow), run_time=2)
        self.play(GrowFromPoint(red_square_mini_shadow, ORIGIN), GrowFromPoint(red_square_mini, ORIGIN), run_time=1)
        self.play(red_square_mini.animate.shift(0.2*UP), run_time=0.2)
        self.play(Rectangle_shadow.animate.shift(0.4*UP), red_square_mini.animate.shift(0.4*UP), run_time=0.4)

        group = VGroup(red_Rectangle_1, red_Rectangle_2, red_Rectangle_3, red_Rectangle_4, red_Rectangle_5, Rectangle_shadow, red_square_mini_shadow, red_square_mini)
        self.play(group.animate.rotate(-PI/4).scale(0.7).shift(2.7*LEFT), run_time=1)
        text_raycast = Text("Raycast", font="Aileron").scale(2).shift(2*RIGHT, 1*UP)
        text_japan = Text("Japan", font="Aileron").scale(2).shift(2*RIGHT, 1*DOWN)
        self.play(Write(text_raycast), run_time=0.8)
        self.play(Write(text_japan), run_time=0.8)
        self.wait(2)

        self.play(Transform(group, dot), Unwrite(text_raycast), Unwrite(text_japan), run_time=1)
        self.wait(2)

