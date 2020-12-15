from manimlib.imports import *

import random

def CoinFlip(times):
    "Return the number of heads"
    return sum([random.randint(0, 1) for _ in range(times)])

class Introduction(Scene):
  def construct(self):
    text = TextMobject("Montecarlo Integration")
    text.scale(2)

    self.play(Write(text))
    self.wait(3)

    integral = TexMobject(r"\int_{a}^{b}f(x)dx")
    integral.scale(3)

    self.play(Transform(text, integral))
    self.wait(3)

class ToC(Scene):
  def construct(self):
    text = TextMobject("Table of Contents")
    text.scale(2)
    transform_text = TextMobject("Table of Contents")
    transform_text.to_corner(UP + LEFT)
    self.play(FadeInFromDown(text))
    self.wait(2)
    self.play(
      Transform(text, transform_text)
    )
    toc = VGroup(TextMobject("1. Integration"),
                 TextMobject("2. Montecarlo Methods"),
                 TextMobject("3. Examples"),
                 TextMobject("4. Montecarlo Integration"))
    toc.arrange(DOWN, buff=LARGE_BUFF, aligned_edge=LEFT)
    toc.to_edge(DOWN, buff=LARGE_BUFF)

    for element in toc:
      self.play(FadeIn(element, lag_ratio=0.1, run_time=2))

class RiemannRectanglesAnimation(GraphScene):
    CONFIG = {
      "y_max": 8,
      "y_axis_height": 5,
      "init_dx": 0.5,
    }

    def construct(self):
      self.setup_axes()

      def func(x):
        return 0.1 * (x + 3 - 5) * (x - 3 - 5) * (x - 5) + 5

      graph = self.get_graph(func, x_min=0.3, x_max=9.2)
      kwargs = {
        "x_min": 2,
        "x_max": 8,
        "fill_opacity": 0.75,
        "stroke_width": 0.25,
      }
      flat_rectangles = self.get_riemann_rectangles(
        self.get_graph(lambda x: 0),
        dx=self.init_dx,
        start_color=invert_color(PURPLE),
        end_color=invert_color(ORANGE),
        **kwargs
      )
      riemann_rectangles_list = self.get_riemann_rectangles_list(
        graph,
        6,
        max_dx=self.init_dx,
        power_base=2,
        start_color=PURPLE,
        end_color=ORANGE,
        **kwargs
      )
      title = TextMobject("Integration")
      self.play(FadeInFromDown(title), run_time = 2)
      self.wait(3)
      transform_title = TextMobject("Integration")
      transform_title.to_corner(UP + LEFT)
      self.play(
        Transform(title, transform_title)
      )
      self.wait(2)

      self.play(Write(graph), run_time = 5)
      self.wait(3)
      # Show Riemann rectangles
      self.play(ReplacementTransform(flat_rectangles, riemann_rectangles_list[0]))
      self.wait()
      for r in range(1, len(riemann_rectangles_list)):
        self.transform_between_riemann_rects(
          riemann_rectangles_list[r - 1],
          riemann_rectangles_list[r],
          replace_mobject_with_target_in_scene=True,
        )
      self.wait(3)

class Integration_p2(Scene):
  def construct(self):
    title = TextMobject("Integration")
    title.to_corner(UP + LEFT)
    self.add(title)
    #Possible Int
    pos_int = TexMobject(r"\int x^2 dx", r" = \frac{x^3}{3} + C")

    notpos_int = TexMobject(r"\int e^{sin(x)}dx")
  # https://math.stackexchange.com/questions/1625613/integrals-with-no-analytic-answer-intuition-and-proof
    #self.play(Write(pos_int[0], run_time = 2))
    self.play(AnimationGroup(
      Write(pos_int[0], run_time  = 2),
      Write(pos_int[1], run_time = 2),
      lag_ratio  = 5
    ))
    self.wait(2)
    self.wait()
    self.remove(pos_int[0], pos_int[1])
    self.wait()
    self.play(Write(notpos_int, run_time = 2))
    self.wait(1)


#TODO: WHAT IS AN INTEGRAL,
# WHAT IS A MONTECARLO PROCESS,
# WHAT IS A MONTECARLO INTERGAL

