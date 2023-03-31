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


void back(Fl_Widget* widget, void* data) {
  Fl_Window* window = (Fl_Window*)widget->window();
    // Get pointer to the current group
    Fl_Group* current_group = (Fl_Group*)data;
    // Hide the current group and show the parent group
    current_group->hide();
    home->show();
    }
void gb(Fl_Widget* widget, void* data) {
  Fl_Window* window = (Fl_Window*)widget->window();
    // Get pointer to the current group
    Fl_Group* current_group = (Fl_Group*)data;
    // Hide the current group and show the parent group
    current_group->hide();
    gas->show();
}
void eb(Fl_Widget* widget, void* data) {
  Fl_Window* window = (Fl_Window*)widget->window();
    // Get pointer to the current group
    Fl_Group* current_group = (Fl_Group*)data;
    // Hide the current group and show the parent group
    current_group->hide();
    elec->show();
}
void ohb(Fl_Widget* widget, void* data) {
  Fl_Window* window = (Fl_Window*)widget->window();
    // Get pointer to the current group
    Fl_Group* current_group = (Fl_Group*)data;
    // Hide the current group and show the parent group
    current_group->hide();
    ohl->show();
}