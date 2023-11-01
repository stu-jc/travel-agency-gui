import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class View:
    def __init__(self, root):
        #could add a thing to change the icon after close btn is pressed
        self.root = root
        self.root.title('Login')
        # self.root.geometry("300x200")
        photo = tk.PhotoImage(file="/Users/jc/Desktop/A2.zip/icons/login_icon.png")
        self.root.iconphoto(True, photo)
        self.root.iconbitmap(bitmap='/Users/jc/Desktop/A2.zip/icon.icns') #not necessary
        frame1 = ttk.Frame(self.root, width=200, height=150)
        frame1.pack(side=TOP, expand=True, fill=BOTH, anchor='n')
        frame1.config(border=True, padding=(20, 30))
        header_style = ttk.Style()
        header_style.configure('Header.TLabel', foreground="#168FC1", font=('Helvetica', 12, 'bold'))
        ttk.Label(frame1, text='Login', style='Header.TLabel').pack(anchor='center', expand=True, fill=Y)
        button_style = ttk.Style()
        button_style.configure('B.TButton', font=('Arial Narrow', 11, 'bold'), relief='flat')
        button_style.map('B.TButton',
                         # foreground=[('active', 'white'), ('disabled', 'white')],
                         # background=[('active', 'red'), ('disabled', 'blue'), ('pressed', 'green')],
                         bordercolour=[('active', 'red'), ('disabled', 'blue')]
                        )
        # event binding for hover on buttons
        frame_style = ttk.Style()
        frame_style.configure("F.TFrame", border=True, borderwidth=10, bordercolour='black', padding=(20, 20))
        label_style = ttk.Style()
        label_style.configure('L.TLabel', foreground='#168FC1', font=('Helvetica', 10, 'bold'))
        entry_style = ttk.Style()
        entry_style.configure('E.TEntry', bordercolour="#E2F3FF", borderwidth=0)
        frame1.config(relief='raised')
        # btn_style = ttk.Style()
        # btn_style.theme_use('default')
        # btn_style.theme_use('clam')

        frame2 = ttk.Frame(self.root)
        frame2.pack(side=TOP, expand=True, fill=BOTH)
        frame2.config(border=True, borderwidth=20)
        ttk.Label(frame2, text='Username:', style='L.TLabel').grid(row=0, column=0)
        self.login_tf = ttk.Entry(frame2, style='E.TEntry')
        self.login_tf.grid(row=0, column=1)
        ttk.Label(frame2, text='Password:', style='L.TLabel').grid(row=1, column=0)
        self.pwd_tf = ttk.Entry(frame2, style='E.TEntry')
        self.pwd_tf.grid(row=1, column=1)
        frame3 = ttk.Frame(self.root)
        frame3.pack(side=BOTTOM, expand=True, fill=X, anchor='s')
        frame3.configure(border=0)
        # self.login_btn = ttk.Button(frame3, text='Login', command=self.login_cmd, style='B.TButton')
        self.login_btn = tk.Button(frame3, text='Login', command=self.login_cmd, highlightbackground='#168FC1',
                                   foreground='white')
        self.login_btn.pack(side=tk.LEFT, fill=X, expand=True)
        ttk.Button(frame3, text='Exit', style='B.TButton', command=root.destroy).pack(side=tk.RIGHT, fill=X, expand=True)
        self.controller = None
        self.login_btn.config(state=DISABLED)
        self.pwd_tf.bind('<Return>', lambda e: self.login_cmd())
        self.login_tf.bind('<KeyRelease>', lambda e: self.set_button())
        self.pwd_tf.bind('<KeyRelease>', lambda e: self.set_button())

    def set_controller(self, controller):
        self.controller = controller

    def set_button(self):
        if len(self.login_tf.get()) != 0 and len(self.pwd_tf.get()) != 0:
            self.login_btn.config(state=NORMAL)
        else:
            self.login_btn.config(state=DISABLED)

    def login_cmd(self):
        if self.controller:
            self.controller.login(self.login_tf.get(), self.pwd_tf.get())
            if self.controller.logged_in_user is None:
                ErrorWindow('Incorrect details', 'Enter correct details')
            else:
                AgencyWindow(self.controller.logged_in_user, self.controller)
                self.root.withdraw()