class Montecarlo(Scene):
  def construct(self):
    su_img = ImageMobject("./assets/img/ulman.jpg")
    su_img.to_edge(2*LEFT)
    su_img.scale(1.8)
    su_name = TextMobject("Stanislaw Ulam")
    su_name.next_to(su_img, DOWN)
    su_name.scale(0.7)

    jvn_img = ImageMobject("./assets/img/jvn.jpg")
    jvn_img.next_to(su_img, RIGHT, buff = 2)
    jvn_img.scale(1.8)
    jvn_name = TextMobject("John von Neumann")
    jvn_name.next_to(jvn_img, DOWN)
    jvn_name.scale(0.7)

    title = TextMobject("Montecarlo Methods")
    title.scale(2)
    transform_text = TextMobject("Montecarlo Methods")
    transform_text.to_corner(UP + LEFT)

    self.play(FadeIn(title))

    self.play(Transform(title, transform_text, run_time = 1),
              FadeIn(su_img),
              FadeIn(su_name),
              FadeIn(jvn_img, lag_ratio = 1),
              FadeIn(jvn_name, lag_ratio = 1)
              )
    self.wait(2)

    dice = SVGMobject("./assets/img/dice.svg")
    dice.to_edge(RIGHT)
    dice.scale(2)
    #self.play(Write(dice)) This is complicated because of colors
    self.play(FadeIn(dice)) #This is not working
    self.wait(2)


class EstimatePi(GraphScene):

  def construct(self):

    title = TexMobject(r"\text{Estimating } \pi")
    self.play(Write(title.scale(2)))
    title.to_edge(UP + LEFT)
    self.wait()

    self.play(Write(Circle().scale(2)))
    self.play(Write(Square().scale(2)))

    self.wait(1)

    counter = VGroup(TextMobject("Inside: ", color = RED),
                     TextMobject("Outside: ", color = BLUE))
    counter.arrange(RIGHT,
                    aligned_edge=RIGHT,
                    buff=LARGE_BUFF)
    counter.to_edge(LEFT)
    counter[1].next_to(counter[0], DOWN)
    self.play(FadeIn(counter))

    estimate = VGroup(TextMobject("\\pi: ", color=RED),
                     TextMobject("N: ", color=BLUE))
    estimate.arrange(RIGHT,
                    aligned_edge=RIGHT,
                    buff=LARGE_BUFF)
    estimate.to_edge(RIGHT)
    estimate[1].next_to(estimate[0], DOWN)
    self.play(FadeIn(estimate))

    num_points = 200
    red_count = 0
    blue_count = 0
    for point in range(num_points):
        #define coordinates
        x = 2*random.random() if random.random() > 0.5 else -2*random.random()
        y = 2*random.random() if random.random() > 0.5 else -2*random.random()



        #Make color conditional on where it lands
        if x**2 + y**2 > 4.1:
          p = SmallDot([x,y, 0], color = BLUE)
          self.play(
            Transform(TextMobject(str(blue_count), color = BLUE).next_to(counter[1], RIGHT),
                      TextMobject(str(blue_count + 1), color = BLUE).next_to(counter[1], RIGHT)))
          blue_count += 1
        else:
          p = SmallDot([x, y, 0], color=RED)
          self.play(
          Transform(TextMobject(str(red_count), color=RED).next_to(counter[0], RIGHT),
                    TextMobject(str(red_count+1), color=RED).next_to(counter[0], RIGHT)))
          red_count += 1

        #Estimate Pi
        if red_count > 0 and blue_count > 0:
          pi_estimate = red_count/blue_count

        self.play(FadeIn(p))
        self.wait()
    self.wait(7)




# example of montecarlo: https://academo.org/demos/estimating-pi-monte-carlo/
class ShowCode(Scene):
  CONFIG = {
    "code_config":{
      "file_name": "./assets/CoinFlip.py",
      "font": "Input Mono",
      "tab_width": 3,
      "style": "monokai",
      "language": "python"
    }
  }
  def setup(self):
    code = Code(**self.code_config)
    code.set_width(FRAME_WIDTH-1)
    code.move_to(ORIGIN)
    self.play(FadeInFromDown(code), run_time = 5)
    self.wait(5)

class Coin(Scene):

  def construct(self):
    n = NumberLine(
      include_tip = False,
      include_numbers = True,
      x_min = 0,
      x_max = 6,
      x_leftmost_tick = 0
    )
    #self.add(n)

    counter = TextMobject("Number of throws: ", "0")
    counter.to_edge(UP)
    self.play(FadeIn(counter))

    num_dots = 21
    num_flips = 10
    for l in range(num_dots):
      #The position of the falling dots in the screen
      pos = CoinFlip(num_flips) - 5
      dot = Dot(point = [pos, -2, 0])
      self.play(FadeInFrom(dot, [0, 10,0]),
                Transform(counter[1], TextMobject(str(l)).to_edge(UP + RIGHT*9.6)))
    self.wait(5)
    self.step_formula()
