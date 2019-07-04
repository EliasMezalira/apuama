#include "DHT.h"
#define DHTPIN A2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
const int TEMPERATURA_INTERNA = 10;
const int TEMPERATURA_EXTERNA = 11;
const int UMIDADE = 12;
const int GAS = 13;
const int intLM35 = A0;
const int MQ7 = A1;

int a =0; 

void setup() {

Serial.begin(9600);              //Starting serial communication
dht.begin();
}

void loop() {
   
   if (Serial.available() > 0) {
      String funcaoS = Serial.readString();
      int funcao = funcaoS.toInt();

      switch (funcao) {
        case TEMPERATURA_INTERNA:
          Serial.println(leituraTemperaturaInterna());
          break;
        case TEMPERATURA_EXTERNA:
          Serial.println(leituraTemperaturaExterna());
          break;
        case UMIDADE:
          Serial.println(leituraUmidade());
          break;
        case GAS:
          Serial.println(leituraGas());
          break;
        default:
          // statements
        break;
       } ;
   } 
}

float leituraTemperaturaInterna(){
  return (float(analogRead(intLM35))*5/(1023))/0.01;
}

float leituraTemperaturaExterna(){
  return dht.readTemperature();
}

float leituraUmidade(){
  return dht.readHumidity();
}

float leituraGas(){
  return analogRead(MQ7);
}


   
