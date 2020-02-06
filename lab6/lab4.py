import arcade

SCREEN_WIDTH = 740 
SCREEN_HEIGHT = 500


def draw_soccer_field():
    #outline of soccer field (bigger yellow box)

    arcade.draw_lrtb_rectangle_filled(
        15, 725, 485, 15, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        20, 720, 480, 20, arcade.color.FOREST_GREEN
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     20, 720, 445.5, 443.5, arcade.color.WHITE
    # )
    # arcade.draw_lrtb_rectangle_filled(
    #     20, 720, 59.5, 57.5, arcade.color.WHITE
    # )
    arcade.draw_lrtb_rectangle_filled(
        368.5, 372.5, 485, 15, arcade.color.YELLOW
    )

    draw_left_yellow_box()
    draw_left_goal_box()
    draw_right_yellow_box()
    draw_right_goal_box()
    draw_left_center_line()
    draw_middle_circle()

def draw_left_center_line():
    #yellow center-line

    arcade.draw_lrtb_rectangle_filled(
        365, 375, 399, 106, arcade.color.YELLOW
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     368.5, 372.5, 399, 106, arcade.color.WHITE
    # )


def draw_middle_circle():
    # middle circle

    arcade.draw_circle_outline(
        369.5, 252.5, 57.5, arcade.color.YELLOW, 5
    )

def draw_left_yellow_box():
    #left yellow box

    arcade.draw_lrtb_rectangle_filled(
        15, 123, 378.5, 126.5, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        15, 118, 373.5, 131.5, arcade.color.FOREST_GREEN
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     15, 20, 399, 106, arcade.color.WHITE
    # )
    # arcade.draw_lrtb_rectangle_filled(
    #     102.5, 105, 399, 106, arcade.color.WHITE
    # )

def draw_right_yellow_box():
    #right yellow box

    arcade.draw_lrtb_rectangle_filled(
        617, 725, 378.5, 126.5, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        622, 725, 373.5, 131.5, arcade.color.FOREST_GREEN
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     720, 725, 399, 106, arcade.color.WHITE
    # )
    # arcade.draw_lrtb_rectangle_filled(
    #     637.5, 640, 399, 106, arcade.color.WHITE
    # )

def draw_left_goal_box():
    #left goal box (smaller yellow box)

    arcade.draw_lrtb_rectangle_filled(
        20, 61, 317.5, 185, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        20, 56, 312.5, 190, arcade.color.FOREST_GREEN
    )

def draw_right_goal_box():
    #right goal box (smaller yellow box)

    arcade.draw_lrtb_rectangle_filled(
        679, 720, 317.5, 185, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        684, 720, 312.5, 190, arcade.color.FOREST_GREEN
    )

def draw_football_field():
    # sideline and yard markers of football field in 10 yard
    # increments

    arcade.draw_lrtb_rectangle_filled(
        15, 725, 409, 97, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        223, 520, 423, 82, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        222.5, 225, 480, 20, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        517.5, 520, 480, 20, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        20, 720, 399, 106, arcade.color.FOREST_GREEN
    )
    arcade.draw_lrtb_rectangle_filled(
        15, 20, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        102.5, 105, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        130, 135, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        162.5, 165, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        190, 195, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        222.5, 225, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        250, 255, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        282.5, 285, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        310, 315, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        342.5, 345, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        368.5, 372.5, 404, 101, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        400, 402.5, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        425, 430, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        457.5, 460, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        485, 490, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        517.5, 520, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        545, 550, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        577.5, 580, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        605, 610, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        637.5, 640, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        70, 75, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        665, 670, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        720, 725, 399, 106, arcade.color.WHITE
    )

def draw_defense(x):
    """Draw the defense"""
    #defense (represented as "x")
    #defensive line 
    arcade.draw_text(
        "x",
        438 + x, 250, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        438 + x, 290, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        438 + x, 210, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    #linebackers
    arcade.draw_text(
        "x",
        408 + x, 225, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        408 + x, 275, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        420 + x, 320, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        420 + x, 180, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    #cornerbacks
    arcade.draw_text(
        "x",
        428 + x, 140, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        428 + x, 370, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    #safeties
    arcade.draw_text(
        "x",
        380 + x, 215, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        380 + x, 285, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_offense(x):
    """Draw the offense"""
    #offense (represented as "o")
    #offensive linemen 
    arcade.draw_text(
        "o",
        455 + x, 250, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        458.75 + x, 270, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        462 + x, 290, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        458.75 + x, 230, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        462 + x, 210, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        462 + x, 190, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    #Quarterback
    arcade.draw_text(
        "o",
        490 + x, 250, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    #Running backs
    arcade.draw_text(
        "o",
        495 + x, 270, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        495 + x, 230, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    #Wide Recievers
    arcade.draw_text(
        "o",
        473 + x, 140, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        462 + x, 370, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

positions = {
    'offense': {
        'x': 0,
        'y': 0,
    },
    'defense': {
        'x': 0,
        'y': 0,
        'speed': 5,
    },
}

def on_draw(delta_time):
    # Modify the defense x
    x = positions['defense']['x']
    if x <= -300:
        positions['defense']['speed'] *= -1
    if x >= SCREEN_WIDTH - 400:
        positions['defense']['speed'] *= -1
    x -= positions['defense']['speed']
    positions['defense']['x'] = x
    
    arcade.start_render()

    # draw_soccer_field()
    draw_football_field()
    draw_offense(positions['offense']['x'])
    draw_defense(positions['defense']['x'])

def main():
    """Draw the field"""
    arcade.open_window(740, 500, "Drawing Example")

    arcade.set_background_color(arcade.color.GRAY)

    arcade.schedule(on_draw, 1/60)

    arcade.run()
    


if __name__ == '__main__':
    main()

