
import tkinter as tk
from tkinter import messagebox


# -------------------------------
# BASIC SETTINGS
# -------------------------------

BG = "#111111"
PANEL = "#202020"
CARD = "#292929"
WHITE = "#FFFFFF"
GREY = "#AAAAAA"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "bug2000"


# -------------------------------
# TEMPORARY INSTRUMENT DATA
# -------------------------------

instruments = [

    {
        "instrument": "Guitar",
        "type": "Acoustic",
        "model": "Yamaha F280",
        "brand": "Yamaha",
        "description": "Steel string acoustic guitar for beginners.",
        "price": 7500,
        "suitable_for": "Beginner"
    },

    {
        "instrument": "Guitar",
        "type": "Electric",
        "model": "Yamaha Pacifica",
        "brand": "Yamaha",
        "description": "Electric guitar suitable for learning and practice.",
        "price": 25000,
        "suitable_for": "Intermediate"
    },

    {
        "instrument": "Keyboard",
        "type": "Digital",
        "model": "Casio CT-S1",
        "brand": "Casio",
        "description": "Portable digital keyboard.",
        "price": 18000,
        "suitable_for": "Beginner"
    }

]


# -------------------------------
# MAIN WINDOW
# -------------------------------

root = tk.Tk()

root.title("BUG2000 - Music Instrument System")
root.geometry("1050x700")
root.minsize(850, 600)

root.configure(bg=BG)


# -------------------------------
# COMMON FUNCTIONS
# -------------------------------

def clear_content():

    for widget in content.winfo_children():
        widget.destroy()


def heading(parent, text, size=22):

    label = tk.Label(
        parent,
        text=text,
        font=("Arial", size, "bold"),
        bg=BG,
        fg=WHITE
    )

    label.pack(anchor="w", pady=10)


def make_button(parent, text, command):

    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BG,
        activebackground="#CCCCCC",
        relief="flat",
        padx=15,
        pady=8,
        cursor="hand2"
    )

    return button


def show_matches(matches, title):

    clear_content()

    heading(content, title)

    if len(matches) == 0:

        tk.Label(
            content,
            text="No matching instruments found.",
            bg=BG,
            fg=GREY,
            font=("Arial", 13)
        ).pack(anchor="w", pady=15)

        return

    for item in matches:

        card = tk.Frame(
            content,
            bg=CARD,
            padx=15,
            pady=12
        )

        card.pack(fill="x", pady=7)

        tk.Label(
            card,
            text=item["model"],
            bg=CARD,
            fg=WHITE,
            font=("Arial", 15, "bold")
        ).pack(anchor="w")

        tk.Label(
            card,
            text="Instrument: " + item["instrument"]
            + " | Type: " + item["type"],
            bg=CARD,
            fg=GREY,
            font=("Arial", 10)
        ).pack(anchor="w", pady=3)

        tk.Label(
            card,
            text="Brand: " + item["brand"]
            + " | Price: Rs. " + str(item["price"]),
            bg=CARD,
            fg=WHITE,
            font=("Arial", 11)
        ).pack(anchor="w", pady=3)

        tk.Label(
            card,
            text="Description: " + item["description"],
            bg=CARD,
            fg=GREY,
            font=("Arial", 10),
            wraplength=750,
            justify="left"
        ).pack(anchor="w", pady=3)

        tk.Label(
            card,
            text="Suitable for: " + item["suitable_for"],
            bg=CARD,
            fg=WHITE,
            font=("Arial", 10, "bold")
        ).pack(anchor="w")


# -------------------------------
# HOME SCREEN
# -------------------------------

