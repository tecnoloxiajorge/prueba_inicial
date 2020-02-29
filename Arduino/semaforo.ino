int rojo=11, amarillo=12, verde=13; 

void setup() {  
pinMode (rojo,OUTPUT); 
pinMode (amarillo,OUTPUT);
pinMode (verde,OUTPUT);

}

void loop() {
  digitalWrite(verde, HIGH); //encendemos verde
  delay(5000); //esperamos 5 segundos
  digitalWrite(verde,LOW); //apagamos el verde
  digitalWrite(amarillo,HIGH); //encendemos amarillo
  delay(2000); // esperamos 2 segundos
  digitalWrite(amarillo,LOW); //apagamos amarillo
  digitalWrite(rojo, HIGH); //encendemos rojo
  delay(7000); //esperamos 7 segundos
  digitalWrite(rojo, LOW); //apagamos rojo
  //ahora ya se vuelve a encender el verde
}