class AgencyWindow:
    def __init__(self, user, agency_controller):
        self.user = user
        self.agency_controller = agency_controller
        self.agency_window = Toplevel()
        self.agency_window.title('Agency Window')
        # self.agency_window.geometry("600x600")
        photo = tk.PhotoImage(file="/Users/jc/Desktop/A2.zip/icons/agency_icon.png")
        self.agency_window.iconphoto(False, photo)
        frame1 = ttk.Frame(self.agency_window)
        frame1.pack(padx=10, pady=(0,15))
        image_path = "/Users/jc/Desktop/A2.zip/images/agency.png"
        original_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(original_image)
        label = tk.Label(frame1, image=tk_image)
        label.pack()
        label.image = tk_image

        separator = ttk.Separator(self.agency_window, orient="horizontal")
        separator.pack(fill=X)

        frame2 = ttk.Frame(self.agency_window)
        frame2.pack(side=TOP, expand=1, pady=20)
        ttk.Label(frame2, text='Hi ' + user.get_name() + ', welcome to the Prog2 Travel Agency', style='Header.TLabel').pack()
        separator = ttk.Separator(self.agency_window, orient="horizontal")
        separator.pack(fill=X)
        frame3 = ttk.Frame(self.agency_window)
        frame3.pack(side=BOTTOM, expand=True, pady=(15,0), fill=X)
        ttk.Button(frame3, text='Explore Flights', style='B.TButton', command=self.exp_flights).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Explore Destinations', style='B.TButton', command=self.exp_destinations).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Book a Trip', style='B.TButton', command=self.book_trip).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Exit', style='B.TButton', command=exit).pack(side=tk.LEFT, expand=True, fill=X)

    def exp_flights(self):
        FlightsMenu(self.user, self.agency_controller)

    def exp_destinations(self):
        DestinationsMenu(self.user, self.agency_controller)

    def book_trip(self):
        TripsMenu(self.user, self.agency_controller)


class ErrorWindow:
    def __init__(self, exception, error_msg):
        self.error_window = Toplevel()
        self.error_window.title('ERROR')
        photo = tk.PhotoImage(file="/Users/jc/Desktop/A2.zip/icons/error_icon.png")
        self.error_window.iconphoto(True, photo)
        frame1 = ttk.Frame(self.error_window)
        frame1.pack()
        self.exc_label = ttk.Label(frame1, text=f'{exception}', style='Header.TLabel', foreground='red')
        self.msg_label = ttk.Label(frame1, text=f'{error_msg}')
        self.exc_label.pack()
        self.msg_label.pack()


