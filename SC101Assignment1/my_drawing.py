"""
File: USAGI
Name: 黃方易
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc
from campy.graphics.gwindow import GWindow
window = GWindow(width=500, height=800, title="U SA GI")


def main():
    """
    Title: USAGI

    This is popular cartoon, and USAGI is my favorite character.

    """
    # 背景圖
    background = GRect(500, 800)
    background.filled = True
    background.fill_color = 'orange'
    window.add(background)
    # 名字
    name_label = GLabel("U S A G I")
    name_label.font = 'Courier-30-italic'
    window.add(name_label, x=window.width/2 - 90, y=name_label.height + 100)
    # 腳
    l_leg = GOval(30, 70)
    l_leg.filled = True
    l_leg.fill_color = 'cornsilk'
    window.add(l_leg, x=window.width / 2-30, y=window.height / 2 + 300)
    r_leg = GOval(30, 70)
    r_leg.filled = True
    r_leg.fill_color = 'cornsilk'
    window.add(r_leg, x=window.width / 2, y=window.height / 2 + 300)
    # 身體
    body = GOval(250, 250)
    body.filled = True
    body.fill_color = 'cornsilk'
    window.add(body, x=window.width / 2 - 125, y=window.height / 2 + 100)
    # 手
    l_hand = GOval(70, 30)
    l_hand.filled = True
    l_hand.fill_color = 'cornsilk'
    window.add(l_hand, x=window.width / 2-90, y=window.height / 2 + 200)
    r_hand = GOval(70, 30)
    r_hand.filled = True
    r_hand.fill_color = 'cornsilk'
    window.add(r_hand, x=window.width / 2 + 30, y=window.height / 2 + 200)
    # 遮住手的正方形
    l_hand = GRect(30, 30)
    l_hand.filled = True
    l_hand.fill_color = 'cornsilk'
    l_hand.color = 'cornsilk'
    window.add(l_hand, x=window.width / 2 - 90, y=window.height / 2 + 200)
    r_hand = GOval(30, 30)
    r_hand.filled = True
    r_hand.fill_color = 'cornsilk'
    r_hand.color = 'cornsilk'
    window.add(r_hand, x=window.width / 2 + 70, y=window.height / 2 + 200)
    # 左右耳朵
    l_ear = GOval(50, 200)
    l_ear.filled = True
    l_ear.fill_color = 'cornsilk'
    window.add(l_ear, x=window.width / 2-50, y=l_ear.height-20)
    r_ear = GOval(50, 200)
    r_ear.filled = True
    r_ear.fill_color = 'cornsilk'
    window.add(r_ear, x=window.width / 2, y=l_ear.height-20)
    # 左右小耳朵
    l_ear = GOval(30, 100)
    l_ear.filled = True
    l_ear.fill_color = 'pink'
    window.add(l_ear, x=window.width / 2-28, y=l_ear.height+100)
    r_ear = GOval(30, 100)
    r_ear.filled = True
    r_ear.fill_color = 'pink'
    window.add(r_ear, x=window.width / 2+24, y=l_ear.height+105)
    # 臉
    face = GOval(300, 300)
    face.filled = True
    face.fill_color = 'cornsilk'
    window.add(face, x=window.width/2 - 150, y=name_label.height + 250)
    face_d = GRect(200, 40)
    face_d.filled = True
    face_d.color = 'cornsilk'
    face_d.fill_color = 'cornsilk'
    window.add(face_d, x=window.width / 2-100, y=window.height/2+150)
    # 遮住腳的
    leg_d = GOval(80, 40)
    leg_d.filled = True
    leg_d.color = 'cornsilk'
    leg_d.fill_color = 'cornsilk'
    window.add(leg_d, x=window.width / 2 - 40, y=window.height / 2 + 312)
    # 改成用眉毛
    l_ear_l = GArc(300, 180, -10, 80)
    window.add(l_ear_l, x=window.width/2-30, y=window.height/2-70)
    l_ear_r = GArc(150, 180, 190, -110)
    window.add(l_ear_r, x=window.width/2-70, y=window.height/2-70)
    # 左右眼
    l_eye = GOval(30, 30)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye, x=window.width/2-40, y=window.height/2-40)
    l_eye_w = GOval(15, 15)
    l_eye_w.filled = True
    l_eye_w.fill_color = 'white'
    window.add(l_eye_w, x=window.width / 2 - 30, y=window.height / 2 - 35)
    r_eye = GOval(30, 30)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye, x=window.width/2+20, y=window.height/2-40)
    r_eye_w = GOval(15, 15)
    r_eye_w.filled = True
    r_eye_w.fill_color = 'white'
    window.add(r_eye_w, x=window.width / 2 + 30, y=window.height / 2 - 35)
    # 腮紅
    l_rouge = GOval(60, 30)
    l_rouge.filled = True
    l_rouge.fill_color = 'pink'
    window.add(l_rouge, x=window.width / 2 - 100, y=window.height/2+20)
    r_rouge = GOval(60, 30)
    r_rouge.filled = True
    r_rouge.fill_color = 'pink'
    window.add(r_rouge, x=window.width / 2+50, y=window.height/2+20)
    # 腮紅的線條
    l_rouge_line1 = GRect(2, 15)
    l_rouge_line1.filled = True
    window.add(l_rouge_line1, x=window.width / 2-85, y=window.height/2+25)
    l_rouge_line2 = GRect(2, 15)
    l_rouge_line2.filled = True
    window.add(l_rouge_line2, x=window.width / 2-70, y=window.height/2+25)
    l_rouge_line3 = GRect(2, 15)
    l_rouge_line3.filled = True
    window.add(l_rouge_line3, x=window.width / 2-55, y=window.height/2+25)
    r_rouge_line1 = GRect(2, 15)
    r_rouge_line1.filled = True
    window.add(r_rouge_line1, x=window.width/2+65, y=window.height/2+25)
    r_rouge_line2 = GRect(2, 15)
    r_rouge_line2.filled = True
    window.add(r_rouge_line2, x=window.width / 2+80, y=window.height/2+25)
    r_rouge_line3 = GRect(2, 15)
    r_rouge_line3.filled = True
    window.add(r_rouge_line3, x=window.width / 2+95, y=window.height/2+25)
    # 嘴巴
    mouth = GOval(30, 60)
    mouth.filled = True
    mouth.fill_color = 'pink'
    window.add(mouth, x=window.width / 2 - 10, y=window.height/2+40)
    mouth_l = GOval(30, 60)
    mouth_l.filled = True
    mouth_l.fill_color = 'cornsilk'
    window.add(mouth_l, x=window.width / 2-20, y=window.height / 2 + 20)
    mouth_r = GOval(30, 60)
    mouth_r.filled = True
    mouth_r.fill_color = 'cornsilk'
    window.add(mouth_r, x=window.width / 2, y=window.height / 2 + 20)
    mouth_u = GRect(60, 50)
    mouth_u.filled = True
    mouth_u.fill_color = 'cornsilk'
    mouth_u.color = 'cornsilk'
    window.add(mouth_u, x=window.width / 2-20, y=window.height / 2+20)


if __name__ == '__main__':
    main()
