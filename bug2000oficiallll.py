import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os

BG = "#111111"
PANEL = "#202020"
CARD = "#292929"
WHITE = "#FFFFFF"
GREY = "#AAAAAA"

admin_u = "admin"
admin_p = "bug2000"

inst = []
pics = []

root = tk.Tk()
root.title("BUG2000 - Music Instrument System")
root.geometry("1050x700")
root.minsize(850, 600)
root.configure(bg=BG)

ic_search = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-26 at 10.25.04 AM.jpeg").resize((20, 20)))
ic_home = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-26 at 10.25.03 AM.jpeg").resize((20, 20)))
ic_dash = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-26 at 10.25.03 AM (1).jpeg").resize((20, 20)))
ic_finder = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-26 at 10.25.03 AM.jpeg").resize((20, 20)))
ic_admin = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-25 at 9.14.10 PM.jpeg").resize((20, 20)))
ic_login = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-26 at 10.25.02 AM.jpeg").resize((20, 20)))
ic_browse = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-26 at 10.25.02 AM.jpeg").resize((20, 20)))
ic_add = ImageTk.PhotoImage(Image.open(r"C:\Users\amen0\Downloads\WhatsApp Image 2026-11-25 at 9.14.11 PM.jpeg").resize((20, 20)))

def clr_cntnt():
    for w in content.winfo_children():
        w.destroy()
    pics.clear()


