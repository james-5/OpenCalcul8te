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



//FL_Group names
Fl_Group* gas;
Fl_Group* elec;
Fl_Group* home;
Fl_Group* phy;
Fl_Group* df;
Fl_Group* bl;
Fl_Group* idl;
Fl_Group*ohl;
Fl_Group*reac;
Fl_Group*mf;
Fl_Group*Wp;
Fl_Group*Ve;
Fl_Group*Rr;
Fl_Group*Ai;
Fl_Group*IsFr;


//Boyels law
Fl_Input* Pv1;
Fl_Input* Pv2;
Fl_Input* Vi1;
Fl_Input* vi2;
Fl_Output* P1aR;
Fl_Output* P2aR;
Fl_Output* V1aR;
Fl_Output* V2aR;

//Ideal Gass Law
Fl_Input* idgP1;
Fl_Input* idgP2;
Fl_Input* idgT1;
Fl_Input* idgT2;
Fl_Input* idgV1;
Fl_Input* idgV2;
Fl_Input* Gc;
Fl_Input* m;
Fl_Output* idgaRP1;
Fl_Output* idgaRP2;
Fl_Output* idgaRT1;
Fl_Output* idgaRT2;
Fl_Output* idgaRV1;
Fl_Output* idgaRV2;
//Elastic Equaison
Fl_Input* m1Input;
Fl_Input* m2Input;
Fl_Input* v1Input;
Fl_Input* v2Input;
Fl_Output* v1Output;
Fl_Output* v2Output;
//ohms law
//wats
Fl_Input* P;
Fl_Input* E;
Fl_Input* R;
Fl_Input* I;
Fl_Output* PaR;
Fl_Output* PaR1;
Fl_Output* PaR2;
//volts
Fl_Input* P1;
Fl_Input* E1;
Fl_Input* R1;
Fl_Input* I1;
Fl_Output* EaR;
Fl_Output* EaR1;
Fl_Output* EaR2;
//resistance
Fl_Input* P2;
Fl_Input* E2;
Fl_Input* R2;
Fl_Input* I2;

Fl_Output* RaR;
Fl_Output* RaR1;
Fl_Output* RaR2;
//amps
Fl_Input* P3;
Fl_Input* E3;
Fl_Input* R3;
Fl_Input* I3;
Fl_Output* IaR;
Fl_Output* IaR1;
Fl_Output* IaR2;
//reactance
Fl_Input* twopi;
Fl_Input* frec;
Fl_Input* Lh;
Fl_Output* ohms;
//Differental flow 
Fl_Input* Cd_input; 
Fl_Input* A_input; 
Fl_Input* T_input;
Fl_Input* P_input;
Fl_Input* delta_P_input;
Fl_Input* gravity; 
Fl_Input* MW_input;
Fl_Input* Z;
Fl_Input* gCon;
Fl_Output* Q_output; 
Fl_Output* rho_output;
Fl_Output* dPc_output;
//Isentropic Flow Relation
Fl_Input *mach_input, *temperature_input, *pressure_input, *gamma_input, *gas_constant;
Fl_Output *velocity_output, *density_output;






