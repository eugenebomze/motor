def on_gesture_down():
    servos.P0.set_angle(180)
    basic.pause(1000)
    servos.P0.stop()
grove.on_gesture(GroveGesture.DOWN, on_gesture_down)

def on_gesture_right():
    for index in range(2):
        servos.P0.set_angle(20)
        basic.pause(1000)
        servos.P0.set_angle(180)
        basic.pause(1000)
        servos.P0.stop()
grove.on_gesture(GroveGesture.RIGHT, on_gesture_right)

def on_gesture_up():
    servos.P0.set_angle(20)
    basic.pause(1000)
    servos.P0.stop()
grove.on_gesture(GroveGesture.UP, on_gesture_up)

def on_gesture_left():
    for index2 in range(2):
        servos.P0.set_angle(20)
        basic.pause(1000)
        servos.P0.set_angle(360)
        basic.pause(1000)
        servos.P0.stop()
grove.on_gesture(GroveGesture.LEFT, on_gesture_left)

strip = neopixel.create(DigitalPin.P1, 30, NeoPixelMode.RGB)

def on_forever():
    strip.show_color(Math.map(pins.analog_read_pin(AnalogPin.P2),
            20,
            200,
            neopixel.hsl(44, 100, 70),
            neopixel.hsl(231, 100, 73)))
    strip.set_brightness(255)
    basic.pause(1000)
basic.forever(on_forever)