def show_matches(matches, title):
    clr_cntnt()
    tk.Label(content, text=title, font=("Arial", 22, "bold"), bg=BG, fg=WHITE).pack(anchor="w", pady=10)

    if len(matches) == 0:
        tk.Label(content, text="No matching instruments found.", bg=BG, fg=GREY, font=("Arial", 13)).pack(anchor="w", pady=15)
        return

    for item in matches:
        card = tk.Frame(content, bg=CARD, padx=15, pady=12)
        card.pack(fill="x", pady=7)

        left_box = tk.Frame(card, bg=CARD)
        left_box.pack(side="left", fill="both", expand=True)

        tk.Label(left_box, text=item["model"], bg=CARD, fg=WHITE, font=("Arial", 15, "bold")).pack(anchor="w")
        tk.Label(left_box, text="Instrument: " + item["instrument"] + " | Type: " + item["type"], bg=CARD, fg=GREY, font=("Arial", 10)).pack(anchor="w", pady=3)
        tk.Label(left_box, text="Brand: " + item["brand"] + " | Price: Rs. " + str(item["price"]), bg=CARD, fg=WHITE, font=("Arial", 11)).pack(anchor="w", pady=3)
        tk.Label(left_box, text="Description: " + item["description"], bg=CARD, fg=GREY, font=("Arial", 10), wraplength=600, justify="left").pack(anchor="w", pady=3)
        tk.Label(left_box, text="Suitable for: " + item["suitable_for"], bg=CARD, fg=WHITE, font=("Arial", 10, "bold")).pack(anchor="w")

        if item["img"] != "" and os.path.exists(item["img"]):
            p = tk.PhotoImage(file=item["img"])
            if p.width() > 140 or p.height() > 140:
                p = p.subsample(max(1, p.width() // 120), max(1, p.height() // 120))
            pics.append(p)
            tk.Label(card, image=p, bg=CARD).pack(side="right", padx=10)


def show_home():
    clr_cntnt()
    tk.Label(content, text="Welcome to BUG2000", font=("Arial", 28, "bold"), bg=BG, fg=WHITE).pack(anchor="w", pady=10)
    tk.Label(content, text="Discover musical instruments that suit your needs.", bg=BG, fg=GREY, font=("Arial", 13)).pack(anchor="w", pady=5)
    tk.Frame(content, bg=BG, height=30).pack()

    card = tk.Frame(content, bg=PANEL, padx=25, pady=25)
    card.pack(fill="x", pady=10)
    tk.Label(card, text="Find Your Instrument", bg=PANEL, fg=WHITE, font=("Arial", 20, "bold")).pack(anchor="w")
    tk.Label(card, text="Enter your budget and requirements to find suitable models.", bg=PANEL, fg=GREY, font=("Arial", 11)).pack(anchor="w", pady=10)
    tk.Button(card, text=" Explore Instruments", image=ic_finder, compound="left", command=show_finder, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").pack(anchor="w", pady=5)

    card2 = tk.Frame(content, bg=PANEL, padx=25, pady=25)
    card2.pack(fill="x", pady=10)
    tk.Label(card2, text="Instrument Catalogue", bg=PANEL, fg=WHITE, font=("Arial", 20, "bold")).pack(anchor="w")
    tk.Label(card2, text="Explore the instruments available in BUG2000.", bg=PANEL, fg=GREY, font=("Arial", 11)).pack(anchor="w", pady=10)
    tk.Button(card2, text=" View Dashboard", image=ic_dash, compound="left", command=show_dashboard, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").pack(anchor="w", pady=5)


def show_dashboard():
    clr_cntnt()
    tk.Label(content, text="Dashboard", font=("Arial", 22, "bold"), bg=BG, fg=WHITE).pack(anchor="w", pady=10)

    total = len(inst)
    types_list = []
    brands_list = []

    for item in inst:
        if item["instrument"] not in types_list:
            types_list.append(item["instrument"])
        if item["brand"] not in brands_list:
            brands_list.append(item["brand"])

    c1 = tk.Frame(content, bg=CARD, padx=20, pady=20)
    c1.pack(fill="x", pady=8)
    tk.Label(c1, text="Total Models", bg=CARD, fg=GREY, font=("Arial", 12)).pack(anchor="w")
    tk.Label(c1, text=str(total), bg=CARD, fg=WHITE, font=("Arial", 25, "bold")).pack(anchor="w")

    c2 = tk.Frame(content, bg=CARD, padx=20, pady=20)
    c2.pack(fill="x", pady=8)
    tk.Label(c2, text="Instrument Categories", bg=CARD, fg=GREY, font=("Arial", 12)).pack(anchor="w")
    tk.Label(c2, text=str(len(types_list)), bg=CARD, fg=WHITE, font=("Arial", 25, "bold")).pack(anchor="w")

    c3 = tk.Frame(content, bg=CARD, padx=20, pady=20)
    c3.pack(fill="x", pady=8)
    tk.Label(c3, text="Available Brands", bg=CARD, fg=GREY, font=("Arial", 12)).pack(anchor="w")
    tk.Label(c3, text=str(len(brands_list)), bg=CARD, fg=WHITE, font=("Arial", 25, "bold")).pack(anchor="w")

    tk.Label(content, text="Recently Available Instruments", font=("Arial", 16, "bold"), bg=BG, fg=WHITE).pack(anchor="w", pady=10)

    for item in inst[:5]:
        tk.Label(content, text=item["instrument"] + " | " + item["type"] + " | " + item["model"], bg=BG, fg=WHITE, font=("Arial", 11)).pack(anchor="w", pady=4)


def global_search():
    s = search_entry.get().strip().lower()
    if s == "":
        messagebox.showinfo("Search", "Please enter something to search.")
        return

    matches = []
    for item in inst:
        if s in item["instrument"].lower() or s in item["type"].lower() or s in item["model"].lower() or s in item["brand"].lower():
            matches.append(item)

    show_matches(matches, "Search Results")


def show_finder():
    clr_cntnt()
    tk.Label(content, text="Instrument Finder", font=("Arial", 22, "bold"), bg=BG, fg=WHITE).pack(anchor="w", pady=10)
    tk.Label(content, text="Enter your requirements below.", bg=BG, fg=GREY, font=("Arial", 11)).pack(anchor="w")

    form = tk.Frame(content, bg=PANEL, padx=25, pady=20)
    form.pack(fill="x", pady=20)

    tk.Label(form, text="Instrument", bg=PANEL, fg=WHITE, font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
    e1 = tk.Entry(form, font=("Arial", 11), width=35)
    e1.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(form, text="Type", bg=PANEL, fg=WHITE, font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
    e2 = tk.Entry(form, font=("Arial", 11), width=35)
    e2.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(form, text="Maximum Budget", bg=PANEL, fg=WHITE, font=("Arial", 11)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
    e3 = tk.Entry(form, font=("Arial", 11), width=35)
    e3.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(form, text="Purpose", bg=PANEL, fg=WHITE, font=("Arial", 11)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    e4 = tk.Entry(form, font=("Arial", 11), width=35)
    e4.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(form, text="Example: Guitar, Acoustic, 15000, Beginner", bg=PANEL, fg=GREY, font=("Arial", 9)).grid(row=4, column=1, sticky="w", padx=10)

    def find_instruments():
        i_val = e1.get().strip().lower()
        t_val = e2.get().strip().lower()
        b_val = e3.get().strip()
        p_val = e4.get().strip().lower()

        if i_val == "" or b_val == "":
            messagebox.showwarning("Missing Information", "Please enter instrument and maximum budget.")
            return

        if not b_val.replace(".", "", 1).isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid numerical budget.")
            return
        b_num = float(b_val)

        matches = []
        for item in inst:
            if i_val not in item["instrument"].lower():
                continue
            if t_val != "" and t_val not in item["type"].lower():
                continue
            if item["price"] > b_num:
                continue
            if p_val != "" and p_val not in item["suitable_for"].lower() and "all" not in item["suitable_for"].lower():
                continue
            matches.append(item)

        for x in range(len(matches)):
            for y in range(len(matches) - 1):
                if matches[y]["price"] > matches[y + 1]["price"]:
                    matches[y], matches[y + 1] = matches[y + 1], matches[y]

        show_matches(matches, "Your Recommended Instruments")

    tk.Button(form, text=" Find My Instrument", image=ic_finder, compound="left", command=find_instruments, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").grid(row=5, column=1, sticky="w", padx=10, pady=15)


def show_admin_login():
    clr_cntnt()
    tk.Label(content, text="Administrator Login", font=("Arial", 22, "bold"), bg=BG, fg=WHITE).pack(anchor="w", pady=10)

    login_frame = tk.Frame(content, bg=PANEL, padx=30, pady=30)
    login_frame.pack(pady=30)

    tk.Label(login_frame, text="Username", bg=PANEL, fg=WHITE).grid(row=0, column=0, padx=10, pady=10)
    u_box = tk.Entry(login_frame, font=("Arial", 11))
    u_box.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_frame, text="Password", bg=PANEL, fg=WHITE).grid(row=1, column=0, padx=10, pady=10)
    p_box = tk.Entry(login_frame, show="*", font=("Arial", 11))
    p_box.grid(row=1, column=1, padx=10, pady=10)

    def check_login():
        if u_box.get() == admin_u and p_box.get() == admin_p:
            messagebox.showinfo("Login", "Welcome Administrator!")
            show_admin()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    tk.Button(login_frame, text=" Login", image=ic_login, compound="left", command=check_login, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").grid(row=2, column=1, pady=15)


admin_listbox = None
a_inst = a_type = a_model = a_brand = a_price = a_suit = a_img = None
description_box = None
sel_idx = None


def pick_img():
    path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.gif *.pgm *.ppm"), ("All files", "*.*")])
    if path != "":
        a_img.delete(0, tk.END)
        a_img.insert(0, path)


def show_admin():
    global admin_listbox, a_inst, a_type, a_model, a_brand, a_price, a_suit, a_img, description_box, sel_idx

    sel_idx = None
    clr_cntnt()
    tk.Label(content, text="Admin Dashboard", font=("Arial", 22, "bold"), bg=BG, fg=WHITE).pack(anchor="w", pady=10)

    main_frame = tk.Frame(content, bg=BG)
    main_frame.pack(fill="both", expand=True)

    left = tk.Frame(main_frame, bg=PANEL, padx=10, pady=10)
    left.pack(side="left", fill="both", expand=True, padx=5)
    tk.Label(left, text="Available Instruments", bg=PANEL, fg=WHITE, font=("Arial", 13, "bold")).pack(anchor="w", pady=10)

    admin_listbox = tk.Listbox(left, bg=CARD, fg=WHITE, font=("Arial", 10), selectbackground="#666666", width=45, height=20)
    admin_listbox.pack(fill="both", expand=True)
    admin_listbox.bind("<<ListboxSelect>>", select_instrument)

    right = tk.Frame(main_frame, bg=PANEL, padx=15, pady=10)
    right.pack(side="right", fill="both", expand=True, padx=5)
    tk.Label(right, text="Instrument Details", bg=PANEL, fg=WHITE, font=("Arial", 13, "bold")).grid(row=0, column=0, columnspan=3, sticky="w", pady=8)

    tk.Label(right, text="Instrument", bg=PANEL, fg=WHITE, font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    a_inst = tk.Entry(right, font=("Arial", 10), width=25)
    a_inst.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)

    tk.Label(right, text="Type", bg=PANEL, fg=WHITE, font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
    a_type = tk.Entry(right, font=("Arial", 10), width=25)
    a_type.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)

    tk.Label(right, text="Model", bg=PANEL, fg=WHITE, font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
    a_model = tk.Entry(right, font=("Arial", 10), width=25)
    a_model.grid(row=3, column=1, columnspan=2, sticky="w", padx=5, pady=5)

    tk.Label(right, text="Brand", bg=PANEL, fg=WHITE, font=("Arial", 10)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
    a_brand = tk.Entry(right, font=("Arial", 10), width=25)
    a_brand.grid(row=4, column=1, columnspan=2, sticky="w", padx=5, pady=5)

    tk.Label(right, text="Price", bg=PANEL, fg=WHITE, font=("Arial", 10)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
    a_price = tk.Entry(right, font=("Arial", 10), width=25)
    a_price.grid(row=5, column=1, columnspan=2, sticky="w", padx=5, pady=5)

    tk.Label(right, text="Suitable For", bg=PANEL, fg=WHITE, font=("Arial", 10)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
    a_suit = tk.Entry(right, font=("Arial", 10), width=25)
    a_suit.grid(row=6, column=1, columnspan=2, sticky="w", padx=5, pady=5)

    tk.Label(right, text="Image", bg=PANEL, fg=WHITE, font=("Arial", 10)).grid(row=7, column=0, sticky="w", padx=5, pady=5)
    a_img = tk.Entry(right, font=("Arial", 10), width=17)
    a_img.grid(row=7, column=1, sticky="w", padx=5, pady=5)
    tk.Button(right, text=" Browse", image=ic_browse, compound="left", command=pick_img, font=("Arial", 9, "bold"), bg=WHITE, fg=BG, relief="flat", padx=8, pady=2, cursor="hand2").grid(row=7, column=2, sticky="w", padx=2, pady=5)

    tk.Label(right, text="Description", bg=PANEL, fg=WHITE).grid(row=8, column=0, sticky="w", padx=5, pady=5)
    description_box = tk.Text(right, width=25, height=3, font=("Arial", 10))
    description_box.grid(row=8, column=1, columnspan=2, sticky="w", padx=5, pady=5)

    tk.Button(right, text=" Add Instrument", image=ic_add, compound="left", command=add_instrument, font=("Arial", 10, "bold"), bg=WHITE, fg=BG, relief="flat", padx=12, pady=6, cursor="hand2").grid(row=9, column=0, padx=5, pady=8)
    tk.Button(right, text="Update", command=update_instrument, font=("Arial", 10, "bold"), bg=WHITE, fg=BG, relief="flat", padx=12, pady=6, cursor="hand2").grid(row=9, column=1, padx=5, pady=8)
    tk.Button(right, text="Delete", command=delete_instrument, font=("Arial", 10, "bold"), bg=WHITE, fg=BG, relief="flat", padx=12, pady=6, cursor="hand2").grid(row=10, column=0, padx=5, pady=4)
    tk.Button(right, text="Clear Form", command=clear_admin_form, font=("Arial", 10, "bold"), bg=WHITE, fg=BG, relief="flat", padx=12, pady=6, cursor="hand2").grid(row=10, column=1, padx=5, pady=4)
    tk.Button(right, text="Logout", command=show_home, font=("Arial", 10, "bold"), bg=WHITE, fg=BG, relief="flat", padx=12, pady=6, cursor="hand2").grid(row=11, column=0, columnspan=2, pady=10)

    refresh_admin_list()


def refresh_admin_list():
    admin_listbox.delete(0, tk.END)
    for item in inst:
        admin_listbox.insert(tk.END, item["instrument"] + " | " + item["type"] + " | " + item["model"])


def select_instrument(event):
    global sel_idx
    selection = admin_listbox.curselection()
    if len(selection) == 0:
        return

    sel_idx = selection[0]
    item = inst[sel_idx]

    a_inst.delete(0, tk.END); a_inst.insert(0, item["instrument"])
    a_type.delete(0, tk.END); a_type.insert(0, item["type"])
    a_model.delete(0, tk.END); a_model.insert(0, item["model"])
    a_brand.delete(0, tk.END); a_brand.insert(0, item["brand"])
    a_price.delete(0, tk.END); a_price.insert(0, str(item["price"]))
    a_suit.delete(0, tk.END); a_suit.insert(0, item["suitable_for"])
    a_img.delete(0, tk.END); a_img.insert(0, item["img"])

    description_box.delete("1.0", tk.END)
    description_box.insert("1.0", item["description"])


def get_admin_data():
    v1 = a_inst.get().strip()
    v2 = a_type.get().strip()
    v3 = a_model.get().strip()
    v4 = a_brand.get().strip()
    v5 = a_price.get().strip()
    v6 = a_suit.get().strip()
    v7 = a_img.get().strip()
    desc = description_box.get("1.0", tk.END).strip()

    if v1 == "" or v2 == "" or v3 == "" or v4 == "" or v5 == "":
        messagebox.showwarning("Missing Information", "Please fill all required fields.")
        return None

    if not v5.replace(".", "", 1).isdigit():
        messagebox.showerror("Invalid Price", "Please enter a valid non-negative price.")
        return None

    return {
        "instrument": v1,
        "type": v2,
        "model": v3,
        "brand": v4,
        "description": desc,
        "price": float(v5),
        "suitable_for": v6,
        "img": v7
    }


def add_instrument():
    data = get_admin_data()
    if data is None:
        return

    for item in inst:
        if item["instrument"].lower() == data["instrument"].lower() and item["type"].lower() == data["type"].lower() and item["model"].lower() == data["model"].lower():
            messagebox.showerror("Duplicate", "This instrument type and model already exists.")
            return

    inst.append(data)
    refresh_admin_list()
    clear_admin_form()
    messagebox.showinfo("Success", "Instrument added successfully.")


def update_instrument():
    global sel_idx
    if sel_idx is None:
        messagebox.showwarning("Selection", "Please select an instrument to update.")
        return

    data = get_admin_data()
    if data is None:
        return

    for i in range(len(inst)):
        if i != sel_idx:
            if inst[i]["instrument"].lower() == data["instrument"].lower() and inst[i]["type"].lower() == data["type"].lower() and inst[i]["model"].lower() == data["model"].lower():
                messagebox.showerror("Duplicate", "Another instrument with this type and model exists.")
                return

    inst[sel_idx] = data
    refresh_admin_list()
    admin_listbox.selection_set(sel_idx)
    messagebox.showinfo("Success", "Instrument updated successfully.")


def delete_instrument():
    global sel_idx
    if sel_idx is None:
        messagebox.showwarning("Selection", "Please select an instrument to delete.")
        return

    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this instrument?"):
        inst.pop(sel_idx)
        sel_idx = None
        refresh_admin_list()
        clear_admin_form()
        messagebox.showinfo("Deleted", "Instrument deleted successfully.")


def clear_admin_form():
    global sel_idx
    sel_idx = None
    a_inst.delete(0, tk.END)
    a_type.delete(0, tk.END)
    a_model.delete(0, tk.END)
    a_brand.delete(0, tk.END)
    a_price.delete(0, tk.END)
    a_suit.delete(0, tk.END)
    a_img.delete(0, tk.END)
    description_box.delete("1.0", tk.END)
    admin_listbox.selection_clear(0, tk.END)


header = tk.Frame(root, bg=BG, padx=20, pady=15)
header.pack(fill="x")
tk.Label(header, text="BUG2000.", bg=BG, fg=WHITE, font=("Arial", 22, "bold")).pack(side="left", padx=10)

search_entry = tk.Entry(header, font=("Arial", 11), width=30)
search_entry.pack(side="right", padx=5, ipady=5)
tk.Button(header, text=" Search", image=ic_search, compound="left", command=global_search, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").pack(side="right", padx=5)

navigation = tk.Frame(root, bg=PANEL, padx=10, pady=10)
navigation.pack(fill="x")
tk.Button(navigation, text=" Home", image=ic_home, compound="left", command=show_home, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").pack(side="left", padx=5)
tk.Button(navigation, text=" Dashboard", image=ic_dash, compound="left", command=show_dashboard, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").pack(side="left", padx=5)
tk.Button(navigation, text=" Instrument Finder", image=ic_finder, compound="left", command=show_finder, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").pack(side="left", padx=5)
tk.Button(navigation, text=" Admin", image=ic_admin, compound="left", command=show_admin_login, font=("Arial", 11, "bold"), bg=WHITE, fg=BG, activebackground="#CCCCCC", relief="flat", padx=15, pady=8, cursor="hand2").pack(side="right", padx=5)

content = tk.Frame(root, bg=BG, padx=30, pady=20)
content.pack(fill="both", expand=True)

show_home()
root.mainloop()