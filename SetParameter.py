#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, Mqy 2014.
#

from Tkinter import *


class SetParameter():

    def show_setting_window(self, parameters, commands):
        """ Show a parameter setting window.

        parameters: A list of dictionaries {'parameter name':default_value}
        commands: A dictionary {'name of button': command}
        """
        self.root = Tk()
        self.root.title('Control Widget')

        frame1 = Frame(self.root, padx=5, pady=5)
        frame1.pack(side='top')
        self.entry = []
        for i, parameter in enumerate(parameters):
            label = Label(frame1, text=parameter.items()[0][0] + ' = ')
            label.grid(row=i, column=0, sticky=E)
            self.entry.append(Entry(frame1, width=10))
            self.entry[i].grid(row=i, column=1)
            self.entry[i].delete(0, END)
            self.entry[i].insert(0, parameter.items()[0][1])
        self.entry[0].focus_set()

        frame2 = Frame(self.root, padx=5, pady=5)
        frame2.pack(side='bottom')
        for name, command in commands.items():
            button = Button(frame2, text=name, command=command)
            button.pack(side='left', fill='x')

        self.root.mainloop()

    def quit(self):
        self.root.destroy()
