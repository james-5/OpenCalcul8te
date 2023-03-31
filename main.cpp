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
#include "ui_elaments.cpp"



int main(int argc, char **argv) {
    // Create window
    Fl_Window *window = new Fl_Window(900, 900, "OpenCalcul8te");
    // Create gas
    home = new Fl_Group(10, 60, 800, 800);
        homepage();
        home->end();
    // Create elec
    elec = new Fl_Group(10, 60, 800, 800);
        spark();
        elec->end();
        elec->hide();
    gas = new Fl_Group(10, 60, 800, 800);
        ges();
        gas->end();
        gas->hide();
    df =new Fl_Group(10, 60, 800, 800);
        VolumeDiffui();
        Fl_Button *bkb = new Fl_Button(20, 700, 120, 20, "Back");
        bkb->callback(gb, df);
        df->end();
        df->hide();
    bl = new Fl_Group(10, 60, 800, 800);
        boylawfunc();
        Fl_Button *bkb1 = new Fl_Button(20, 700, 120, 20, "Back");
            bkb1->callback(gb, bl);
        bl->end();
        bl->hide();
    idl = new Fl_Group(10, 60, 800, 800);
        IdealGassLawFunc();
        Fl_Button *bkb2 = new Fl_Button(20, 700, 120, 20, "Back");
            bkb2->callback(gb, idl);
        idl->end();
        idl->hide();
    ohl = new Fl_Group(10, 60, 800, 800);
        ohm();
        Fl_Button *bkb3 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb3->callback(eb, ohl);
        ohl->end();
        ohl->hide();
    
    reac = new Fl_Group(10, 60, 800, 800);
        Reactanceui();
        Fl_Button *bkb4 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb4->callback(eb, reac);
        reac->end();
        reac->hide();

    mf = new Fl_Group(10, 60, 800, 800);
        Fl_Button *bkb5 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb5->callback(eb, mf);
        mf->end();
        mf->hide();
    Wp = new Fl_Group(10, 60, 800, 800);
        WattUi();
        Fl_Button *bkb6 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb6->callback(ohb, Wp);
        Wp->end();
        Wp->hide();
    Ve = new Fl_Group(10, 60, 800, 800);
        voltsUi();
        Fl_Button *bkb7 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb7->callback(ohb, Ve);
        Ve->end();
        Ve->hide();
    Rr = new Fl_Group(10, 60, 800, 800);
        resistUi();
        Fl_Button *bkb8 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb8->callback(ohb, Rr);
        Rr->end();
        Rr->hide();
    Ai = new Fl_Group(10, 60, 800, 800);
        ampUi();
        Fl_Button *bkb9 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb9->callback(ohb, Ai);
        Ai->end();
        Ai->hide();       
    IsFr = new Fl_Group(10, 60, 800, 800);
        IsentropicFlowUi();
        Fl_Button *bkb10 = new Fl_Button(20, 700, 120, 20, "Back");
        bkb10->callback(gb, IsFr);
        IsFr->end();
        IsFr->hide();       
    // Show window
    window->end();
    window->show(argc, argv);

    // Run event loop
    return Fl::run();
}
