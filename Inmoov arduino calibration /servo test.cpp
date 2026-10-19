//proof of concept :

#include <Servo.h>

Servo servo_1;

Servo servo_2;

Servo servo_3;

Servo servo_4;

Servo servo_5;

Servo servo_6;

void close (){
  servo_1.write(0);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(0);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
}
void open (){
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
 }
//gradual close 
 void grad_open(){
servo_1.write(0);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(90);
  servo_6.write(0);
 delay(1000);
  servo_1.write(0);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(90);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(0);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(0);
  servo_2.write(0);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(0);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
}

void grad_close(){
delay(1000);
 servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(90);
  servo_6.write(0);
delay(1000);
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(90);
  servo_5.write(0);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(90);
  servo_4.write(0);
  servo_5.write(0);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(90);
  servo_2.write(90);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(0);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(90);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(0);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
  servo_1.write(0);
  servo_2.write(0);
  servo_3.write(0);
  servo_4.write(0);
  servo_5.write(0);
  servo_6.write(0);
  delay(1000); // Wait for 1000 millisecond(s)
 }

void setup(){

//set servo to pin
 servo_1.attach(1, 500, 2500);
 servo_2.attach(2, 500, 2500);
 servo_3.attach(3, 500, 2500);
 servo_4.attach(4, 500, 2500);
 servo_5.attach(5, 500, 2500);
 servo_6.attach(6, 500, 2500);

open();
close();
open();
grad_close();
grad_open();
close();
open();
//servo test


}

void loop()
{
  delay(10); // Delay a little bit to improve simulation performance
}
