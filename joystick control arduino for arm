
#include <Servo.h>

Servo servo_1;
Servo servo_2;
Servo servo_3;
Servo servo_4;
Servo servo_5;
Servo servo_6;  // Servo for wrist (connected to pin 6)

int joyX = A0;    // Joystick X-axis connected to A0
int joyY = A1;    // Joystick Y-axis connected to A1
int joyButton = 7;  // Joystick button connected to digital pin 7

int servo6_pos = 90;  // Initial position of wrist servo (servo_6)
int deadzone = 100;   // Deadzone for joystick to prevent accidental movement

void close() {
  servo_1.write(0);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(0);
  servo_6.write(90);  // Keep wrist (servo 6) at 90° when opening
  delay(1000);  // Wait for 1000 millisecond(s)
}

void open() {
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(90);  // Close wrist (servo 6)
  delay(1000);  // Wait for 1000 millisecond(s)
}

// Gradual Open
void grad_open() {
  servo_1.write(0);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(90);
  servo_6.write(90);
  delay(1000);
  
  servo_4.write(90);
  delay(1000);
  
  servo_3.write(90);
  delay(1000);
  
  servo_2.write(90);
  delay(1000);
  
  servo_1.write(90);
  delay(1000);
}

// Gradual close
void grad_close() {
  delay(1000);
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(90);
  delay(1000);
  
  servo_5.write(0);
  delay(1000);
  
  servo_4.write(0);
  delay(1000);
  
  servo_3.write(0);
  delay(1000);
  
  servo_2.write(0);
  delay(1000);
  
  servo_1.write(0);
  delay(1000);
}

//funny secret when joysick button is pressed
void open_servo2_4_5() {
  servo_2.write(0);  // Open servo 2
  servo_4.write(0);  // Open servo 4
  servo_5.write(0);  // Open servo 5
}

void setup() {
  // Set servo to pins
  servo_1.attach(1, 500, 2500);
  servo_2.attach(2, 500, 2500);
  servo_3.attach(3, 500, 2500);
  servo_4.attach(4, 500, 2500);
  servo_5.attach(5, 500, 2500);
  servo_6.attach(6, 500, 2500);  // Servo 6 (wrist) on pin 6

  // Joystick button pin setup
  pinMode(joyButton, INPUT_PULLUP);  // Configure joystick button pin with internal pull-up resistor

  // Servo test
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(90);  // Set wrist servo to 90°

  grad_close();
  delay(1000);
  grad_open();
}

void loop() {
  int xValue = analogRead(joyX);  // Read X-axis value
  int yValue = analogRead(joyY);  // Read Y-axis value
  int buttonState = digitalRead(joyButton);  // Read the state of the joystick button (LOW when pressed)

  // Handle up/down movement for open/close using Y-axis
  if (yValue > 512 + deadzone) {
    close();  // Joystick pushed up, close
    delay(1000);  // Add delay to debounce
  } else if (yValue < 512 - deadzone) {
    open();  // Joystick pulled down, open
    delay(1000);  // Add delay to debounce
  }

  // Handle left/right movement for wrist (servo_6) using X-axis
  if (abs(xValue - 512) > deadzone) {  // Only move if outside deadzone
    // Map joystick X-axis to servo position (0-180 degrees)
    servo6_pos = map(xValue, 0, 1023, 0, 180);
    servo_6.write(servo6_pos);  // Update wrist servo position
  }

  // If the joystick button is pressed, open only servo 2, 4, and 5
  if (buttonState == LOW) {  // Button is pressed (LOW)
    open_servo2_4_5();
    delay(1000);  // Debounce delay to avoid rapid triggering
  }

  delay(10);  // Delay a little bit to improve simulation performance
}
