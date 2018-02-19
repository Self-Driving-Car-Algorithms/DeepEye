#! /usr/bin/env python
# GUI module generated by PAGE version 4.9

# libraries and dependencies
# ---------------------------------------------------------------------------- #
import sys, os, threading, time

import driving_assistant.user_interface.gui_utils as gui_utils
from driving_assistant.DrivingAssistant import *


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
# ---------------------------------------------------------------------------- #


# Utility Functions
# ---------------------------------------------------------------------------- #
FOLDER_PATH = os.path.join(os.getcwd(), 'driving_assistant', 'user_interface')

def start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    gui_utils.set_Tk_var()
    top = Window(root)
    gui_utils.init(root, top)
    root.mainloop()

w = None
def create_gui(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    gui_utils.set_Tk_var()
    top = Window (w)
    gui_utils.init(w, top, *args, **kwargs)       
    return (w, top)

def destroy_gui():
    global w
    w.destroy()
    w = None
    
# ---------------------------------------------------------------------------- #

class Window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font18 = "-family {Calibri Light} -size 22 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"
        font21 = "-family David -size 48 -weight bold -slant italic "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("496x707+2678+135")
        top.title("DeepEye")
        top.configure(background="#d9d9d9")


        self.DatasetFrame = ttk.Labelframe(top)
        self.DatasetFrame.place(relx=0.5, rely=0.21, relheight=0.18
                , relwidth=0.45)
        self.DatasetFrame.configure(text='''CNN''')
        self.DatasetFrame.configure(width=225)

        self.ClassifierCode = ttk.Combobox(self.DatasetFrame)
        self.ClassifierCode.place(relx=0.38, rely=0.03, relheight=0.23, relwidth=0.54)
        self.value_list = ['Nas','Inception-Resnet','Resnet101',]
        self.ClassifierCode.configure(values=self.value_list)
        self.ClassifierCode.configure(textvariable=gui_utils.ClassiferBox)
        self.ClassifierCode.configure(takefocus="")
        self.ClassifierCode.insert(0,'Resnet101')

        self.DatasetCode = ttk.Combobox(self.DatasetFrame)
        self.DatasetCode.place(relx=0.38, rely=0.37, relheight=0.23, relwidth=0.54)
        self.value_list = ['Coco','Kitti',]
        self.DatasetCode.configure(values=self.value_list)
        self.DatasetCode.configure(textvariable=gui_utils.DatasetBox)
        self.DatasetCode.configure(takefocus="")
        self.DatasetCode.insert(0,'Coco')
        
        self.Threshold = Spinbox(self.DatasetFrame, from_=0.0, to=1.0)
        self.Threshold.place(relx=0.38, rely=0.69, relheight=0.23, relwidth=0.54)
        self.Threshold.configure(activebackground="#f9f9f9")
        self.Threshold.configure(background="white")
        self.Threshold.configure(buttonbackground="#d9d9d9")
        self.Threshold.configure(disabledforeground="#a3a3a3")
        self.Threshold.configure(foreground="black")
        self.Threshold.configure(highlightbackground="black")
        self.Threshold.configure(highlightcolor="black")
        self.Threshold.configure(increment="0.01")
        self.Threshold.configure(insertbackground="black")
        self.Threshold.configure(selectbackground="#c4c4c4")
        self.Threshold.configure(selectforeground="black")
        self.Threshold.configure(textvariable=gui_utils.ThresholdBox)
        self.Threshold.configure(to="1.0")
        self.value_list.clear()
        for i in range(101):
            self.value_list.append(str(i)+'%')        
        self.Threshold.configure(values=self.value_list)
        self.Threshold.configure(width=115)
        self.Threshold.delete(0,"end")
        self.Threshold.insert(0,'85%')

        self.TLabel4 = ttk.Label(self.DatasetFrame)
        self.TLabel4.place(relx=0.1, rely=0.05, height=19, width=51)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''Identifier''')

        self.TLabel5 = ttk.Label(self.DatasetFrame)
        self.TLabel5.place(relx=0.14, rely=0.39, height=19, width=51)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(relief=FLAT)
        self.TLabel5.configure(text='''Dataset''')
        #self.TLabel5.configure(width=51)

        self.TLabel6 = ttk.Label(self.DatasetFrame)
        self.TLabel6.place(relx=0.08, rely=0.71, height=19, width=57)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''Threshold''')

        self.InputOutputFrame = ttk.Labelframe(top)
        self.InputOutputFrame.place(relx=0.04, rely=0.21, relheight=0.43
                , relwidth=0.42)
        self.InputOutputFrame.configure(text='''Monitor Output''')
        self.InputOutputFrame.configure(width=210)


        self.TLabel9 = ttk.Label(self.InputOutputFrame)
        self.TLabel9.place(relx=0.07, rely=0.04, height=19, width=61)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(relief=FLAT)
        self.TLabel9.configure(text='''Monitor ID''')


        self.MonitorId = ttk.Combobox(self.InputOutputFrame)
        self.MonitorId.place(relx=0.43, rely=0.04, relheight=0.07, relwidth=0.4)
        self.MonitorId.configure(textvariable=gui_utils.MonitorIDBox)
        self.MonitorId.configure(width=83)
        self.MonitorId.configure(takefocus="")
        self.value_list = ['0','1', '2']
        self.MonitorId.configure(values=self.value_list)
        self.MonitorId.insert(0,'1')


        self.visualCheck = IntVar()
        self.EnableVisual = Checkbutton(self.InputOutputFrame, command=self.FlipState)
        self.EnableVisual.place(relx=0.08, rely=0.15, relheight=0.08, relwidth=0.65)
        self.EnableVisual.configure(activebackground="#d9d9d9")
        self.EnableVisual.configure(activeforeground="#000000")
        self.EnableVisual.configure(background="#d9d9d9")
        self.EnableVisual.configure(disabledforeground="#a3a3a3")
        self.EnableVisual.configure(foreground="#000000")
        self.EnableVisual.configure(highlightbackground="#d9d9d9")
        self.EnableVisual.configure(highlightcolor="black")
        self.EnableVisual.configure(justify=LEFT)
        self.EnableVisual.configure(text='''Enable Visualization?''')
        self.EnableVisual.configure(variable=self.visualCheck)
        self.EnableVisual.select()


        self.LaneDetectionCheck = Checkbutton(self.InputOutputFrame)
        self.LaneDetectionCheck.place(relx=0.08, rely=0.27, relheight=0.08
                , relwidth=0.72)
        self.LaneDetectionCheck.configure(activebackground="#d9d9d9")
        self.LaneDetectionCheck.configure(activeforeground="#000000")
        self.LaneDetectionCheck.configure(background="#d9d9d9")
        self.LaneDetectionCheck.configure(disabledforeground="#a3a3a3")
        self.LaneDetectionCheck.configure(foreground="#000000")
        self.LaneDetectionCheck.configure(highlightbackground="#d9d9d9")
        self.LaneDetectionCheck.configure(highlightcolor="black")
        self.LaneDetectionCheck.configure(justify=LEFT)
        self.LaneDetectionCheck.configure(text='''Enable Lane Detection?''')
        self.LaneDetectionCheck.configure(variable=gui_utils.LaneDetection)
        self.LaneDetectionCheck.configure(width=151)
        self.LaneDetectionCheck.select()

        
        self.windowCheck = IntVar()
        self.CustomWindowCheck = Checkbutton(self.InputOutputFrame, command=self.FlipState)
        self.CustomWindowCheck.place(relx=0.088, rely=0.39, relheight=0.08
                , relwidth=0.77)
        self.CustomWindowCheck.configure(activebackground="#d9d9d9")
        self.CustomWindowCheck.configure(activeforeground="#000000")
        self.CustomWindowCheck.configure(background="#d9d9d9")
        self.CustomWindowCheck.configure(disabledforeground="#a3a3a3")
        self.CustomWindowCheck.configure(foreground="#000000")
        self.CustomWindowCheck.configure(highlightbackground="#d9d9d9")
        self.CustomWindowCheck.configure(highlightcolor="black")
        self.CustomWindowCheck.configure(justify=LEFT)
        self.CustomWindowCheck.configure(text='''Set Custom Window Size?''')
        self.CustomWindowCheck.configure(variable=self.windowCheck)
        self.CustomWindowCheck.configure(width=151)
        

        self.TLabel8 = ttk.Label(self.InputOutputFrame)
        self.TLabel8.place(relx=0.19, rely=0.52, height=19, width=43)
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(relief=FLAT)
        self.TLabel8.configure(text='''Width''')
        

        self.WindowWidth = Spinbox(self.InputOutputFrame, from_=1.0, to=5000.0)
        self.WindowWidth.place(relx=0.4, rely=0.52, relheight=0.06
                , relwidth=0.45)
        self.WindowWidth.configure(activebackground="#f9f9f9")
        self.WindowWidth.configure(background="white")
        self.WindowWidth.configure(buttonbackground="#d9d9d9")
        self.WindowWidth.configure(disabledforeground="#a3a3a3")
        self.WindowWidth.configure(foreground="black")
        self.WindowWidth.configure(from_="1.0")
        self.WindowWidth.configure(highlightbackground="black")
        self.WindowWidth.configure(highlightcolor="black")
        self.WindowWidth.configure(insertbackground="black")
        self.WindowWidth.configure(selectbackground="#c4c4c4")
        self.WindowWidth.configure(selectforeground="black")
        self.WindowWidth.configure(textvariable=gui_utils.WindowWidthBox)
        self.WindowWidth.configure(to="5000.0")
        self.WindowWidth.configure(width=95)
        self.WindowWidth['state'] = DISABLED


        self.TLabel7 = ttk.Label(self.InputOutputFrame)
        self.TLabel7.place(relx=0.17, rely=0.6, height=35, width=45)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(relief=FLAT)
        self.TLabel7.configure(text='''Height''')

        
        self.WindowHeight = Spinbox(self.InputOutputFrame, from_=1.0, to=5000.0)
        self.WindowHeight.place(relx=0.4, rely=0.63, relheight=0.06
                , relwidth=0.45)
        self.WindowHeight.configure(activebackground="#f9f9f9")
        self.WindowHeight.configure(background="white")
        self.WindowHeight.configure(buttonbackground="#d9d9d9")
        self.WindowHeight.configure(disabledbackground="#f0f0f0f0f0f0")
        self.WindowHeight.configure(disabledforeground="#a3a3a3")
        self.WindowHeight.configure(foreground="black")
        self.WindowHeight.configure(from_="1.0")
        self.WindowHeight.configure(highlightbackground="black")
        self.WindowHeight.configure(highlightcolor="black")
        self.WindowHeight.configure(insertbackground="black")
        self.WindowHeight.configure(selectbackground="#c4c4c4")
        self.WindowHeight.configure(selectforeground="black")
        self.WindowHeight.configure(textvariable=gui_utils.WindowHeightBox)
        self.WindowHeight.configure(to="5000.0")
        self.WindowHeight.configure(width=95)
        self.WindowHeight['state'] = DISABLED


        self.TLabel1 = ttk.Label(self.InputOutputFrame)
        self.TLabel1.place(relx=0.07, rely=0.74, height=19, width=63)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Top Offest''')


        self.TopOffset = Spinbox(self.InputOutputFrame, from_=0.0, to=5000.0)
        self.TopOffset.place(relx=0.4, rely=0.74, relheight=0.06, relwidth=0.45)
        self.TopOffset.configure(activebackground="#f9f9f9")
        self.TopOffset.configure(background="white")
        self.TopOffset.configure(buttonbackground="#d9d9d9")
        self.TopOffset.configure(disabledforeground="#a3a3a3")
        self.TopOffset.configure(foreground="black")
        self.TopOffset.configure(from_="0.0")
        self.TopOffset.configure(highlightbackground="black")
        self.TopOffset.configure(highlightcolor="black")
        self.TopOffset.configure(insertbackground="black")
        self.TopOffset.configure(selectbackground="#c4c4c4")
        self.TopOffset.configure(selectforeground="black")
        self.TopOffset.configure(textvariable=gui_utils.TopOffsetBox)
        self.TopOffset.configure(to="5000.0")
        self.TopOffset.insert(0,'0')
        self.TopOffset.configure(width=95)
        self.TopOffset['state'] = DISABLED
        

        self.TLabel2 = ttk.Label(self.InputOutputFrame)
        self.TLabel2.place(relx=0.07, rely=0.85, height=19, width=59)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Left Offset''')


        self.LeftOffset = Spinbox(self.InputOutputFrame, from_=0.0, to=5000.0)
        self.LeftOffset.place(relx=0.4, rely=0.85, relheight=0.06, relwidth=0.45)
        self.LeftOffset.configure(activebackground="#f9f9f9")
        self.LeftOffset.configure(background="white")
        self.LeftOffset.configure(buttonbackground="#d9d9d9")
        self.LeftOffset.configure(disabledforeground="#a3a3a3")
        self.LeftOffset.configure(foreground="black")
        self.LeftOffset.configure(from_="0.0")
        self.LeftOffset.configure(highlightbackground="black")
        self.LeftOffset.configure(highlightcolor="black")
        self.LeftOffset.configure(insertbackground="black")
        self.LeftOffset.configure(selectbackground="#c4c4c4")
        self.LeftOffset.configure(selectforeground="black")
        self.LeftOffset.configure(textvariable=gui_utils.LeftOffsetBox)
        self.LeftOffset.configure(to="5000.0")
        self.LeftOffset.insert(0,'0')
        self.LeftOffset.configure(width=95)
        self.LeftOffset['state'] = DISABLED


        self.RunExitFrame = ttk.Frame(top)
        self.RunExitFrame.place(relx=0.5, rely=0.42, relheight=0.22
                , relwidth=0.45)
        self.RunExitFrame.configure(relief=GROOVE)
        self.RunExitFrame.configure(borderwidth="2")
        self.RunExitFrame.configure(relief=GROOVE)
        self.RunExitFrame.configure(width=225)


        self.ExitButton = Button(self.RunExitFrame, command=root.destroy)
        self.ExitButton.place(relx=0.09, rely=0.55, height=54, width=187)
        self.ExitButton.configure(activebackground="#d9d9d9")
        self.ExitButton.configure(activeforeground="#000000")
        self.ExitButton.configure(background="#ec0006")
        self.ExitButton.configure(disabledforeground="#a3a3a3")
        self.ExitButton.configure(font=font18)
        self.ExitButton.configure(foreground="#000000")
        self.ExitButton.configure(highlightbackground="#d9d9d9")
        self.ExitButton.configure(highlightcolor="black")
        self.ExitButton.configure(pady="0")
        self.ExitButton.configure(text='''Exit''')


        self.RunButton = Button(self.RunExitFrame, command=self.runProgram)
        self.RunButton.place(relx=0.09, rely=0.1, height=54, width=187)
        self.RunButton.configure(activebackground="#d9d9d9")
        self.RunButton.configure(activeforeground="#000000")
        self.RunButton.configure(background="#33cf1d")
        self.RunButton.configure(disabledforeground="#a3a3a3")
        self.RunButton.configure(font=font18)
        self.RunButton.configure(foreground="#000000")
        self.RunButton.configure(highlightbackground="#d9d9d9")
        self.RunButton.configure(highlightcolor="black")
        self.RunButton.configure(pady="0")
        self.RunButton.configure(text='''Run''')


        self.EyeBall = ttk.Label(top)
        self.EyeBall.place(relx=0.02, rely=0.02, height=99, width=106)
        self.EyeBall.configure(background="#d9d9d9")
        self.EyeBall.configure(foreground="#000000")
        self.EyeBall.configure(relief=FLAT)
        self.EyeBall.configure(text='''Tlabel''')
        self.EyeBall.configure(width=106)
        self._img1 = PhotoImage(file=os.path.join(FOLDER_PATH, 'eye.gif'))
        self.EyeBall.configure(image=self._img1)


        self.Title = ttk.Label(top)
        self.Title.place(relx=0.3, rely=0.04, height=110, width=496)
        self.Title.configure(background="#d9d9d9")
        self.Title.configure(foreground="#000000")
        self.Title.configure(font=font21)
        self.Title.configure(relief=FLAT)
        self.Title.configure(text='''DeepEye''')


        self.OutputFrame = LabelFrame(top)
        self.OutputFrame.place(relx=0.04, rely=0.66, relheight=0.32
                , relwidth=0.91)
        self.OutputFrame.configure(relief=GROOVE)
        self.OutputFrame.configure(foreground="black")
        self.OutputFrame.configure(text='''Program Output''')
        self.OutputFrame.configure(background="#d9d9d9")
        self.OutputFrame.configure(width=450)


        self.CommandLineOutput = ScrolledListBox(self.OutputFrame)
        self.CommandLineOutput.place(relx=0.02, rely=0.09, relheight=0.87
                , relwidth=0.96)
        #self.CommandLineOutput.pack(side="top", fill="both", expand=True)
        #self.CommandLineOutput.tag_configure("stderr", foreground="#b22222")
        self.CommandLineOutput.configure(background="white")
        self.CommandLineOutput.configure(disabledforeground="#a3a3a3")
        self.CommandLineOutput.configure(font="TkFixedFont")
        self.CommandLineOutput.configure(foreground="black")
        self.CommandLineOutput.configure(highlightbackground="#d9d9d9")
        self.CommandLineOutput.configure(highlightcolor="#d9d9d9")
        self.CommandLineOutput.configure(selectbackground="#c4c4c4")
        self.CommandLineOutput.configure(selectforeground="black")
        self.CommandLineOutput.configure(width=10)
        self.CommandLineOutput.configure(listvariable=gui_utils.CommandLineOutput)
        sys.stdout = TextRedirector(self.CommandLineOutput)
        
    def print_stdout(self):
        '''Illustrate that using 'print' writes to stdout'''
        print ("Example text")

        
    def FlipState(self):
        self.test = self.visualCheck.get()
        self.test2 = self.windowCheck.get()
            
        if self.test2 == 0:
            self.WindowWidth['state'] = DISABLED
            self.WindowHeight['state'] = DISABLED
            self.TopOffset['state'] = DISABLED
            self.LeftOffset['state'] = DISABLED
        elif self.test2 == 1:
            self.WindowWidth['state'] = NORMAL
            self.WindowHeight['state'] = NORMAL
            self.TopOffset['state'] = NORMAL
            self.LeftOffset['state'] = NORMAL
            
        if self.test == 0:
            self.CustomWindowCheck.deselect()
            self.CustomWindowCheck['state'] = DISABLED
            self.WindowWidth['state'] = DISABLED
            self.WindowHeight['state'] = DISABLED
            self.TopOffset['state'] = DISABLED
            self.LeftOffset['state'] = DISABLED
        elif self.test == 1:
            self.CustomWindowCheck['state'] = NORMAL

            
    def runProgram(self):
        print ("Loading...")
        convertedThreshold = int(self.Threshold.get()[:-1])/100
        convertedWindowHeight = 0
        convertedWindowWidth = 0
        convertedTopOffset = 0
        convertedLeftOffset = 0
        
        if self.windowCheck.get() == 1:
            convertedWindowHeight = int(self.WindowHeight.get())
            convertedWindowWidth = int(self.WindowWidth.get())
            convertedTopOffset = int(self.TopOffset.get())
            convertedLeftOffset = int(self.LeftOffset.get())
            
        convertedClassifier = ''
        if self.ClassifierCode.get() == 'Resnet101':
            convertedClassifier = 'faster_rcnn_resnet101_coco_2017_11_08'
        elif self.ClassifierCode.get() == 'Nas':
            convertedClassifier = 'faster_rcnn_nas_coco_2017_11_08'
        elif self.ClassifierCode.get() == 'Inception-Resnet':
            convertedClassifier = 'mask_rcnn_inception_v2_coco_coco_2017_11_08'
            
        convertedDataset = ''
        if self.DatasetCode.get() == 'Coco':
            convertedDataset = 'mscoco'
        elif self.DatasetCode.get() == 'Kitti':
            convertedDataset = 'kitti'

        driving_assistant = DrivingAssistant()
        
        driving_assistant.set_prams(
            convertedClassifier, 
            convertedDataset, 
            convertedThreshold,
            gui_utils.LaneDetection.get(),
            int(self.MonitorId.get()), 
            convertedTopOffset,
            convertedLeftOffset, 
            convertedWindowWidth, 
            convertedWindowHeight)
        driving_assistant.activate()

        root.destroy()
        
class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget
        #self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str)
        self.widget.configure(state="disabled")


# The following code is added to facilitate the Scrolled widgets.
class AutoScroll(object):
    #Configure the scrollbars for a widget.

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        #Hide and show scrollbar as needed.
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    #Creates a ttk Frame with a given master, and use this new frame to
    #place the scrollbars and the widget.
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    #A standard Tkinter Text widget with scrollbars that will
    #automatically show/hide as needed.
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