def show_home():

    clear_content()

    heading(content, "Welcome to BUG2000", 28)

    tk.Label(
        content,
        text="Discover musical instruments that suit your needs.",
        bg=BG,
        fg=GREY,
        font=("Arial", 13)
    ).pack(anchor="w", pady=5)

    tk.Frame(content, bg=BG, height=30).pack()

    card = tk.Frame(
        content,
        bg=PANEL,
        padx=25,
        pady=25
    )

    card.pack(fill="x", pady=10)

    tk.Label(
        card,
        text="Find Your Instrument",
        bg=PANEL,
        fg=WHITE,
        font=("Arial", 20, "bold")
    ).pack(anchor="w")

    tk.Label(
        card,
        text="Enter your budget and requirements to find suitable models.",
        bg=PANEL,
        fg=GREY,
        font=("Arial", 11)
    ).pack(anchor="w", pady=10)

    make_button(
        card,
        "Explore Instruments",
        show_finder
    ).pack(anchor="w", pady=5)

    card2 = tk.Frame(
        content,
        bg=PANEL,
        padx=25,
        pady=25
    )

    card2.pack(fill="x", pady=10)

    tk.Label(
        card2,
        text="Instrument Catalogue",
        bg=PANEL,
        fg=WHITE,
        font=("Arial", 20, "bold")
    ).pack(anchor="w")

    tk.Label(
        card2,
        text="Explore the instruments available in BUG2000.",
        bg=PANEL,
        fg=GREY,
        font=("Arial", 11)
    ).pack(anchor="w", pady=10)

    make_button(
        card2,
        "View Dashboard",
        show_dashboard
    ).pack(anchor="w", pady=5)


# -------------------------------
# DASHBOARD
# -------------------------------

def show_dashboard():

    clear_content()

    heading(content, "Dashboard")

    total = len(instruments)

    instrument_types = []

    for item in instruments:

        if item["instrument"] not in instrument_types:
            instrument_types.append(item["instrument"])

    brands = []

    for item in instruments:

        if item["brand"] not in brands:
            brands.append(item["brand"])

    stats = [
        ("Total Models", total),
        ("Instrument Categories", len(instrument_types)),
        ("Available Brands", len(brands))
    ]

    for name, number in stats:

        card = tk.Frame(
            content,
            bg=CARD,
            padx=20,
            pady=20
        )

        card.pack(fill="x", pady=8)

        tk.Label(
            card,
            text=name,
            bg=CARD,
            fg=GREY,
            font=("Arial", 12)
        ).pack(anchor="w")

        tk.Label(
            card,
            text=str(number),
            bg=CARD,
            fg=WHITE,
            font=("Arial", 25, "bold")
        ).pack(anchor="w")

    heading(content, "Recently Available Instruments", 16)

    for item in instruments[:5]:

        tk.Label(
            content,
            text=item["instrument"] + " | "
            + item["type"] + " | "
            + item["model"],
            bg=BG,
            fg=WHITE,
            font=("Arial", 11)
        ).pack(anchor="w", pady=4)


# -------------------------------
# SEARCH BAR
# -------------------------------

def global_search():

    search = search_entry.get().strip().lower()

    if search == "":

        messagebox.showinfo(
            "Search",
            "Please enter something to search."
        )

        return

    matches = []

    for item in instruments:

        if (search in item["instrument"].lower()
            or search in item["type"].lower()
            or search in item["model"].lower()
            or search in item["brand"].lower()):

            matches.append(item)

    show_matches(matches, "Search Results")


# -------------------------------
# INSTRUMENT FINDER
# -------------------------------