class FlightsMenu:
    def __init__(self, user, controller):
        self.flights_window = Toplevel()
        self.flights_window.title('Flights Menu')
        # self.flights_window.geometry("600x600")
        photo = tk.PhotoImage(file="/Users/jc/Desktop/A2.zip/icons/flights_icon.png")
        self.flights_window.iconphoto(True, photo)
        self.fm_controller = controller
        self.user = user
        frame1 = ttk.Frame(self.flights_window)
        frame1.pack(side=TOP, fill=BOTH, expand=True, pady=(0,15))
        image_path = "/Users/jc/Desktop/A2.zip/images/flight.png"
        original_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(original_image)
        label = tk.Label(frame1, image=tk_image)
        label.pack()
        label.image = tk_image

        separator = ttk.Separator(self.flights_window, orient="horizontal")
        separator.pack(fill=X)
        frame2 = ttk.Frame(self.flights_window, style="Custom.TFrame")
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=20)
        ttk.Label(frame2, text='Hi '+user.get_name()+', welcome to the Flights section', style='Header.TLabel').pack()
        separator = ttk.Separator(self.flights_window, orient="horizontal")
        separator.pack(fill=X)

        frame3 = ttk.Frame(self.flights_window)
        frame3.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(15,0))
        btn_width = 9
        ttk.Button(frame3, text='View All Flights', command=lambda: self.view_all_flights(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='View Flights by Country', command=lambda: self.view_filtered_flights(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Add Flight', command=lambda: self.add_flight(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Remove Flight', command=lambda: self.remove_flight(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Close', command=self.flights_window.destroy, width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)

    def view_all_flights(self):
        ViewAllFlights(self.fm_controller)

    def view_filtered_flights(self):
        ViewFilteredFlights(self.fm_controller)

    def add_flight(self):
        if self.fm_controller:
            AddFlight(self.fm_controller)

    def remove_flight(self):
        if self.fm_controller:
            RemoveFlight(self.fm_controller)


class ViewAllFlights:
    def __init__(self, controller):
        self.view_all_flights = Toplevel(width=600, height=600)
        self.vaf_controller = controller
        self.view_all_flights.title('View All Fights')
        frame1 = ttk.Frame(self.view_all_flights)
        # frame1.pack() #this is where image goes
        frame2 = ttk.Frame(self.view_all_flights)
        frame2.pack(side=TOP, fill=BOTH, expand=True)
        ttk.Label(frame2, text='Flights', style='Header.TLabel').pack()

        outer_frame = ttk.Frame(self.view_all_flights, width=600, height=300)
        outer_frame.pack(side=TOP, expand=1)
        canvas = tk.Canvas(outer_frame, width=1000, height=300)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = ttk.Scrollbar(outer_frame, orient='vertical', command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        self.inner_frame = ttk.Frame(canvas, width=1000, height=300)
        self.inner_frame.pack()
        canvas.create_window((0, 0), window=self.inner_frame, anchor='nw')

        columns = ('Airline', 'FN', 'Takeoff', 'Landing', 'Cost')
        self.treeview = ttk.Treeview(self.inner_frame, columns=columns, show="headings")
        self.treeview.pack()
        self.treeview.heading(column=0, text='Airline')
        self.treeview.heading(column=1, text='Flight Number')
        self.treeview.heading(column=2, text='Takeoff')
        self.treeview.heading(column=3, text='Landing')
        self.treeview.heading(column=4, text='Cost')

        frame4 = ttk.Frame(self.view_all_flights)
        frame4.pack(side=BOTTOM, fill=X, expand=True)
        ttk.Button(frame4, text='Close', command=self.view_all_flights.destroy).pack(side=BOTTOM, fill=BOTH, expand=True)
        self.fill_table()
        self.view_all_flights.bind('<Return>', lambda e: self.fill_table())
        # !! bind this to the event of add and remove buttons being clicked
        self.inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def clear_treeview(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def fill_table(self):
        self.clear_treeview()
        lst = self.vaf_controller.model.agency.flights.flights
        data = []
        for f in lst:
            flight = (f.airline, f.flight_no, f.takeoff, f.landing, f.cost)
            data.append(flight)

        for a,fn,t,l,c in data:
            self.treeview.insert('', 'end', values=(a,fn,t,l,c))


class ViewFilteredFlights:
    def __init__(self, controller):
        self.view_ff = Toplevel(width=600, height=600)
        self.v_ff_controller = controller

        self.view_ff.title('View Flights by Country')
        frame1 = ttk.Frame(self.view_ff)
        frame1.pack()
        frame2 = ttk.Frame(self.view_ff)
        frame2.pack(side=TOP, fill=BOTH, expand=True)
        ttk.Label(frame2, text='Flights', foreground='blue', width=20, font=('Arial', 16, 'bold')).pack()
        self.input_entry = ttk.Entry(frame2)
        self.input_entry.pack(side=tk.RIGHT, fill=X, expand=True)

        outer_frame = ttk.Frame(self.view_ff, width=600, height=300)
        outer_frame.pack(side=TOP, expand=1)
        canvas = tk.Canvas(outer_frame, width=1000, height=300)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = ttk.Scrollbar(outer_frame, orient='vertical', command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        self.inner_frame = ttk.Frame(canvas, width=1000, height=300)
        self.inner_frame.pack()
        canvas.create_window((0, 0), window=self.inner_frame, anchor='nw')

        columns = ('Airline', 'FN', 'Takeoff', 'Landing', 'Cost')
        self.treeview = ttk.Treeview(self.inner_frame, columns=columns, show="headings")
        self.treeview.pack()
        self.treeview.heading(column=0, text='Airline')
        self.treeview.heading(column=1, text='Flight Number')
        self.treeview.heading(column=2, text='Takeoff')
        self.treeview.heading(column=3, text='Landing')
        self.treeview.heading(column=4, text='Cost')

        frame4 = ttk.Frame(self.view_ff)
        frame4.pack(fill=X, expand=True)
        ttk.Button(frame4, text='Close', command=self.view_ff.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)
        self.fill_table()
        self.input_entry.bind('<KeyRelease>', lambda e: self.filtered_table())
        self.inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def clear_treeview(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def fill_table(self):
        self.clear_treeview()
        lst = self.v_ff_controller.model.agency.flights.flights
        data = []
        for f in lst:
            flight = (f.airline, f.flight_no, f.takeoff, f.landing, f.cost)
            data.append(flight)

        for a, fn, t, l, c in data:
            self.treeview.insert('', 'end', values=(a, fn, t, l, c))

    def filtered_table(self):
        self.clear_treeview()
        lst = self.v_ff_controller.view_filtered_flights(self.input_entry.get())
        if len(lst) == 0:
            self.treeview.insert('', 'end', values=('No Flights',))
        else:
            data = []
            for f in lst:
                flight = (f.airline, f.flight_no, f.takeoff, f.landing, f.cost)
                data.append(flight)

            for a, fn, t, l, c in data:
                self.treeview.insert('', 'end', values=(a, fn, t, l, c))


class AddFlight:
    def __init__(self, controller):
        self.af_controller = controller
        self.add_flights = Toplevel()

        self.add_flights.title('Add Flights')
        self.add_flights.geometry("600x600")
        frame1 = ttk.Frame(self.add_flights)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # picture goes here

        frame2 = ttk.Frame(self.add_flights)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Label(frame2, text='Add a Flight', style='Header.TLabel').pack()

        frame3 = ttk.Frame(self.add_flights)
        frame3.pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Label(frame3, text='Airline:').grid(row=0, column=0)
        ttk.Label(frame3, text='Flight Number:').grid(row=1, column=0)
        ttk.Label(frame3, text='Takeoff:').grid(row=2, column=0)
        ttk.Label(frame3, text='Landing:').grid(row=3, column=0)
        ttk.Label(frame3, text='Cost:').grid(row=4, column=0)

        self.airline_tf = ttk.Entry(frame3)
        self.fn_tf = ttk.Entry(frame3)
        self.takeoff_tf = ttk.Entry(frame3)
        self.landing_tf = ttk.Entry(frame3)
        self.cost_tf = ttk.Entry(frame3)
        self.airline_tf.grid(row=0, column=1)
        self.fn_tf.grid(row=1, column=1)
        self.takeoff_tf.grid(row=2, column=1)
        self.landing_tf.grid(row=3, column=1)
        self.cost_tf.grid(row=4, column=1)

        frame4 = ttk.Frame(self.add_flights)
        frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.add_btn = ttk.Button(frame4, text='Add Flight', command=self.add_the_flight)
        self.add_btn.pack(side=tk.LEFT, fill=BOTH, expand=True)
        self.add_btn.config(state=DISABLED)
        ttk.Button(frame4, text='Close', command=self.add_flights.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)
        self.airline_tf.bind('<KeyRelease>', lambda e: self.set_btn())
        self.cost_tf.bind('<KeyRelease>', lambda e: self.set_btn())

    def add_the_flight(self):
        try:
            self.af_controller.add_flight(self.airline_tf.get(), self.fn_tf.get(),  self.takeoff_tf.get(), self.landing_tf.get(), self.cost_tf.get())
            self.add_flights.destroy()
        except Exception as e:
            ErrorWindow(Exception, e)

    def set_btn(self):
        if len(self.airline_tf.get()) != 0 and len(self.fn_tf.get()) != 0 and len(self.takeoff_tf.get()) != 0 and len(self.landing_tf.get()) != 0 and len(self.cost_tf.get()) != 0:
            self.add_btn.config(state=NORMAL)
        else:
            self.add_btn.config(state=DISABLED)


class RemoveFlight:
    def __init__(self, controller):
        self.rf_controller = controller
        self.remove_flight = Toplevel()

        self.remove_flight.title('Remove Flight')
        self.remove_flight.geometry("600x600")
        frame1 = ttk.Frame(self.remove_flight)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # picture goes here

        frame2 = ttk.Frame(self.remove_flight)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Label(frame2, text='Remove a Flight', style='Header.TLabel').pack()

        frame3 = ttk.Frame(self.remove_flight)
        frame3.pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Label(frame3, text='Takeoff:').grid(row=0, column=0)
        ttk.Label(frame3, text='Landing:').grid(row=1, column=0)
        self.take_tf = ttk.Entry(frame3)
        self.land_tf = ttk.Entry(frame3)
        self.take_tf.grid(row=0, column=1)
        self.land_tf.grid(row=1, column=1)

        frame4 = ttk.Frame(self.remove_flight)
        frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.remove_btn = ttk.Button(frame4, text='Remove Flight', command=self.remove_the_flight)
        self.remove_btn.pack(side=tk.LEFT, fill=BOTH, expand=True)
        self.remove_btn.config(state=DISABLED)
        ttk.Button(frame4, text='Close', command=self.remove_flight.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)

        self.take_tf.bind('<KeyRelease>', lambda e: self.set_btn())
        self.land_tf.bind('<KeyRelease>', lambda e: self.set_btn())

    def remove_the_flight(self):
        try:
            self.rf_controller.remove_flight(self.take_tf.get(), self.land_tf.get())
            self.remove_flight.destroy()
        except Exception as e:
            ErrorWindow(Exception, e)

    def set_btn(self):
        if len(self.take_tf.get()) != 0 and len(self.land_tf.get()) != 0:
            self.remove_btn.config(state=NORMAL)
        else:
            self.remove_btn.config(state=DISABLED)


class DestinationsMenu:
    def __init__(self, user, controller):
        self.destinations_menu = Toplevel()
        self.destinations_menu.title('Destinations Menu')
        photo = tk.PhotoImage(file="/Users/jc/Desktop/A2.zip/icons/destinations_icon.png")
        self.destinations_menu.iconphoto(True, photo)
        self.user = user
        self.dm_controller = controller
        # self.destinations_menu.geometry("600x600")
        frame1 = ttk.Frame(self.destinations_menu)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(0, 15))
        image_path = "/Users/jc/Desktop/A2.zip/images/destination.png"
        original_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(original_image)
        label = tk.Label(frame1, image=tk_image)
        label.pack()
        label.image = tk_image

        separator = ttk.Separator(self.destinations_menu, orient="horizontal")
        separator.pack(fill=X)
        frame2 = ttk.Frame(self.destinations_menu)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=20)
        ttk.Label(frame2, text='Hi ' + user.get_name() + ', welcome to the Destinations section', style='Header.TLabel').pack()
        separator = ttk.Separator(self.destinations_menu, orient="horizontal")
        separator.pack(fill=X)

        frame3 = ttk.Frame(self.destinations_menu)
        frame3.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(15,0))
        btn_width = 9
        ttk.Button(frame3, text='View All Destinations', command=lambda: self.view_destinations(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='View Destinations by Country', command=lambda: self.view_filtered_destinations(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Add Destinations', command=lambda: self.add_destinations(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Remove Destinations', command=lambda: self.remove_destinations(), width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Close', command=self.destinations_menu.destroy, width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)

    def view_destinations(self):
        ViewAllDestinations(self.dm_controller)

    def view_filtered_destinations(self):
        ViewFilteredDestinations(self.dm_controller)

    def add_destinations(self):
        AddDestination(self.dm_controller)

    def remove_destinations(self):
        RemoveDestination(self.dm_controller)


class ViewAllDestinations:   #it doesn't auto update, need to fix that
    def __init__(self, controller):
        self.view_all_destinations = Toplevel()
        self.vad_controller = controller
        # self.view_all_destinations.geometry("600x600")
        self.view_all_destinations.title('View All Destinations')
        frame1 = tk.Frame(self.view_all_destinations)
        frame1.pack(pady=(0,15))
        image_path = "/Users/jc/Desktop/A2.zip/images/destination.png"
        original_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(original_image)
        label = tk.Label(frame1, image=tk_image, width=1000, height=300)
        label.pack()
        label.image = tk_image

        separator = ttk.Separator(self.view_all_destinations, orient="horizontal")
        separator.pack(fill=X)
        frame2 = ttk.Frame(self.view_all_destinations)
        frame2.pack(side=TOP, fill=BOTH, expand=True, pady=25)
        ttk.Label(frame2, text='Destinations', style='Header.TLabel').pack()
        separator = ttk.Separator(self.view_all_destinations, orient="horizontal")
        separator.pack(fill=X)

        self.frame3 = ttk.Frame(self.view_all_destinations)
        self.frame3.pack(pady=(15,0), fill=BOTH, expand=True)
        columns = ('Name', 'Country')
        treev_style = ttk.Style()
        # treev_style.theme_use('clam')
        treev_style.configure('Treeview.Heading', foreground="#168FC1", background='lightgrey', font=('Arial', 16, 'bold'))
        self.t = ttk.Treeview(self.frame3, columns=columns, show="headings", )
        self.t.pack(fill=BOTH, expand=True)
        # self.t.place(width=1000, height=300)
        self.t.heading(column=0, text='Name')
        self.t.heading(column=1, text='Country')
        frame4 = ttk.Frame(self.view_all_destinations)
        frame4.pack(side=BOTTOM, fill=X, expand=True)
        ttk.Button(frame4, text='Close', command=self.view_all_destinations.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)
        self.lst = self.vad_controller.model.agency.destinations.destinations
        # self.lst_var = tk.IntVar()
        # self.lst_var.set(len(self.lst))
        # self.lst_var.trace("w", lambda *args: print('called'))
        # to make this work, this variable has to be updated everywhere whenever a change is made
        self.view_all_destinations.bind('<Return>', lambda e: self.fill_table()) #bind this to the event of buttons being clicked
        self.fill_table()

    def clear_treeview(self):
        for item in self.t.get_children():
            self.t.delete(item)

    def fill_table(self):
        self.clear_treeview()
        data = []
        for d in self.lst:
            desti = (d.name, d.country)
            data.append(desti)

        for index, (n,c) in enumerate(data):
            num = index+1
            if num % 2 != 0:
                self.t.insert('', 'end', values=(n, c), tags=('oddrow',))
            else:
                self.t.insert('', 'end', values=(n, c), tags=('evenrow',))

            self.t.tag_configure('evenrow', background='lightgrey', font=("Arial", 11))
            self.t.tag_configure('oddrow', font=("Arial", 11))
            # self.t.tag_configure('heading', font=("Arial", 14, "bold"), foreground="green")
#           if n index is odd: do one with tag oddrow


class ViewFilteredDestinations:
    #doesn't need to be auto updating to add and remove destis
    def __init__(self, controller):
        self.view_filtered_d = Toplevel()
        self.vf_controller = controller
        self.view_filtered_d.geometry("600x600")
        self.view_filtered_d.title('View Destinations by Country')
        frame1 = ttk.Frame(self.view_filtered_d)
        frame1.pack()
        frame2 = ttk.Frame(self.view_filtered_d)
        frame2.pack(side=TOP, fill=BOTH, expand=True)
        ttk.Label(frame2, text='Destinations', foreground='blue', width=20, font=('Arial', 16, 'bold')).pack()
        self.input_entry = ttk.Entry(frame2)
        self.input_entry.pack(side=tk.RIGHT, fill=X, expand=True)

        self.frame3 = ttk.Frame(self.view_filtered_d)
        self.frame3.pack()

        columns = ('Name', 'Country')
        self.treeview = ttk.Treeview(self.frame3, columns=columns, show="headings")
        self.treeview.pack()
        self.treeview.heading(column=0, text='Name')
        self.treeview.heading(column=1, text='Country')

        frame4 = ttk.Frame(self.view_filtered_d)
        frame4.pack(fill=X, expand=True)
        ttk.Button(frame4, text='Close', command=self.view_filtered_d.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)
        self.fill_table()
        self.input_entry.bind('<KeyRelease>', lambda e: self.filtered_table())

    def clear_treeview(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def fill_table(self):
        self.clear_treeview()
        lst = self.vf_controller.model.agency.destinations.destinations
        data = []
        for d in lst:
            desti = (d.name, d.country)
            data.append(desti)

        for n, c in data:
            self.treeview.insert('', 'end', values=(n, c))

    def filtered_table(self):
        self.clear_treeview()
        lst = self.vf_controller.view_filtered_destinations(self.input_entry.get())
        if len(lst) == 0:
            self.treeview.insert('', 'end', values=('No Destinations',))
        else:
            data = []
            for d in lst:
                desti = (d.name, d.country)
                data.append(desti)

            for n, c in data:
                self.treeview.insert('', 'end', values=(n, c))


class AddDestination:
    def __init__(self, controller):
        self.add_destination = Toplevel()
        self.ad_controller = controller

        self.add_destination.title('Add Destination')
        self.add_destination.geometry("600x600")
        frame1 = ttk.Frame(self.add_destination)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # picture goes here

        frame2 = ttk.Frame(self.add_destination)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Label(frame2, text='Add a Destination', style='Header.TLabel').pack()

        frame3 = ttk.Frame(self.add_destination)
        frame3.pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Label(frame3, text='Name:').grid(row=0, column=0)
        ttk.Label(frame3, text='Country:').grid(row=1, column=0)
        self.name_tf = ttk.Entry(frame3)
        self.country_tf = ttk.Entry(frame3)
        self.name_tf.grid(row=0, column=1)
        self.country_tf.grid(row=1, column=1)

        frame4 = ttk.Frame(self.add_destination)
        frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.add_d_btn = ttk.Button(frame4, text='Add Destination', command=self.add_the_destination)
        self.add_d_btn.pack(side=tk.LEFT, fill=BOTH, expand=True)
        self.add_d_btn.config(state=DISABLED)
        ttk.Button(frame4, text='Close', command=self.add_destination.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)

        self.name_tf.bind('<KeyRelease>', lambda e: self.set_btn())
        self.country_tf.bind('<KeyRelease>', lambda e: self.set_btn())

    def add_the_destination(self):
        try:
            self.ad_controller.add_destination(self.name_tf.get(), self.country_tf.get())
            self.add_destination.destroy()
        except Exception as e:
            ErrorWindow(Exception, e)

    def set_btn(self):
        if len(self.name_tf.get()) != 0 and len(self.country_tf.get()) != 0:
            self.add_d_btn.config(state=NORMAL)
        else:
            self.add_d_btn.config(state=DISABLED)


class RemoveDestination:
    def __init__(self, controller):
        self.ad_controller = controller
        self.remove_destination = Toplevel()

        self.remove_destination.title('Remove Destination')
        self.remove_destination.geometry("600x600")
        frame1 = ttk.Frame(self.remove_destination)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # picture goes here

        frame2 = ttk.Frame(self.remove_destination)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Label(frame2, text='Remove a Destination', style='Header.TLabel').pack()

        frame3 = ttk.Frame(self.remove_destination)
        frame3.pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Label(frame3, text='Name:').grid(row=0, column=0)
        ttk.Label(frame3, text='Country:').grid(row=1, column=0)
        self.name_tf = ttk.Entry(frame3)
        self.country_tf = ttk.Entry(frame3)
        self.name_tf.grid(row=0, column=1)
        self.country_tf.grid(row=1, column=1)

        frame4 = ttk.Frame(self.remove_destination)
        frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.add_d_btn = ttk.Button(frame4, text='Remove Destination', command=self.remove_the_destination)
        self.add_d_btn.pack(side=tk.LEFT, fill=BOTH, expand=True)
        self.add_d_btn.config(state=DISABLED)
        ttk.Button(frame4, text='Close', command=self.remove_destination.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)

        self.name_tf.bind('<KeyRelease>', lambda e: self.set_btn())
        self.country_tf.bind('<KeyRelease>', lambda e: self.set_btn())

    def remove_the_destination(self):
        try:
            self.ad_controller.remove_destination(self.name_tf.get(), self.country_tf.get())
            self.remove_destination.destroy()
        except Exception as e:
            ErrorWindow(Exception, e)

    def set_btn(self):
        if len(self.name_tf.get()) != 0 and len(self.country_tf.get()) != 0:
            self.add_d_btn.config(state=NORMAL)
        else:
            self.add_d_btn.config(state=DISABLED)


class TripsMenu:
    def __init__(self, user, controller):
        self.trips_menu = Toplevel()
        self.trips_menu.title('Trips Menu')
        photo = tk.PhotoImage(file="/Users/jc/Desktop/A2.zip/icons/trip_icon.png")
        self.trips_menu.iconphoto(True, photo)
        # self.trips_menu.geometry("600x600")
        self.tm_controller = controller
        frame1 = ttk.Frame(self.trips_menu)
        frame1.pack(side=TOP, fill=tk.BOTH, expand=True, pady=(0,15))
        image_path = "/Users/jc/Desktop/A2.zip/images/trip.png"
        original_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(original_image)
        label = tk.Label(frame1, image=tk_image)
        label.pack()
        label.image = tk_image
        separator = ttk.Separator(self.trips_menu, orient="horizontal")
        separator.pack(fill=X)
        frame2 = ttk.Frame(self.trips_menu)
        frame2.pack(side=TOP, fill=tk.BOTH, expand=True, pady=20)
        ttk.Label(frame2, text='Hi ' + user.get_name() + ', welcome to the Trips section', style='Header.TLabel').pack()
        separator = ttk.Separator(self.trips_menu, orient="horizontal")
        separator.pack(fill=X)


        frame3 = ttk.Frame(self.trips_menu)
        frame3.pack(side=BOTTOM, fill=X, expand=True, pady=(15,0))
        btn_width = 9
        ttk.Button(frame3, text='Add Destination', command=self.add_destination, width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Remove Destination', command=self.remove_destination, width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Add Connecting Flights', command=self.add_connecting_flights, width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='View Trip', command=self.view_trip, width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)
        ttk.Button(frame3, text='Close', command=self.trips_menu.destroy, width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)

        # self.destinations_menu.title('Destinations Menu')
        # photo = tk.PhotoImage(file="/Users/jc/Desktop/A2.zip/icons/destinations_icon.png")
        # self.destinations_menu.iconphoto(True, photo)
        # self.user = user
        # self.dm_controller = controller
        # # self.destinations_menu.geometry("600x600")
        # frame1 = ttk.Frame(self.destinations_menu)
        # frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(0, 15))

        # image_path = "/Users/jc/Desktop/A2.zip/images/destination.png"
        # original_image = Image.open(image_path)
        # tk_image = ImageTk.PhotoImage(original_image)
        # label = tk.Label(frame1, image=tk_image)
        # label.pack()
        # label.image = tk_image
        #
        # separator = ttk.Separator(self.destinations_menu, orient="horizontal")
        # separator.pack(fill=X)
        # frame2 = ttk.Frame(self.destinations_menu)
        # frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=20)
        # ttk.Label(frame2, text='Hi ' + user.get_name() + ', welcome to the Destinations section',
        #           style='Header.TLabel').pack()
        # separator = ttk.Separator(self.destinations_menu, orient="horizontal")
        # separator.pack(fill=X)
        #
        # frame3 = ttk.Frame(self.destinations_menu)
        # frame3.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(15, 0))
        # btn_width = 9
        # ttk.Button(frame3, text='View All Destinations', command=lambda: self.view_destinations(),
        #            width=btn_width).pack(side=tk.LEFT, expand=True, fill=X)

    def set_tm_controller(self, ctrl):
        self.tm_controller = ctrl

    def add_destination(self):
        AddTripDestination(self.tm_controller)

    def remove_destination(self):
        RemoveTripDestination(self.tm_controller)

    def add_connecting_flights(self):
        try:
            self.tm_controller.add_connecting_flights()
        except Exception as e:
            ErrorWindow(Exception, e)

    def view_trip(self):
        #this is gonna have to be a treeview so I can do something when it's selected
        ViewTrip(self.tm_controller)


class AddTripDestination:
    def __init__(self, ctrl):
        self.add_trip_d = Toplevel()
        self.atd_controller = ctrl

        self.add_trip_d.title('Add Destination')
        self.add_trip_d.geometry("600x600")
        frame1 = ttk.Frame(self.add_trip_d)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # picture goes here

        frame2 = ttk.Frame(self.add_trip_d)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Label(frame2, text='Add a Destination', style='Header.TLabel').pack()

        frame3 = ttk.Frame(self.add_trip_d)
        frame3.pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Label(frame3, text='Name:').grid(row=0, column=0)
        ttk.Label(frame3, text='Country:').grid(row=1, column=0)
        self.name_tf = ttk.Entry(frame3)
        self.country_tf = ttk.Entry(frame3)
        self.name_tf.grid(row=0, column=1)
        self.country_tf.grid(row=1, column=1)

        frame4 = ttk.Frame(self.add_trip_d)
        frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.add_d_btn = ttk.Button(frame4, text='Add Destination', command=self.add_the_destination)
        self.add_d_btn.pack(side=tk.LEFT, fill=BOTH, expand=True)
        self.add_d_btn.config(state=DISABLED)
        ttk.Button(frame4, text='Close', command=self.add_trip_d.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)

        self.name_tf.bind('<KeyRelease>', lambda e: self.set_btn())
        self.country_tf.bind('<KeyRelease>', lambda e: self.set_btn())

    def add_the_destination(self):
        try:
            self.atd_controller.add_trip_destination(self.name_tf.get(), self.country_tf.get())
            self.add_trip_d.destroy()
        except Exception as e:
            ErrorWindow(Exception, e)

    def set_btn(self):
        if len(self.name_tf.get()) != 0 and len(self.country_tf.get()) != 0:
            self.add_d_btn.config(state=NORMAL)
        else:
            self.add_d_btn.config(state=DISABLED)


class RemoveTripDestination:
    def __init__(self, ctrl):
        self.rtd_c = ctrl
        self.remove_trip_d = Toplevel()

        self.remove_trip_d.title('Remove Destination')
        self.remove_trip_d.geometry("600x600")
        frame1 = ttk.Frame(self.remove_trip_d)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # picture goes here

        frame2 = ttk.Frame(self.remove_trip_d)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Label(frame2, text='Remove a Destination', style='Header.TLabel').pack()

        frame3 = ttk.Frame(self.remove_trip_d)
        frame3.pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Label(frame3, text='Name:').grid(row=0, column=0)
        ttk.Label(frame3, text='Country:').grid(row=1, column=0)
        self.name_tf = ttk.Entry(frame3)
        self.country_tf = ttk.Entry(frame3)
        self.name_tf.grid(row=0, column=1)
        self.country_tf.grid(row=1, column=1)

        frame4 = ttk.Frame(self.remove_trip_d)
        frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.add_d_btn = ttk.Button(frame4, text='Remove Destination', command=self.remove_the_destination)
        self.add_d_btn.pack(side=tk.LEFT, fill=BOTH, expand=True)
        self.add_d_btn.config(state=DISABLED)
        ttk.Button(frame4, text='Close', command=self.remove_trip_d.destroy).pack(side=tk.RIGHT, fill=BOTH, expand=True)

        self.name_tf.bind('<KeyRelease>', lambda e: self.set_btn())
        self.country_tf.bind('<KeyRelease>', lambda e: self.set_btn())

    def remove_the_destination(self):
        try:
            self.rtd_c.remove_trip_destination(self.name_tf.get(), self.country_tf.get())
            self.remove_trip_d.destroy()
        except Exception as e:
            ErrorWindow(Exception, e)

    def set_btn(self):
        if len(self.name_tf.get()) != 0 and len(self.country_tf.get()) != 0:
            self.add_d_btn.config(state=NORMAL)
        else:
            self.add_d_btn.config(state=DISABLED)


class ViewTrip:
    def __init__(self, ctrl):
        self.view_trip = Toplevel()
        self.vt_ctrl = ctrl
        self.view_trip.geometry("600x600")
        self.view_trip.title('View the Trip')

        frame1 = ttk.Frame(self.view_trip)
        frame1.pack()
        frame2 = ttk.Frame(self.view_trip)
        frame2.pack(side=TOP, fill=BOTH, expand=True)
        ttk.Label(frame2, text='Your Trip', foreground='blue', width=20, font=('Arial', 16, 'bold')).pack()
        frame3 = ttk.Frame(self.view_trip)
        frame3.pack(side=TOP, fill=BOTH, expand=True)
        self.treeview = ttk.Treeview(frame3)
        self.treeview.pack(fill=BOTH, expand=True)

        frame4 = ttk.Frame(self.view_trip)
        frame4.pack(side=BOTTOM, fill=X, expand=True)
        ttk.Button(frame4, text='Close', command=self.view_trip.destroy).pack(side=tk.RIGHT, fill=X, expand=True)
        self.view_ind_btn = ttk.Button(frame4, text='View Individual', command=self.view_individual)
        self.view_ind_btn.pack(side=tk.LEFT, fill=X, expand=True)
        self.view_ind_btn.config(state=DISABLED)

        self.set_treeview()
        self.treeview.bind("<<TreeviewSelect>>", lambda e: self.view_ind_btn.config(state=NORMAL))

    def set_treeview(self):
        lst = self.vt_ctrl.view_trip()
        if len(lst) == 0:
            self.treeview.heading("#0", text='Nothing yet')
        else:
            self.treeview['show'] = 'tree'
            for i in lst:
                x = self.vt_ctrl.desti_or_flight(i)
                if x is True:
                    self.treeview.insert('', 'end', text=i.name + ' in ' + i.country, values=i.__class__)
                else:
                    self.treeview.insert('', 'end', text=i.airline + ' ' + str(i.flight_no) +
                                 ' from ' + i.takeoff + ' to ' + i.landing + ' for ' + str(i.cost), values=i.__class__)

    def is_desti(self, selection):
        for item in selection:
            item_class = self.treeview.item(item, option='values')
            if item_class[1] != "'Destination.Destination'>":
                return False
        return True

    def is_flight(self, selection):
        for item in selection:
            item_class = self.treeview.item(item, option='values')
            if item_class[1] != "'Flight.Flight'>":
                return False
        return True

    def view_individual(self):
        if self.is_desti(self.treeview.selection()):
            ViewAllDestinations(self.vt_ctrl)
        elif self.is_flight(self.treeview.selection()):
            ViewAllFlights(self.vt_ctrl)
        else:
            ErrorWindow('ID 10 T Err: idiosyncratic Selection', 'View a Flight or Destination individually, not both')







