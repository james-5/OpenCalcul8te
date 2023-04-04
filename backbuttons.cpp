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
void phb(Fl_Widget* widget, void* data) {
  Fl_Window* window = (Fl_Window*)widget->window();
    // Get pointer to the current group
    Fl_Group* current_group = (Fl_Group*)data;
    // Hide the current group and show the parent group
    current_group->hide();
    phy->show();
}
void asb(Fl_Widget* widget, void* data) {
  Fl_Window* window = (Fl_Window*)widget->window();
    // Get pointer to the current group
    Fl_Group* current_group = (Fl_Group*)data;
    // Hide the current group and show the parent group
    current_group->hide();
    astron->show();
}