def show_finder():

    clear_content()

    heading(content, "Instrument Finder")

    tk.Label(
        content,
        text="Enter your requirements below.",
        bg=BG,
        fg=GREY,
        font=("Arial", 11)
    ).pack(anchor="w")

    form = tk.Frame(
        content,
        bg=PANEL,
        padx=25,
        pady=20
    )

    form.pack(fill="x", pady=20)

    finder_fields = {}

    field_names = [
        "Instrument",
        "Type",
        "Maximum Budget",
        "Purpose"
    ]

    for i, name in enumerate(field_names):

        tk.Label(
            form,
            text=name,
            bg=PANEL,
            fg=WHITE,
            font=("Arial", 11)
        ).grid(
            row=i,
            column=0,
            sticky="w",
            padx=10,
            pady=10
        )

        entry = tk.Entry(
            form,
            font=("Arial", 11),
            width=35
        )

        entry.grid(
            row=i,
            column=1,
            padx=10,
            pady=10
        )

        finder_fields[name] = entry

    tk.Label(
        form,
        text="Example: Guitar, Acoustic, 15000, Beginner",
        bg=PANEL,
        fg=GREY,
        font=("Arial", 9)
    ).grid(
        row=4,
        column=1,
        sticky="w",
        padx=10
    )

    def find_instruments():

        instrument = finder_fields["Instrument"].get().strip().lower()

        instrument_type = finder_fields["Type"].get().strip().lower()

        budget = finder_fields["Maximum Budget"].get().strip()

        purpose = finder_fields["Purpose"].get().strip().lower()

        if instrument == "" or budget == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter instrument and maximum budget."
            )

            return

        try:

            budget = float(budget)

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid numerical budget."
            )

            return

        matches = []

        for item in instruments:

            if instrument not in item["instrument"].lower():
                continue

            if instrument_type != "" and instrument_type not in item["type"].lower():
                continue

            if item["price"] > budget:
                continue

            if purpose != "" and purpose not in item["suitable_for"].lower() and "all" not in item["suitable_for"].lower():
                continue

            matches.append(item)

        matches.sort(key=lambda x: x["price"])

        show_matches(
            matches,
            "Your Recommended Instruments"
        )

    make_button(
        form,
        "Find My Instrument",
        find_instruments
    ).grid(
        row=5,
        column=1,
        sticky="w",
        padx=10,
        pady=15
    )


# -------------------------------
# ADMIN LOGIN
# -------------------------------

def show_admin_login():

    clear_content()

    heading(content, "Administrator Login")

    login_frame = tk.Frame(
        content,
        bg=PANEL,
        padx=30,
        pady=30
    )

    login_frame.pack(pady=30)

    tk.Label(
        login_frame,
        text="Username",
        bg=PANEL,
        fg=WHITE
    ).grid(row=0, column=0, padx=10, pady=10)

    username_entry = tk.Entry(
        login_frame,
        font=("Arial", 11)
    )

    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(
        login_frame,
        text="Password",
        bg=PANEL,
        fg=WHITE
    ).grid(row=1, column=0, padx=10, pady=10)

    password_entry = tk.Entry(
        login_frame,
        show="*",
        font=("Arial", 11)
    )

    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def check_login():

        username = username_entry.get()

        password = password_entry.get()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            messagebox.showinfo(
                "Login",
                "Welcome Administrator!"
            )

            show_admin()

        else:

            messagebox.showerror(
                "Login Failed",
                "Incorrect username or password."
            )

    make_button(
        login_frame,
        "Login",
        check_login
    ).grid(
        row=2,
        column=1,
        pady=15
    )


# -------------------------------
# ADMIN PANEL
# -------------------------------

admin_listbox = None
admin_fields = {}
description_box = None
selected_index = None


