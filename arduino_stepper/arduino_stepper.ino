#include <Stepper.h>

const int nombreDePas=48*64;

Stepper RotMoteur(nombreDePas,9,11,10,6);

 
void setup() {

  RotMoteur.setSpeed(1);
  
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  
  Serial.setTimeout(10);
}

void loop() {

  int NbPas = 0 ;
  
  String string = Serial.readString();

// le code du moteur : Information (0:pour moteur) + IndiceMoteur (0:rotate / 1) + LeSens ( 0: counter clockwise / 1: clockwise) + NbPas ( 0 a 1000 )
// un tour = 2048
  if(string.charAt(0) == '0')
  {
    
  if(string.charAt(2) == '1' )
  {
    NbPas = string.substring(3).toInt();
  }
  if(string.charAt(2) == '0' )
  {
    NbPas = -string.substring(3).toInt();
  }
  
  if(string.charAt(1) == '0' )
  {
    RotMoteur.step(NbPas);
  }

  }


}
