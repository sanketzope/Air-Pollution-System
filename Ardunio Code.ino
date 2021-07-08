#include <dht.h>
#include <LiquidCrystal.h>
#define dht_apin A0 
int sensorValue;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
dht DHT;
 
void setup()
{
  lcd.begin(16, 2);
  Serial.begin(9600);
  delay(500);
  delay(500);
}
 
void loop()
   {sensorValue = analogRead(0);       
lcd.setCursor(0,0);
lcd.print("ArQ=");
lcd.print(sensorValue,DEC);
lcd.print(" PPM");
lcd.println("       "); 
lcd.print("  ");
delay(100);                                   
DHT.read11(dht_apin);
Serial.println("T="+String(DHT.temperature)+", H="+String(DHT.humidity)+", A="+String(sensorValue));
delay(500);
}
