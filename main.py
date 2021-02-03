def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
    for index in range(2):
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    soundExpression.happy.play_until_done() 
    basic.show_number(randint(1, 6))
input.on_button_pressed(Button.A, on_button_pressed_a)
