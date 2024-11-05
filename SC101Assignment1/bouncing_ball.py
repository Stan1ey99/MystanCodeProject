"""
File: bouncing_ball
Name: 黃方易
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
can_clicked = False  # 開關機制


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    總之寫一個會撞到下面後開始往上彈的 while true

    """
    global can_clicked
    run = 1  # 次數
    times = 0  # 總次數
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(go)   # 無法關閉功能
    vy = 0  # 下落速率
    while True:  # 運用骰子的方式，做開關
        if can_clicked:
            ball.move(VX, vy)
            vy += GRAVITY  # 下落速率
            run += 1
            if ball.y + ball.height >= window.height:
                if vy >= 0:  # **往下的時候才能反彈
                    vy = -vy*REDUCE  # 反彈的係數
        if ball.x + ball.width >= window.width:
            times += 1
            window.add(ball, x=START_X, y=START_Y)
            can_clicked = False
            vy = 0
        if times == 3:
            break
        pause(DELAY)


def go(mouse):  # 開關可以設在這
    global can_clicked
    can_clicked = True


if __name__ == "__main__":
    main()
