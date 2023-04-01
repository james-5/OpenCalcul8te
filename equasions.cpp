/*   Copyright 2022 james-5

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Input_.H>
#include <FL/Fl_Tabs.H>
#include <FL/Fl_Group.H>
#include <FL/Fl_Button.H>
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Box.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Output.H>
#include <cstdlib>
#include <iostream>
#include <math.h>
#include <sstream>
#include <string>
#include <cmath>
#include "GlobalVar.cpp"
#include "backbuttons.cpp"




void ab(Fl_Widget* widget, void* data) {
  double P1 = std::atof(Pv1->value());
  double P2 = std::atof(Pv2->value());
  double V1 = std::atof(Vi1->value());
  double V2 = std::atof(vi2->value());

  

  // Calculate the result using the Boyles Law equation
  double P1a = P2 * (V2 / V1);
  double P2a = P1 * (V2 / V1);
  double V1a = (P1 / P2) * V2;
  double V2a = (P1 / P2) * V1;

  // Convert the result to a string and display it
  std::ostringstream P1as;
  P1as << P1a;
  P1aR->value(P1as.str().c_str());
  std::ostringstream P2as;
  P2as << P2a;
  P2aR->value(P2as.str().c_str());
  std::ostringstream v1as;
  v1as << V1a;
  V1aR->value(v1as.str().c_str());
  std::ostringstream V2as;
  V2as << V2a;
  V2aR->value(V2as.str().c_str());
}
void boylawfunc() {
        Pv1 = new Fl_Input(120, 100, 80, 50, "Pressure one:");
        Pv2 = new Fl_Input(120, 150, 80, 50, "Pressure two:");
        Vi1 = new Fl_Input(120, 200, 80, 50, "Volume one:");
        vi2 = new Fl_Input(120, 250, 80, 50, "Volume two:");

        P1aR = new Fl_Output(300, 100, 80, 50, "Pressure one:");
        P2aR = new Fl_Output(300, 150, 80, 50, "Pressure two:");
        V1aR = new Fl_Output(300, 200, 80, 50, "Volume one:");
        V2aR = new Fl_Output(300, 250, 80, 50, "Volume two:");
       //show_image("boyle_s_law.png");
        Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
        b1->callback(ab);
}
void idglf(Fl_Widget* widget, void* data) {
    double P1 = std::atof(idgP1->value());
    double P2 = std::atof(idgP2->value());
    double T1 = std::atof(idgT1->value());
    double T2 = std::atof(idgT2->value());
    double V1 = std::atof(idgV1->value());
    double V2 = std::atof(idgV2->value());
    double R = std::atof(Gc->value());
    double n = std::atof(m->value()); 

    double P1a = (n * R * T1) / V1;
    double P2a = (n * R * T2) / V2;
    double T1a = (P1 * V1) / (n * R);
    double T2a = (P2 * V2) / (n * R);
    double V1a = (n * R * T1) / P1;
    double V2a = (n * R * T2) / P2;

    std::ostringstream P1as;
    P1as << P1a;
    idgaRP1->value(P1as.str().c_str());
    std::ostringstream P2as;
    P2as << P2a;
    idgaRP2->value(P2as.str().c_str());
    std::ostringstream v1as;
    v1as << V1a;
    idgaRV1->value(v1as.str().c_str());
    std::ostringstream V2as;
    V2as << V2a;
    idgaRV2->value(V2as.str().c_str());
    std::ostringstream T1as;
    T1as << T1a;
    idgaRT1->value(T1as.str().c_str());
    std::ostringstream T2as;
    T2as << T2a;
    idgaRT2->value(V2as.str().c_str());
}
void IdealGassLawFunc() {

    idgP1 = new Fl_Input(120, 100, 80, 50,   "Pressuer one");
    idgP2 = new Fl_Input(120, 150, 80, 50, "Pressuer two");
    idgT1 = new Fl_Input(120, 200, 80, 50, "Temp one");
    idgT2 = new Fl_Input(120, 250, 80, 50, "Temp two");
    idgV1 = new Fl_Input(120, 300, 80, 50, "Volume one");
    idgV2 = new Fl_Input(120, 350, 80, 50, "Volume two");
    Gc = new Fl_Input(680, 100 , 80, 50,"Gas Constent just put 8.314");
    m = new Fl_Input(680, 150 , 80, 50,"moles if you dont know just put 1");    
    idgaRP1 = new Fl_Output(300, 100, 80, 50,  "Pressure one");
    idgaRP2 = new Fl_Output(300, 150, 80, 50,  "Pressure two");
    idgaRT1 = new Fl_Output(300, 200, 80, 50,  "Temp One");
    idgaRT2 = new Fl_Output(300, 250, 80, 50 , "Temp Two");
    idgaRV1 = new Fl_Output(300, 300, 80, 50 , "Volume one");
    idgaRV2 = new Fl_Output(300, 350, 80, 50 , "Volume Two");

    Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
      b1->callback(idglf); 
}
void elasticmath(Fl_Widget* widget, void* data) {
  
  double m1 = std::atof(m1Input->value());
  double m2 = std::atof(m2Input->value());
  double v1 = std::atof(v1Input->value());
  double v2 = std::atof(v2Input->value());

  // Calculate the new velocities using the elastic collision formula
  double v1New = (m1 - m2) / (m1 + m2) * v1 + (2 * m2) / (m1 + m2) * v2;
  double v2New = (m2 - m1) / (m1 + m2) * v2 + (2 * m1) / (m1 + m2) * v1;

    std::ostringstream v1Newa;
    v1Newa << v1New;
    v1Output->value(v1Newa.str().c_str());
    std::ostringstream v2Newa;
    v2Newa << v2New;
    v2Output->value(v2Newa.str().c_str());
}
void elasticUi() {
  m1Input = new Fl_Input(120, 100, 80,  50,"Mass 1 (kg):");
  m2Input = new Fl_Input(120, 150, 80,  50,"Mass 2 (kg):");
  v1Input = new Fl_Input(120, 200, 80, 50, "Velocity 1 (m/s):");
  v2Input = new Fl_Input(120, 250, 80, 50, "Velocity 2 (m/s):");

  // Create the output widgets
  v1Output = new Fl_Output(350, 100, 80, 50, "Velocity 1 (m/s):");
  v2Output = new Fl_Output(350, 150, 80, 50, "Velocity 2 (m/s):");
  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
  b1->callback(elasticmath);
}
void watmath(Fl_Widget* widget, void* data) {
   // double Pw = std::atof(P->value());
    double Ev = std::atof(E->value());
    double Ia = std::atof(I->value());
    double Rr = std::atof(R->value());

    double a = pow(Ev, 2);
    double PaRa = a / Rr;
    double PaR0a = Rr * pow(Ia, 2);
    double PaR1a = Ev * Ia;   

    std::ostringstream PaRaa;
    PaRaa << PaRa;
    PaR->value(PaRaa.str().c_str());
    std::ostringstream PaRab;
    PaRab << PaR0a;
    PaR1->value(PaRab.str().c_str());
    std::ostringstream PaRac;
    PaRac << PaR1a;
    PaR2->value(PaRac.str().c_str());
    
}
void volmath(Fl_Widget* widget, void* data) {
    double Pw = std::atof(P1->value());
    //double Ev = std::atof(E1->value());
    double Ia = std::atof(I1->value());
    double Rr = std::atof(R1->value());

    double EaRa =  Rr * Ia;   
    double EaR1a =  Pw / Ia;
    double EaR2a =  sqrt(Pw * Rr);

    std::ostringstream ab;
    ab << EaRa;
    EaR->value(ab.str().c_str());  
    std::ostringstream abc;
    abc << EaR1a;
    EaR1->value(abc.str().c_str());
    std::ostringstream abd;
    abd << EaR2a;
    EaR2->value(abd.str().c_str());
}
void restmath(Fl_Widget* widget, void* data) {
    double Pw = std::atof(P2->value());
    double Ev = std::atof(E2->value());
    double Ia = std::atof(I2->value());
    //double Rr = std::atof(R2->value());
    double RaRa = Ev / Ia;
    double RaR1a = pow(Ev, 2) / Pw;
    double RaR2a = Pw / pow(Ia, 2);

    std::ostringstream ab;
    ab << RaRa;
    RaR->value(ab.str().c_str());  
    std::ostringstream abc;
    abc << RaR1a;
    RaR1->value(abc.str().c_str());
    std::ostringstream abd;
    abd << RaR2a;
    RaR2->value(abd.str().c_str());

}
void ampmath(Fl_Widget* widget, void* data) {
    double Pw = std::atof(P3->value());
    double Ev = std::atof(E3->value());
    //double Ia = std::atof(I3->value());
    double Rr = std::atof(R3->value());

    double IaRa = sqrt(Pw / Rr);  
    double IaR1a = Pw / Ev;
    double IaR2a = Ev / Rr; 

    std::ostringstream ab;
    ab << IaRa;
    IaR->value(ab.str().c_str());  
    std::ostringstream abc;
    abc << IaR1a;
    IaR1->value(abc.str().c_str());
    std::ostringstream abd;
    abd << IaR2a;
    IaR2->value(abd.str().c_str());   

}
void reacmath(Fl_Widget* widget, void* data) {
  double Fv = std::atof(frec->value()); 
  double Hv = std::atof(Lh->value());
  
  double Oh = 6.28 * Fv * Hv;
  std::ostringstream ab;
  ab << Oh;
  ohms->value(ab.str().c_str());
}
void Reactanceui() {
  frec = new Fl_Input(120, 100, 80, 50, "Frequency (Hz)");
  Lh = new Fl_Input(120, 150, 80, 50, "Length in Henry");

  ohms = new Fl_Output(350, 100, 80, 50, "ohms");
  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
  b1->callback(reacmath);
}
void VolumeDiffmath(Fl_Widget* widget, void* data) {
  double cd = std::atof(Cd_input->value());
  double Ai = std::atof(A_input->value());
  double Pi = std::atof(P_input->value());
  double Ti = std::atof(T_input->value());
  double MW = std::atof(MW_input->value());
  double Gc = std::atof(gCon->value());
  double G = std::atof(gravity->value());
  double Zi = std::atof(Z->value());
  double dPi = std::atof(delta_P_input->value());

  double rho = Pi * MW / (Gc);
  double dPc = dPi / Zi;
  double  Q = cd * Ai * sqrt(2 * G * dPi / rho);

  std::ostringstream ab;
  ab << rho;
  rho_output->value(ab.str().c_str());
  std::ostringstream abc;
  abc << dPc;
  dPc_output->value(abc.str().c_str());
  std::ostringstream abd;
  abd << Q;
  Q_output->value(abd.str().c_str());
}
void IsentropicFlowMath(Fl_Widget* widget, void* data) {
    //Get the input values from the widgets
    double mach = std::atof(mach_input->value());
    double temperature_fahrenheit = std::atof(temperature_input->value());
    double pressure = std::atof(pressure_input->value());
    double gamma = std::atof(gamma_input->value());
    double gas_con =std::atof(gas_constant->value());
    // Convert temperature from Fahrenheit to Kelvin
    double temperature_kelvin = (temperature_fahrenheit - 32) * 5.0 / 9.0 + 273.15;
    // Calculate the speed of sound
    double speed_of_sound = std::sqrt(gamma * gas_con * temperature_kelvin);
    // Calculate the velocity and density
    double velocity = mach * speed_of_sound;
    double density = pressure / (gas_con * temperature_kelvin);

    // Set the output values in the widgets
    char velocity_str[50], density_str[50];
    std::sprintf(velocity_str, "%.2f", velocity);
    std::sprintf(density_str, "%.2f", density);
    velocity_output->value(velocity_str);
    density_output->value(density_str);
}
void IsentropicFlowUi() {
  mach_input = new Fl_Input(140, 50, 80, 50, "Mach Number");
  temperature_input = new Fl_Input(140, 100, 80, 50, "Temperature\n(F)");
  pressure_input = new Fl_Input(140, 150, 80, 50, "Pressure\n(Pa)");
  gamma_input = new Fl_Input(140, 200, 80, 50, "Specific Heat Ratio\n(gamma)");

  velocity_output = new Fl_Output(320, 50, 80, 50, "Velocity\n(m/s):");
  density_output = new Fl_Output(320, 100, 80, 50, "Density\n(kg/m^3):");


  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
  b1->callback(IsentropicFlowMath);
}
void VolumeDiffui() {
  Cd_input = new Fl_Input(170, 100, 80,50, "discharge coificiant");
  A_input = new Fl_Input(170, 150, 80, 50, "Plate area");
  delta_P_input = new Fl_Input(170, 200, 80, 50, "delta p");
  P_input = new Fl_Input(170, 250, 80, 50, "Pruesure");
  T_input = new Fl_Input(170, 300, 80, 50, "Tempeture");
  gravity = new Fl_Input(170, 350, 80, 50, "Gravity 9.81");
  gCon = new Fl_Input(170, 450, 80, 50, "Gas Constant 8.314");
  Z = new Fl_Input(170, 400, 80, 50, " Compressability Chart");
  MW_input = new Fl_Input(170, 500, 80, 50, " molecular weight");
  Q_output = new Fl_Output(350, 100, 80, 50, "Q"); 
  rho_output = new Fl_Output(350, 150, 80,50, "Rho");
  dPc_output = new Fl_Output(350, 200, 80, 50, "DPC");

  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
    b1->callback(VolumeDiffmath); // Remove the arguments 
}
void WattUi() {
 // P = new Fl_Input(120, 100, 80, 50, "Watts(P)");
  E = new Fl_Input(120, 150, 80, 50, "Volts(E)");  
  R = new Fl_Input(120, 200, 80, 50, "Resistance(R)");  
  I = new Fl_Input(120, 250, 80, 50, "Ampacity(I)");  

  PaR = new Fl_Output(350, 150, 80, 50, "Watts(P)");
  PaR1 = new Fl_Output(350, 200, 80, 50, "Watts(P)");
  PaR2 = new Fl_Output(350, 250, 80, 50, "Watts(P)");
  //IaR = new Fl_Output(350, 250, 80, 50, "Ampacity(I)");
  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
  b1->callback(watmath);
}
void voltsUi() {
  P1 = new Fl_Input(120, 150, 80, 50, "Watts(P)");
  //  E = new Fl_Input(120, 150, 80, 50, "Volts(E)");  
  R1 = new Fl_Input(120, 200, 80, 50, "Resistance(R)");  
  I1 = new Fl_Input(120, 250, 80, 50, "Ampacity(I)");  

 // PaR = new Fl_Output(350, 100, 80, 50, "Watts(P)");
  EaR = new Fl_Output(350, 150, 80, 50, "Volts(E)");
  EaR1 = new Fl_Output(350, 200, 80, 50, "Volts(E)");
  EaR2 = new Fl_Output(350, 250, 80, 50, "Volts(E)");
 // RaR = new Fl_Output(350, 200, 80, 50, "Resistance(R)");
 // IaR = new Fl_Output(350, 250, 80, 50, "Ampacity(I)");
  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
  b1->callback(volmath);
}
void resistUi() {
  P2 = new Fl_Input(120, 150, 80, 50, "Watts(P)");
  E2 = new Fl_Input(120, 200, 80, 50, "Volts(E)");  
  // R = new Fl_Input(120, 200, 80, 50, "Resistance(R)");  
  I2 = new Fl_Input(120, 250, 80, 50, "Ampacity(I)");  

  // PaR = new Fl_Output(350, 100, 80, 50, "Watts(P)");
  //  EaR = new Fl_Output(350, 150, 80, 50, "Volts(E)");
  RaR = new Fl_Output(350, 150, 80, 50, "Resistance(R)");
  RaR1 = new Fl_Output(350, 200, 80, 50, "Resistance(R)");
  RaR2 = new Fl_Output(350, 250, 80, 50, "Resistance(R)");
  // IaR = new Fl_Output(350, 250, 80, 50, "Ampacity(I)");
  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
  b1->callback(restmath);
}
void ampUi() {
  P3 = new Fl_Input(120, 150, 80, 50, "Watts(P)");
  E3 = new Fl_Input(120, 200, 80, 50, "Volts(E)");  
  R3 = new Fl_Input(120, 250, 80, 50, "Resistance(R)");  
   // I = new Fl_Input(120, 250, 80, 50, "Ampacity(I)");  

   // PaR = new Fl_Output(350, 100, 80, 50, "Watts(P)");
   // EaR = new Fl_Output(350, 150, 80, 50, "Volts(E)");
   // RaR = new Fl_Output(350, 200, 80, 50, "Resistance(R)");
  IaR = new Fl_Output(350, 150, 80, 50, "Ampacity(I)");
  IaR1 = new Fl_Output(350, 200, 80, 50, "Ampacity(I)");
  IaR2 = new Fl_Output(350, 250, 80, 50, "Ampacity(I)");
   
  Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
  b1->callback(ampmath);
  
}
