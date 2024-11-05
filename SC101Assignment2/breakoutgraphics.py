"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
count = 0              # Count of the brick
# score = 0
# score_label = GLabel('Score: '+str(score))


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        # self.remote_paddle = GRect(paddle_width, paddle_height)
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width/2 - paddle_width/2,
                            y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2 - ball_radius, y=window_height/2 + ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        self.count = 0
        # self.score = 0
        # self.score_label = GLabel('Score: '+str(score), y=window_height)
        # self.score_label.font = '-20'
        # self.window.add(score_label)
        # self.win_game = GImage('win_game.png')          # 補充贏的照片
        # self.loss_game = GImage('loss_game.png')        # 補充失敗的照片
        self.__dx = 0
        self.__dy = 0
        self.start_click = False

        # Create the score

        # self.reset_ball()
        onmouseclicked(self.go)  # 遊戲開始
        onmousemoved(self.remote_paddle)  # 要寫出怎麼移動板子，板子動不了
        # Draw bricks
        for i in range(brick_rows+1):
            self.bricks = GRect(brick_width, brick_height, x=brick_spacing*(i-1)+brick_width*(i-1), y=brick_offset)
            self.bricks.filled = True
            self.bricks.fill_color = 'red'
            self.window.add(self.bricks)
            for j in range(brick_cols+1):
                self.bricks = GRect(brick_width, brick_height, x=brick_spacing*(i-1)+brick_width*(i-1),
                                    y=brick_spacing*(j-1)+brick_height*(j-1)+brick_offset)
                self.bricks.filled = True
                if j <= 2:
                    self.bricks.fill_color = 'red'
                elif j <= 4:
                    self.bricks.fill_color = 'orange'
                elif j <= 6:
                    self.bricks.fill_color = 'yellow'
                elif j <= 8:
                    self.bricks.fill_color = 'green'
                else:
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks)

    def remote_paddle(self, mouse):   # 目標完成只移動板子
        if mouse.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width
        elif mouse.x <= self.paddle.width/2:
            self.paddle.x = mouse.x
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    def go(self, mouse):
        self.start_click = True

    def set_ball_position(self):
        self.ball.x = self.window.width/2 - self.ball.width/2
        self.ball.y = self.window.height/2 + self.ball.height/2
        self.ball.filled = True
        self.window.add(self.ball)

    def reset_ball(self):
        self.set_ball_velocity()
        self.window.add(self.ball, x=self.window.width / 2 - self.ball.width/2,
                        y=self.window.height / 2 + self.ball.height/2)

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        # if random.random() > 0.5:
        #     self.__dy = -self.__dy

    def get_dx(self):   # 為了讓user 可以使用
        return self.__dx

    def get_dy(self):   # 為了讓user 可以使用
        return self.__dy

    def remove(self, event):
        """
        :param event: 主要是判別是否碰到物件，並做反彈機制，補充的是加上成績
        :return:
        """
        obj = self.window.get_object_at(event.x, event.y)
        if obj == self.paddle:
            self.__dy = -self.__dy
        if obj is not None and obj is not self.paddle:
            if self.ball.x == event.x and self.ball.y == event.y:
                self.window.remove(obj)
                self.__dy = -self.__dy
                self.count += 1
                # self.score += 100
                # self.score_label.text = 'Score: ' + str(self.score)
            elif self.ball.width + self.ball.x == event.x and self.ball.y == event.y:
                self.window.remove(obj)
                self.__dy = -self.__dy
                self.count += 1
                # self.score += 100
                # self.score_label.text = 'Score: ' + str(self.score)
            elif self.ball.x == event.x and self.ball.y + self.ball.height == event.y:
                self.window.remove(obj)
                self.__dy = -self.__dy
                self.count += 1
                # self.score += 100
                # self.score_label.text = 'Score: ' + str(self.score)
            elif self.ball.width + self.ball.x == event.x and self.ball.y + self.ball.height == event.y:
                self.window.remove(obj)
                self.__dy = -self.__dy
                self.count += 1
                # self.score += 100
                # self.score_label.text = 'Score: ' + str(self.score)
        if self.ball.x <= 0 or self.ball.width + self.ball.x >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            if self.ball.y + 5 < 0: # windows 系統有多"工具列" 故 +5
                self.__dy = -self.__dy