def show_admin():

    global admin_listbox
    global admin_fields
    global description_box
    global selected_index

    selected_index = None

    clear_content()

    heading(content, "Admin Dashboard")

    main_frame = tk.Frame(
        content,
        bg=BG
    )

    main_frame.pack(fill="both", expand=True)

    # LEFT SIDE: INSTRUMENT LIST

    left = tk.Frame(
        main_frame,
        bg=PANEL,
        padx=10,
        pady=10
    )

    left.pack(
        side="left",
        fill="both",
        expand=True,
        padx=5
    )

    tk.Label(
        left,
        text="Available Instruments",
        bg=PANEL,
        fg=WHITE,
        font=("Arial", 13, "bold")
    ).pack(anchor="w", pady=10)

    admin_listbox = tk.Listbox(
        left,
        bg=CARD,
        fg=WHITE,
        font=("Arial", 10),
        selectbackground="#666666",
        width=48,
        height=20
    )

    admin_listbox.pack(fill="both", expand=True)

    admin_listbox.bind(
        "<<ListboxSelect>>",
        select_instrument
    )

    # RIGHT SIDE: INPUT FORM

    right = tk.Frame(
        main_frame,
        bg=PANEL,
        padx=15,
        pady=10
    )

    right.pack(
        side="right",
        fill="both",
        expand=True,
        padx=5
    )

    tk.Label(
        right,
        text="Instrument Details",
        bg=PANEL,
        fg=WHITE,
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="w",
        pady=10
    )

    admin_fields = {}

    field_names = [
        "Instrument",
        "Type",
        "Model",
        "Brand",
        "Price",
        "Suitable For"
    ]

    for i, name in enumerate(field_names):

        tk.Label(
            right,
            text=name,
            bg=PANEL,
            fg=WHITE,
            font=("Arial", 10)
        ).grid(
            row=i+1,
            column=0,
            sticky="w",
            padx=5,
            pady=7
        )

        entry = tk.Entry(
            right,
            font=("Arial", 10),
            width=25
        )

        entry.grid(
            row=i+1,
            column=1,
            padx=5,
            pady=7
        )

        admin_fields[name] = entry

    tk.Label(
        right,
        text="Description",
        bg=PANEL,
        fg=WHITE
    ).grid(
        row=7,
        column=0,
        sticky="w",
        padx=5,
        pady=7
    )

    description_box = tk.Text(
        right,
        width=25,
        height=4,
        font=("Arial", 10)
    )

    description_box.grid(
        row=7,
        column=1,
        padx=5,
        pady=7
    )

    # ADMIN BUTTONS

    make_button(
        right,
        "Add Instrument",
        add_instrument
    ).grid(
        row=8,
        column=0,
        padx=5,
        pady=10
    )

    make_button(
        right,
        "Update",
        update_instrument
    ).grid(
        row=8,
        column=1,
        padx=5,
        pady=10
    )

    make_button(
        right,
        "Delete",
        delete_instrument
    ).grid(
        row=9,
        column=0,
        padx=5,
        pady=5
    )

    make_button(
        right,
        "Clear Form",
        clear_admin_form
    ).grid(
        row=9,
        column=1,
        padx=5,
        pady=5
    )

    make_button(
        right,
        "Logout",
        show_home
    ).grid(
        row=10,
        column=0,
        columnspan=2,
        pady=15
    )

    refresh_admin_list()


# -------------------------------
# REFRESH ADMIN LIST
# -------------------------------

def refresh_admin_list():

    admin_listbox.delete(0, tk.END)

    for item in instruments:

        text = (
            item["instrument"] + " | "
            + item["type"] + " | "
            + item["model"]
        )

        admin_listbox.insert(tk.END, text)


# -------------------------------
# SELECT INSTRUMENT
# -------------------------------

def select_instrument(event):

    global selected_index

    selection = admin_listbox.curselection()

    if len(selection) == 0:
        return

    selected_index = selection[0]

    item = instruments[selected_index]

    admin_fields["Instrument"].delete(0, tk.END)
    admin_fields["Instrument"].insert(0, item["instrument"])

    admin_fields["Type"].delete(0, tk.END)
    admin_fields["Type"].insert(0, item["type"])

    admin_fields["Model"].delete(0, tk.END)
    admin_fields["Model"].insert(0, item["model"])

    admin_fields["Brand"].delete(0, tk.END)
    admin_fields["Brand"].insert(0, item["brand"])

    admin_fields["Price"].delete(0, tk.END)
    admin_fields["Price"].insert(0, str(item["price"]))

    admin_fields["Suitable For"].delete(0, tk.END)
    admin_fields["Suitable For"].insert(0, item["suitable_for"])

    description_box.delete("1.0", tk.END)
    description_box.insert("1.0", item["description"])


# -------------------------------
# GET ADMIN INPUT
# -------------------------------

def get_admin_data():

    data = {}

    for name, entry in admin_fields.items():

        data[name] = entry.get().strip()

    data["description"] = description_box.get(
        "1.0",
        tk.END
    ).strip()

    if (
        data["Instrument"] == ""
        or data["Type"] == ""
        or data["Model"] == ""
        or data["Brand"] == ""
        or data["Price"] == ""
    ):

        messagebox.showwarning(
            "Missing Information",
            "Please fill all required fields."
        )

        return None

    try:

        data["Price"] = float(data["Price"])

        if data["Price"] < 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Invalid Price",
            "Please enter a valid non-negative price."
        )

        return None

    return {
        "instrument": data["Instrument"],
        "type": data["Type"],
        "model": data["Model"],
        "brand": data["Brand"],
        "description": data["description"],
        "price": data["Price"],
        "suitable_for": data["Suitable For"]
    }