class MonteCarloIntegration(GraphScene, ZoomedScene):
  CONFIG = {
    "x_min": -2,
    "x_max": 6,
    "y_min": -4,
    "y_max": 5,
    "default_riemann_start_color": PURPLE,
    "default_riemann_end_color": ORANGE,
  }

  def func(self, x):
     return math.e**math.sin(x)

  def construct(self):
    self.setup_axes(animate = True)
    title = TextMobject("Montecarlo Integration")
    title.to_corner(UP + LEFT)
    self.play(FadeIn(title))

    graph = self.get_graph(self.func)
    graph_l = self.get_graph_label(graph, label = "y = e^{sin(x)}", direction=UP + RIGHT)
    self.play(Write(graph), Write(graph_l.scale(0.7),run_time = 7))
    self.wait(3)

    line1 = self.get_vertical_line_to_graph(1, graph, DashedLine, color=YELLOW)
    line2 = self.get_vertical_line_to_graph(4, graph, DashedLine, color=YELLOW)
    area2 = self.get_area(graph, 1, 4)
    self.play(Write(line1, run_time = 4), Write(line2),
              Write(area2, run_time = 2, lag_ratio = 1))
    self.wait(2)

    #Not sure which one of these should I leave
    self.play(FadeOut(area2))

class MonteCarloIntegrationpt2(GraphScene, ZoomedScene):
  CONFIG = {
    "x_min": -2,
    "x_max": 6,
    "y_min": -4,
    "y_max": 5,
    "default_riemann_start_color": RED,
    "default_riemann_end_color": RED,
    "num_rects": 1,
    "area_opacity": 0.5,
    "x_labeled_nums": [1, 4],
    "zoomed_display_height": 6,
    "zoomed_display_width": 6,
    "zoom_activated": True,
    "zoom_factor": 0.7,
  }
  def func(self, x):
     return math.e**math.sin(x)

  def construct(self):
    self.setup_axes()
    title = TextMobject("Montecarlo Integration")
    title.to_edge(LEFT)
    self.add(title)

    graph = self.get_graph(self.func)
    graph_l = self.get_graph_label(graph, label = "y = e^{sin(x)}", direction=UP + RIGHT)
    self.add(graph)
    self.add(graph_l.scale(0.7))

    line1 = self.get_vertical_line_to_graph(1, graph, DashedLine, color=YELLOW)
    line2 = self.get_vertical_line_to_graph(4, graph, DashedLine, color=YELLOW)

    self.add(line1)
    self.add(line2)

    #Random point to create rectangle
    x_point = random.uniform(1, 4)
    y_point = math.e**math.sin(x_point)
    transform = self.coords_to_point(x_point, y_point)
    point = SmallDot(transform, color=RED)
    line3 = self.get_vertical_line_to_graph(x_point, graph, DashedLine, color=RED)
    self.play(FadeIn(point), Write(line3, run_time = 1))
    self.wait()

    #Draw one rectangle
    #i just neeed the horizontal line and the area of this

    hline = self.get_graph(lambda x: y_point, x_min = 1, x_max=4, color= RED)
    area3 = self.get_area(hline, 1, 4)
    self.play(Write(hline), Write(area3))

    #Add braces
    brace1 = Brace(area3)
    brace_txt1 = brace1.get_text("3")
    brace2 = Brace(area3, direction=RIGHT)
    brace2_txt2 = brace2.get_text(str(round(x_point, 1)))
    initial_txt = VGroup(brace_txt1, brace2_txt2)
    self.play(FadeIn(brace1),
              FadeIn(initial_txt[0].scale(0.7)))
    self.wait(2)
    self.play(FadeIn(brace2),
              FadeIn(initial_txt[1].scale(0.7)))
    self.wait(3)
    # Multiplication
    self.play(FadeOut(brace1), FadeOut(brace2))
    self.wait()
    area_result = round(x_point*3, 2)
    multi = VGroup(brace2_txt2, TexMobject("\\cdot"),
    brace_txt1, TexMobject(r"="), TexMobject(str(area_result)))

    multi.arrange(RIGHT)

    multi.move_to(0.5*RIGHT)

    self.play(FadeIn(multi), run_time = 3)
    self.wait(3)

    #Create another rectangle
    num_rectangles = 10
    for i in range(num_rectangles):
      # Random point to create rectangle
      x_point = random.uniform(1, 4)
      y_point = math.e ** math.sin(x_point)
      transform = self.coords_to_point(x_point, y_point)
      point = SmallDot(transform, color=RED)
      line = self.get_vertical_line_to_graph(x_point, graph, DashedLine, color=RED)
      self.play(FadeIn(point), Write(line3, run_time=1))
      self.wait()

      hline = self.get_graph(lambda x: y_point, x_min=1, x_max=4, color=RED)
      area4 = self.get_area(hline, 1, 4)
      self.play(Write(hline), Write(area4))

    self.wait(2)

class MontecarloPython(Scene):
    CONFIG = {
        "code_config": {
            "file_name": "./assets/montecarlo_integration_code.py",
            "font": "Input Mono",
            "tab_width": 3,
            "style": "monokai",
            "language": "python"
        }
    }

    def setup(self):
        code = Code(**self.code_config)
        code.set_width(FRAME_WIDTH - 1)
        code.move_to(ORIGIN)
        self.play(FadeInFromDown(code), run_time=5)
        self.wait(5)