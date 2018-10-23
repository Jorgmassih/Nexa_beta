#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 20, 2018 10:28:39 PM AST  platform: Linux

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import transducer_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Toplevel()
    transducer_support.set_Tk_var()
    top = Transductor (root)
    transducer_support.init(root, top)
    root.mainloop()

w = None
def create_Transductor(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    transducer_support.set_Tk_var()
    top = Transductor (w)
    transducer_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Transductor():
    global w
    w.destroy()
    w = None




#**********************Edited************************************

#----------------------Ecuations solver function-----------------
    
def calculate(self, R_min,R_max,v_in,v_out_min, v_out_max):
    R3 = R_min
    R1 = 10*R3
    R2 = 10*R3
    R_span = R_max - R_min
    V_in_max = (v_in*R_max)/(R1 + R_max)
    V_in_min = (v_in*R_min)/(R1 + R_min)
    A = (v_out_max - v_out_min)/(V_in_max - V_in_min)
    Rg = (49.4*1000)/(A-1)
        
    text_result = """
    R1 = {}
    R2 = {}
    R3 = {}
    Pot = {}
    Rmin = {}
    Rg = {}
    """.format(round(R1,2), round(R2,2), round(R3,2), round(R_span,2), round(R3,2), round(Rg,2))
        
    self.Label4.configure(text=text_result)
        
#************************Edited************************************


class Transductor:
    

    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {DejaVu Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("548x477+418+211")
        top.title("Transductor")
        top.configure(background="#2d3436")
        top.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.036, rely=0.042, relheight=0.22
                , relwidth=0.912)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="#ffffff")
        self.Labelframe1.configure(text='''Resistencias''')
        self.Labelframe1.configure(background="#2d3436")
        self.Labelframe1.configure(width=500)

        self.R_min = Entry(self.Labelframe1)
        self.R_min.place(relx=0.26, rely=0.571, height=23, relwidth=0.252
                , bordermode='ignore')
        self.R_min.configure(background="white")
        self.R_min.configure(font="TkFixedFont")
        self.R_min.configure(relief=FLAT)
        self.R_min.configure(selectbackground="#c4c4c4")
        self.R_min.configure(textvariable=transducer_support.r_min)
        self.R_min.configure(width=126)

        self.R_max = Entry(self.Labelframe1)
        self.R_max.place(relx=0.54, rely=0.571, height=23, relwidth=0.252
                , bordermode='ignore')
        self.R_max.configure(background="white")
        self.R_max.configure(font="TkFixedFont")
        self.R_max.configure(relief=FLAT)
        self.R_max.configure(selectbackground="#c4c4c4")
        self.R_max.configure(textvariable=transducer_support.r_max)
        self.R_max.configure(width=126)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.28, rely=0.286, height=21, width=219
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#2d3436")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Rango de operacion (min-max)''')

        self.Labelframe1_1 = LabelFrame(top)
        self.Labelframe1_1.place(relx=0.036, rely=0.294, relheight=0.178
                , relwidth=0.912)
        self.Labelframe1_1.configure(relief=GROOVE)
        self.Labelframe1_1.configure(foreground="#ffffff")
        self.Labelframe1_1.configure(text='''Voltajes''')
        self.Labelframe1_1.configure(background="#2d3436")
        self.Labelframe1_1.configure(width=500)

        self.V_out_min = Entry(self.Labelframe1_1)
        self.V_out_min.place(relx=0.46, rely=0.588, height=23, relwidth=0.172
                , bordermode='ignore')
        self.V_out_min.configure(background="white")
        self.V_out_min.configure(font="TkFixedFont")
        self.V_out_min.configure(selectbackground="#c4c4c4")
        self.V_out_min.configure(textvariable=transducer_support.v_out_min)

        self.V_in = Entry(self.Labelframe1_1)
        self.V_in.place(relx=0.2, rely=0.588, height=23, relwidth=0.172
                , bordermode='ignore')
        self.V_in.configure(background="white")
        self.V_in.configure(font="TkFixedFont")
        self.V_in.configure(selectbackground="#c4c4c4")
        self.V_in.configure(textvariable=transducer_support.v_in)

        self.V_out_max = Entry(self.Labelframe1_1)
        self.V_out_max.place(relx=0.68, rely=0.588, height=23, relwidth=0.152
                , bordermode='ignore')
        self.V_out_max.configure(background="white")
        self.V_out_max.configure(font="TkFixedFont")
        self.V_out_max.configure(selectbackground="#c4c4c4")
        self.V_out_max.configure(textvariable=transducer_support.v_out_max)

        self.Label2 = Label(self.Labelframe1_1)
        self.Label2.place(relx=0.26, rely=0.235, height=21, width=25
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(background="#2d3436")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Vin''')

        self.Label3 = Label(self.Labelframe1_1)
        self.Label3.place(relx=0.42, rely=0.235, height=21, width=229
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(background="#2d3436")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Rango de operacion (min - max)''')

        self.Labelframe1_2 = LabelFrame(top)
        self.Labelframe1_2.place(relx=0.036, rely=0.503, relheight=0.325
                , relwidth=0.912)
        self.Labelframe1_2.configure(relief=GROOVE)
        self.Labelframe1_2.configure(foreground="#ffffff")
        self.Labelframe1_2.configure(text='''Resultados''')
        self.Labelframe1_2.configure(background="#2d3436")
        self.Labelframe1_2.configure(width=500)

        self.Label4 = Label(self.Labelframe1_2)
        self.Label4.place(relx=0.02, rely=0.194, height=111, width=479
                , bordermode='ignore')
        self.Label4.configure(background="#2d3436")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(text='''Los resultados aparecerán aqui''')
        self.Label4.configure(width=479)

        self.Calculate = Button(top, command=lambda:calculate(self, transducer_support.r_min.get(),
                                                              transducer_support.r_max.get(),
                                                              transducer_support.v_in.get(),
                                                              transducer_support.v_out_min.get(),
                                                              transducer_support.v_out_max.get(),
                                                                          ))
        self.Calculate.place(relx=0.036, rely=0.86, height=39, width=499)
        self.Calculate.configure(activebackground="#d9d9d9")
        self.Calculate.configure(background="#00b894")
        self.Calculate.configure(font=font9)
        self.Calculate.configure(highlightbackground="#00b894")
        self.Calculate.configure(relief=FLAT)
        self.Calculate.configure(text='''Calcular''')






if __name__ == '__main__':
    vp_start_gui()


