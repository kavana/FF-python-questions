from Tkinter import *
import ttk
import json
import Tkinter as tk

class App(Frame):
    list_cityinfo = {}
    def __init__(self, parent):
        self.parent = parent
        value_of_combo = None
        self.set_window()
        self.design_grid()

    def set_window(self):
        self.parent.geometry("450x300+100+100")
        self.parent.wm_title("City Information")

    def fetch_data(self):
        with open('ca.json', 'r') as dataf:
            return json.load(dataf)

    def fetch_cities(self, list_cityinfo):
        temp = tuple(sorted([x['name'] for x in self.list_cityinfo]))
        return tuple([x.encode('UTF-8') for x in temp])

    def design_grid(self):
        tk.Label(self.parent, text="City", font=("Arial", 15)).grid(row=0, sticky='W', padx=20, pady=20)
        tk.Label(self.parent, text="County", font=("Arial", 15)).grid(row=1, sticky='W', padx=20, pady=20)
        tk.Label(self.parent, text="Latitude", font=("Arial", 15)).grid(row=2, sticky='W', padx=20, pady=20)
        tk.Label(self.parent, text="Longitude", font=("Arial", 15)).grid(row=3, sticky='W', padx=20, pady=20)
        # textbox designs
        self.list_cityinfo = self.fetch_data()
        sor_cities = self.fetch_cities(self.list_cityinfo)
        self.cbox_value = StringVar()
        self.cbox = ttk.Combobox(self.parent, textvariable=self.cbox_value)
        self.cbox['values'] = sor_cities
        self.cbox.current(0)
        self.update_selection()
        self.cbox.grid(row=0, column=1, padx=100, pady=20, ipady=4, ipadx=34)
        self.cbox.bind("<<ComboboxSelected>>", self.update_selection)

    def update_selection(self,event=None):
        self.value_of_combo = self.cbox.get()
        print self.value_of_combo
        data = self.get_values(self.value_of_combo)
        cou_var = tk.StringVar(self.parent, value=None)
        lat_var = tk.StringVar(self.parent, value=None)
        lon_var = tk.StringVar(self.parent, value=None)

        tk.Entry(self.parent, width=30, textvariable=cou_var).grid(row=1, column=1, padx=100, pady=20, ipady=4)
        tk.Entry(self.parent, width=30, textvariable=lat_var).grid(row=2, column=1, padx=100, pady=20, ipady=4)
        tk.Entry(self.parent, width=30, textvariable=lon_var).grid(row=3, column=1, padx=100, pady=20, ipady=4)
        cou_var.set(data['full_county_name'])
        lat_var.set(data['primary_latitude'])
        lon_var.set(data['primary_longitude'])
        print "after display"

    def get_values(self, city_name):
        info = [x for x in self.list_cityinfo if x['name'] == city_name]
        return info[0]


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    print "exit"