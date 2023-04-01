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
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Tabs.H>
#include <FL/Fl_Box.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Output.H>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include "equasions.cpp"
#include <FL/gl.h>








void homee(Fl_Widget* widget, void* data) {
    // Hide widgets in gas
    home->show();
    // Show widgets in elec
    elec->hide();
}
void elecc(Fl_Widget* widget, void* data) {
    // Hide widgets in gas
    home->hide();
     // Show widgets in elec
    elec->show();
}
void gass(Fl_Widget* widget, void* data) {
    home->hide();
    gas->show();
}
void diff(Fl_Widget* widget, void* data) {
    gas->hide();
    df->show();
}
void boy(Fl_Widget* widget, void* data){
    gas->hide();
    bl->show();
}
void iddl(Fl_Widget* widget, void* data){
    gas->hide();
    idl->show();
}
void iissffrr(Fl_Widget* widget, void* data){
    gas->hide();
    IsFr->show();
}
void mmf(Fl_Widget* widget, void* data){
    elec->hide();
    mf->show();
}
void rreac(Fl_Widget* widget, void* data){
    elec->hide();
    reac->show();
}
void oohm(Fl_Widget* widget, void* data){
    elec->hide();
    ohl->show();
}
void wwp(Fl_Widget* widget, void* data){
    ohl->hide();
    Wp->show();
}
void vve(Fl_Widget* widget, void* data){
    ohl->hide();
    Ve->show();
}
void rrr(Fl_Widget* widget, void* data){
    ohl->hide();
    Rr->show();
}
void aai(Fl_Widget* widget, void* data){
    ohl->hide();
    Ai->show();
}
void phiiy(Fl_Widget* widget, void* data){
    home->hide();
    phy->show();
}
void eelas(Fl_Widget* widget, void* data){
    phy->hide();
    eleas->show();
}
void asstron(Fl_Widget* widget, void* data){
    phy->hide();
    astron->show();
}
void uunig(Fl_Widget* widget, void* data){
    phy->hide();
    unig->show();
}
void mmxe(Fl_Widget* widget, void* data){
    phy->hide();
    mxe->show();
}
void pparallax(Fl_Widget* widget, void* data){
    phy->hide();
    Parallax->show();
}
void uunig(Fl_Widget* widget, void* data){
    phy->hide();
    unig->show();
}
void uunig(Fl_Widget* widget, void* data){
    phy->hide();
    unig->show();
}

void homepage() {     
    Fl_Button *button1 = new Fl_Button(20, 40, 120, 80, "Gas Math");
    Fl_Button *button2 = new Fl_Button(140, 40, 120, 80, "Eletrical");
    Fl_Button *button3 = new Fl_Button(260, 40, 120, 80, "Physics");
    button1->callback(gass);
    button2->callback(elecc);
    button3->callback(phiiy);
     }
void spark(){
    Fl_Button *button4 = new Fl_Button(20, 40, 120, 80, "Ohms Law");
    Fl_Button *button5 = new Fl_Button(140, 40, 120, 80, "Reactance");
    Fl_Button *button9 = new Fl_Button(260, 40, 120, 80, "Magnetic\nFeild");
    Fl_Button *bkb = new Fl_Button(20, 700, 120, 20, "Back");
    bkb->callback(back, elec);
    button4->callback(oohm);  
    button5->callback(rreac);
    button9->callback(mmf); 
    }
void ohm() {
    Fl_Button *button10 =new Fl_Button( 20, 40, 120, 80, " Watts\n(P)");
    Fl_Button *button11 =new Fl_Button( 140, 40, 120, 80, " Volts\n(E)");
    Fl_Button *button12 =new Fl_Button( 260, 40, 120, 80, " Resistance\n(R)");
    Fl_Button *button13 =new Fl_Button( 380, 40, 120, 80, " Amp\n(I)");
    Fl_Button *bkb = new Fl_Button(20, 700, 120, 20, "Back");
    bkb->callback(eb, ohl);
    button10->callback(wwp);
    button11->callback(vve);
    button12->callback(rrr);
    button13->callback(aai);
  
}
void ges(){
    Fl_Button *button6 = new Fl_Button(20, 40, 120, 80, "Boyels\nlaw");
    Fl_Button *button7 = new Fl_Button(140, 40, 120, 80, "Ideal\nGas\nLaw");
    Fl_Button *button8 = new Fl_Button(260, 40, 120, 80, "Diferential");
    Fl_Button *button9 = new Fl_Button(380, 40, 120, 80, "Isentropic\nFlow\nRelation");
    Fl_Button *bkb = new Fl_Button(20, 700, 120, 20, "Back");
    bkb->callback(back, gas);
    button6->callback(boy);  
    button7->callback(iddl);
    button8->callback(diff);
    button9->callback(iissffrr);
}
void phiy() {
    Fl_Button *button10 = new Fl_Button(20, 40, 120, 80, "Elastic\nColision");
    Fl_Button *bkb = new Fl_Button(20, 700, 120, 20, "Back");
    bkb->callback(back, phy);
    button10->callback(eelas);
}
void aastrom() {
    Fl_Button *button13 = new Fl_Button(20, 40, 120, 80, "Universal\nGravitation");
    Fl_Button *button14 = new Fl_Button(20, 40, 120, 80, "Maxwell's\nequations ");
    Fl_Button *button14 = new Fl_Button(20, 40, 120, 80, " ");
    Fl_Button *bkb = new Fl_Button(20, 700, 120, 20, "Back");
    bkb->callback(back, astron);
    button13->callback(eelas);
    button14->callback();
}