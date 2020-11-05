grove.onGesture(GroveGesture.Down, function () {
    servos.P0.setAngle(180)
    basic.pause(1000)
    servos.P0.stop()
})
grove.onGesture(GroveGesture.Right, function () {
    for (let index = 0; index < 2; index++) {
        servos.P0.setAngle(20)
        basic.pause(1000)
        servos.P0.setAngle(180)
        basic.pause(1000)
        servos.P0.stop()
    }
})
grove.onGesture(GroveGesture.Up, function () {
    servos.P0.setAngle(20)
    basic.pause(1000)
    servos.P0.stop()
})
grove.onGesture(GroveGesture.Left, function () {
    for (let index = 0; index < 2; index++) {
        servos.P0.setAngle(20)
        basic.pause(1000)
        servos.P0.setAngle(360)
        basic.pause(1000)
        servos.P0.stop()
    }
})
let strip = neopixel.create(DigitalPin.P1, 30, NeoPixelMode.RGB)
basic.forever(function () {
    strip.showColor(Math.map(pins.analogReadPin(AnalogPin.P2), 20, 200, neopixel.hsl(44, 100, 70), neopixel.hsl(231, 100, 73)))
    strip.setBrightness(255)
    basic.pause(1000)
})
