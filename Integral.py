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
    toc = VGroup(TextMobject("1. Montecarlo Methods"),
                 TextMobject("2. Law of Large Numbers"),
                 TextMobject("3. Integration"),
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
  CONFIG = {
    "x_min": -3.0,
    "x_max": 3.0,
    "y_min": 0,
    "y_max": 1.0,
    "num_rects": 400,
    "y_axis_label": "",
    "x_axis_label": "",
    "variable_point_label": "a",
    "graph_origin": ORIGIN,
    "x_axis_width": 5,
    "y_axis_height": 5
  }
  def func(self, t):
    return [math.sin(t), math.cos(t), 0]

  def construct(self):
    self.setup_axes()
    f = self.get_graph(lambda x: x**2)

    circle = ParametricFunction(self.func, t_min = 0, t_max = 2*PI)

    self.play(Write(circle), run_time = 2)
    #self.play(Write(Circle()))
    num_points = 24
    for point in range(num_points):
        x = random.random() if random.random() > 0.5 else -random.random()
        y = random.random() if random.random() > 0.5 else -random.random()
        p = Dot([x,y, 0], color = RED)
        self.play(FadeIn(p))
        self.wait()
    #example = Dot([0.1, 0.2, 0])
    #self.play(Write(example), run_time=2)
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

class NormalDistribution(GraphScene):
  CONFIG = {
    "x_min": -2,
    "x_max": 6,
    "y_min": -4,
    "y_max": 10
  }
  def construct(self):
    fun = FunctionGraph(lambda x: (1/1*math.sqrt(2*math.pi))*math.e**(-1/2*((x-0)/1)**2))
    #def fun(x):
    #  return (1/1*math.sqrt(2*math.pi))*math.e**(-1/2*((x-0)/1)**2)

    graph = self.get_graph(fun, x_min=0.3, x_max=9.2)
    label_graph = self.get_graph_label(fun, label = "y = f(x)")
    self.play(Write(fun), Write(label_graph), run_time=7)
    self.wait(5)
