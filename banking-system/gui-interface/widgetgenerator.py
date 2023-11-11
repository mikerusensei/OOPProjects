import tkinter as tk

class ButtonGenerator(tk.Button):
    def __init__(self, root):
        self.root = root
        self.button = None

    def set_text(self, text):
        self.text = text
        return self
    
    def set_command(self, command):
        self.command = command
        return self
    
class ButtonGeneratorGrid(ButtonGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self
    
    def build(self):
        self.button = tk.Button(self.root, text=self.text, command=self.command)
        self.button.grid(row=self.row, column=self.column)
        return self.button
    
class ButtonGeneratorPack(ButtonGenerator):
    def set_anchor(self, anchor):
        self.anchor = anchor
        return self
    
    def build(self):
        self.button = tk.Button(self.root, text=self.text, command=self.command)
        self.button.pack(anchor=self.anchor)
        return self.button

class LabelGenerator(tk.Label):
    def __init__(self, root):
        self.root = root
        self.label = None

    def set_text(self, text):
        self.text = text
        return self
    
class LabelGeneratorGrid(LabelGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self
    
    def build(self):
        self.label = tk.Label(self.root, text=self.text)
        self.label.grid(row=self.row, column=self.column)
        return self.label

class LabelGeneratorPack(LabelGenerator):
    def set_anchor(self, anchor):
        self.anchor = anchor
        return self
    
    def build(self):
        self.label = tk.Label(self.root, text=self.text)
        self.label.pack(anchor=self.anchor)
        return self.label
    
class FrameGenerator(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.frame = None

class FrameGeneratorGrid(FrameGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self
    
    def build(self):
        self.frame = tk.Frame(self.root, text=self.text)
        self.frame.grid(row=self.row, column=self.column)
        return self.frame
    
class FrameGeneratorPack(FrameGenerator):
    def set_anchor(self, anchor):
        self.anchor = anchor
        return self
    
    def build(self):
        self.frame = tk.Frame(self.root, text=self.text)
        self.frame.grid(row=self.row, column=self.column)
        return self.frame