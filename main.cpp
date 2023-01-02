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
#include "equasions.cpp"


int main(int argc, char *argv[]) {
  Fl::scheme("gtk+");
  Fl_Window *win = new Fl_Window(800,800,"OpenCalcul8te");
  {
    // Create the tab widget
    Fl_Tabs *tabs = new Fl_Tabs(10,10,800,800);
    {
      Fl_Group *GasMath = new Fl_Group(10,35,800,800,"GasMath");{
          Fl_Tabs* gastab = new Fl_Tabs(10, 35, 800, 800); {
            Fl_Group *Boyleslaw = new Fl_Group(10,60,800,800,"Boyles law");{
               boylawfunc();
               Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
               b1->callback(ab); // Remove the arguments 
             }
            Boyleslaw->end();

            Fl_Group *idealGassLaw = new Fl_Group(10,60,800,800,"idealGassLaw"); {
              IdealGassLawFunc();
              Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
               b1->callback(idglf); // Remove the arguments 
             }
            idealGassLaw->end();
      }
      }
      GasMath->end();
      Fl_Group *physics = new Fl_Group(10,65,800,800,"Physics");{
         Fl_Tabs* gastab = new Fl_Tabs(10, 35, 800, 800); {
           Fl_Group *Elastic = new Fl_Group(10,60,800,800,"Elastic colision");{
                elasticUi();
               Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
               b1->callback(elasticmath); // Remove the arguments 
               }
      Elastic->end();
      }}
      
      physics->end();

      Fl_Group *ohmslaw = new Fl_Group(10, 35, 800, 800, "Ohms Law"); {
        Fl_Tabs* gastab =new Fl_Tabs(10, 35, 800, 800); {
          Fl_Group *watt = new Fl_Group(10, 60, 800, 800, "Watts(P)"); {
               WattUi();
               Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
               b1->callback(watmath); // Remove the arguments 
          }
          watt->end();
          Fl_Group *volt = new Fl_Group(10, 60, 800, 800, "Volts(E)");{
              voltsUi();
              Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
               b1->callback(elasticmath); // Remove the arguments 
          }
          volt->end();
          Fl_Group *res = new Fl_Group(10, 60, 800, 800, "Resistance(R)");{
               resistUi();
               Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
               b1->callback(elasticmath); // Remove the arguments 
          }
          res->end();
          Fl_Group *amp = new Fl_Group(10, 60, 800, 800, "Amp(I)");{
               ampUi();
               Fl_Button *b1 = new Fl_Button(680,680,100,75,"Calculate"); b1->color(88+3);
               b1->callback(elasticmath); // Remove the arguments 
          }
          amp->end();
        }
      }
    tabs->end();
  }
  win->end();
  win->show(argc, argv);
  return(Fl::run());
  }
}
