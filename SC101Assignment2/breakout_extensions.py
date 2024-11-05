"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extensions import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.window.add(graphics.score_label)
    graphics.remote_paddle(graphics.paddle)
    graphics.set_ball_velocity()
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while True:
        pause(FRAME_RATE)
        if graphics.start_click:
            graphics.ball.move(dx, dy)
            graphics.remove(graphics.ball)
            dx = graphics.get_dx()   # 判別式後，在做一次
            dy = graphics.get_dy()
            if graphics.ball.height + graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                graphics.start_click = False
                graphics.window.add(graphics.ball)
                if lives == 0:
                    graphics.window.clear()
                    graphics.window.add(graphics.loss_game, x=graphics.window.width/2-graphics.loss_game.width/2,
                                        y=graphics.window.height/2 - graphics.loss_game.height/3-60)
                    graphics.window.add(graphics.loss_game_label,
                                        x=graphics.window.width/2-graphics.loss_game.width/2-25,
                                        y=graphics.window.height/2 + graphics.loss_game.height-45)
                    break
            elif graphics.score == 8100:
                graphics.window.clear()
                graphics.window.add(graphics.win_game, x=graphics.window.width / 2 - graphics.win_game.width / 2,
                                    y=graphics.window.height / 2 - graphics.win_game.height / 2)
                break

    # Add the animation loop here!


if __name__ == '__main__':
    main()