# -------------------------------
# ADD INSTRUMENT
# -------------------------------

def add_instrument():

    data = get_admin_data()

    if data is None:
        return

    for item in instruments:

        if (
            item["instrument"].lower() == data["instrument"].lower()
            and item["type"].lower() == data["type"].lower()
            and item["model"].lower() == data["model"].lower()
        ):

            messagebox.showerror(
                "Duplicate",
                "This instrument type and model already exists."
            )

            return

    instruments.append(data)

    refresh_admin_list()

    clear_admin_form()

    messagebox.showinfo(
        "Success",
        "Instrument added successfully."
    )


# -------------------------------
# UPDATE INSTRUMENT
# -------------------------------

def update_instrument():

    global selected_index

    if selected_index is None:

        messagebox.showwarning(
            "Selection",
            "Please select an instrument to update."
        )

        return

    data = get_admin_data()

    if data is None:
        return

    for i, item in enumerate(instruments):

        if i != selected_index:

            if (
                item["instrument"].lower() == data["instrument"].lower()
                and item["type"].lower() == data["type"].lower()
                and item["model"].lower() == data["model"].lower()
            ):

                messagebox.showerror(
                    "Duplicate",
                    "Another instrument with this type and model exists."
                )

                return

    instruments[selected_index] = data

    refresh_admin_list()

    admin_listbox.selection_set(selected_index)

    messagebox.showinfo(
        "Success",
        "Instrument updated successfully."
    )


# -------------------------------
# DELETE INSTRUMENT
# -------------------------------

def delete_instrument():

    global selected_index

    if selected_index is None:

        messagebox.showwarning(
            "Selection",
            "Please select an instrument to delete."
        )

        return

    answer = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this instrument?"
    )

    if answer:

        instruments.pop(selected_index)

        selected_index = None

        refresh_admin_list()

        clear_admin_form()

        messagebox.showinfo(
            "Deleted",
            "Instrument deleted successfully."
        )


# -------------------------------
# CLEAR ADMIN FORM
# -------------------------------

def clear_admin_form():

    global selected_index

    selected_index = None

    for entry in admin_fields.values():

        entry.delete(0, tk.END)

    description_box.delete("1.0", tk.END)

    admin_listbox.selection_clear(0, tk.END)


# -------------------------------
# TOP HEADER
# -------------------------------

header = tk.Frame(
    root,
    bg=BG,
    padx=20,
    pady=15
)

header.pack(fill="x")

tk.Label(
    header,
    text="BUG2000.",
    bg=BG,
    fg=WHITE,
    font=("Arial", 22, "bold")
).pack(side="left", padx=10)

search_entry = tk.Entry(
    header,
    font=("Arial", 11),
    width=30
)

search_entry.pack(
    side="right",
    padx=5,
    ipady=5
)

make_button(
    header,
    "Search",
    global_search
).pack(side="right", padx=5)


# -------------------------------
# NAVIGATION BAR
# -------------------------------

navigation = tk.Frame(
    root,
    bg=PANEL,
    padx=10,
    pady=10
)

navigation.pack(fill="x")

make_button(
    navigation,
    "Home",
    show_home
).pack(side="left", padx=5)

make_button(
    navigation,
    "Dashboard",
    show_dashboard
).pack(side="left", padx=5)

make_button(
    navigation,
    "Instrument Finder",
    show_finder
).pack(side="left", padx=5)

make_button(
    navigation,
    "Admin",
    show_admin_login
).pack(side="right", padx=5)


# -------------------------------
# MAIN CONTENT AREA
# -------------------------------

content = tk.Frame(
    root,
    bg=BG,
    padx=30,
    pady=20
)

content.pack(
    fill="both",
    expand=True
)


# -------------------------------
# START APPLICATION
# -------------------------------

show_home()

root.mainloop()
