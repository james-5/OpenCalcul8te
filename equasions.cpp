#include <FL/Fl.H>
#include <FL/Fl_Window.H>
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
#include <sstream>
#include <string>
#include "GlobalVar.cpp"






void boylawfunc() {
        Pv1 = new Fl_Input(120, 100, 80, 50, "Pressure one:");
        Pv2 = new Fl_Input(120, 150, 80, 50, "Pressure two:");
        Vi1 = new Fl_Input(120, 200, 80, 50, "Volume one:");
        vi2 = new Fl_Input(120, 250, 80, 50, "Volume two:");

        P1aR = new Fl_Output(300, 100, 80, 50, "Pressure one:");
        P2aR = new Fl_Output(300, 150, 80, 50, "Pressure two:");
        V1aR = new Fl_Output(300, 200, 80, 50, "Volume one:");
        V2aR = new Fl_Output(300, 250, 80, 50, "Volume two:");
}
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
void elasticUi() {
  m1Input = new Fl_Input(120, 100, 80,  50,"Mass 1 (kg):");
  m2Input = new Fl_Input(120, 150, 80,  50,"Mass 2 (kg):");
  v1Input = new Fl_Input(120, 200, 80, 50, "Velocity 1 (m/s):");
  v2Input = new Fl_Input(120, 250, 80, 50, "Velocity 2 (m/s):");

  // Create the output widgets
  v1Output = new Fl_Output(350, 100, 80, 50, "Velocity 1 (m/s):");
  v2Output = new Fl_Output(350, 150, 80, 50, "Velocity 2 (m/s):");
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