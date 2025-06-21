import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window - Day 1")
        # Set window size to match screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.attributes('-fullscreen', True)

        # Initialize appearance mode
        self.current_theme = "dark"
        ctk.set_appearance_mode(self.current_theme)
        ctk.set_default_color_theme("blue")

        # Main container
        self.main_frame = ctk.CTkFrame(self.root, fg_color=("#2B2D42", "#EDF2F4"))
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Top frame for heading and toggle button
        self.top_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.top_frame.pack(fill="x")

        # Heading
        self.heading_label = ctk.CTkLabel(
            self.top_frame,
            text="   Registration Window - Day 1",
            font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"),
            text_color=("#EDF2F4", "#2B2D42")
        )
        self.heading_label.pack(side="left", pady=(20, 30))

        # Theme toggle button
        self.toggle_button = ctk.CTkButton(
            self.top_frame,
            text="Light",
            width=150,
            corner_radius=10,
            fg_color=("#4A4B6B", "#3A3B5B"),
            hover_color=("#EF233C", "#D90429"),
            command=self.toggle_theme
        )
        self.toggle_button.pack(side="right", padx=20)

        # Input Frame
        self.input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.input_frame.pack(fill="x", padx=20, pady=10)

        # First Row: Reg No, First Name, Last Name, Class
        self.first_row_frame = ctk.CTkFrame(self.input_frame, fg_color="transparent")
        self.first_row_frame.pack(fill="x", pady=10, anchor="w")

        # Registration Number
        self.reg_entry = ctk.CTkEntry(
            self.first_row_frame,
            width=100,
            corner_radius=10,
            border_width=1,
            fg_color=("#3A3B5B", "#FFFFFF"),
            text_color=("#EDF2F4", "#2B2D42"),
            border_color=("#4A4B6B", "#D3D3D3")
        )
        self.reg_entry.grid(row=0, column=0, padx=20, pady=(0, 5), sticky="w")
        self.reg_label = ctk.CTkLabel(
            self.first_row_frame,
            text="Registration Number",
            font=ctk.CTkFont(size=15),
            text_color=("#D3D3D3", "#4A4B6B"),
            anchor="w"
        )
        self.reg_label.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="w")

        # First Name
        self.fname_entry = ctk.CTkEntry(
            self.first_row_frame,
            width=250,
            placeholder_text="Enter First Name",
            corner_radius=10,
            border_width=1,
            fg_color=("#3A3B5B", "#FFFFFF"),
            text_color=("#EDF2F4", "#2B2D42"),
            border_color=("#4A4B6B", "#D3D3D3")
        )
        self.fname_entry.grid(row=0, column=1, padx=20, pady=(0, 5), sticky="w")
        self.fname_label = ctk.CTkLabel(
            self.first_row_frame,
            text="First Name",
            font=ctk.CTkFont(size=15),
            text_color=("#D3D3D3", "#4A4B6B"),
            anchor="w"
        )
        self.fname_label.grid(row=1, column=1, padx=20, pady=(0, 10), sticky="w")

        # Last Name
        self.lname_entry = ctk.CTkEntry(
            self.first_row_frame,
            width=250,
            corner_radius=10,
            placeholder_text="Enter Last Name",
            border_width=1,
            fg_color=("#3A3B5B", "#FFFFFF"),
            text_color=("#EDF2F4", "#2B2D42"),
            border_color=("#4A4B6B", "#D3D3D3")
        )
        self.lname_entry.grid(row=0, column=2, padx=20, pady=(0, 5), sticky="w")
        self.lname_label = ctk.CTkLabel(
            self.first_row_frame,
            text="Last Name",
            font=ctk.CTkFont(size=15),
            text_color=("#D3D3D3", "#4A4B6B"),
            anchor="w"
        )
        self.lname_label.grid(row=1, column=2, padx=20, pady=(0, 10), sticky="w")

        # Class Dropdown
        self.class_var = tk.StringVar()
        self.class_dropdown = ctk.CTkComboBox(
            self.first_row_frame,
            values=[str(i) for i in range(1, 13)],
            variable=self.class_var,
            width=150,
            state="readonly",
            corner_radius=10,
            fg_color=("#3A3B5B", "#FFFFFF"),
            text_color=("#EDF2F4", "#2B2D42"),
            dropdown_fg_color=("#3A3B5B", "#FFFFFF"),
            dropdown_text_color=("#FFFFFF", "#000000"),  # White in dark, black in light
            button_color=("#4A4B6B", "#D3D3D3"),
            button_hover_color="#ADD8E6",
            dropdown_hover_color=("#000000","#ffee05")
        )
        self.class_dropdown.grid(row=0, column=3, padx=20, pady=(0, 5), sticky="w")
        self.class_var.set("Select Class")
        self.class_label = ctk.CTkLabel(
            self.first_row_frame,
            text="Class",
            font=ctk.CTkFont(size=15),
            text_color=("#D3D3D3", "#4A4B6B"),
            anchor="w"
        )
        self.class_label.grid(row=1, column=3, padx=20, pady=(0, 10), sticky="w")

        # School Dropdown
        self.school_var = tk.StringVar()
        self.school_dropdown = ctk.CTkComboBox(
            self.input_frame,
            values=["School A", "School B", "School C"],
            variable=self.school_var,
            width=915,
            corner_radius=10,
            state="readonly",
            fg_color=("#3A3B5B", "#FFFFFF"),
            text_color=("#EDF2F4", "#2B2D42"),
            dropdown_fg_color=("#3A3B5B", "#FFFFFF"),
            dropdown_text_color=("#FFFFFF", "#000000"),  # White in dark, black in light
            button_color=("#4A4B6B", "#D3D3D3"),
            button_hover_color="#ADD8E6",  # Light blue for hover
            dropdown_hover_color = ("#000000", "#ffee05")
        )
        self.school_dropdown.pack(padx=17, pady=(10, 5), anchor="w")
        self.school_dropdown.set("Select your School")
        self.school_label = ctk.CTkLabel(
            self.input_frame,
            text="School",
            font=ctk.CTkFont(size=15),
            text_color=("#D3D3D3", "#4A4B6B"),
            anchor="w"
        )
        self.school_label.pack(anchor="w", pady=(0, 10), padx=20)

        # Competition Dropdown
        self.comp_var = tk.StringVar()
        self.comp_dropdown = ctk.CTkComboBox(
            self.input_frame,
            values=["Competition 1", "Competition 2", "Competition A3"],
            variable=self.comp_var,
            width=915,
            corner_radius=10,
            state="readonly",
            fg_color=("#3A3B5B", "#FFFFFF"),
            text_color=("#EDF2F4", "#2B2D42"),
            dropdown_fg_color=("#3A3B5B", "#FFFFFF"),
            dropdown_text_color=("#FFFFFF", "#000000"),  # White in dark, black in light
            button_color=("#4A4B6B", "#D3D3D3"),
            button_hover_color="#ADD8E6",  # Light blue for hover
            dropdown_hover_color=("#000000", "#ffee05")

        )
        self.comp_dropdown.set("Select a Competition")
        self.comp_dropdown.pack(padx=17,pady=(10, 5), anchor="w")
        self.comp_label = ctk.CTkLabel(
            self.input_frame,
            text="Competition",
            font=ctk.CTkFont(size=15),
            text_color=("#D3D3D3", "#4A4B6B"),
            anchor="w"
        )
        self.comp_label.pack(anchor="w", pady=(0, 10), padx=20)

        # Phone Number
        self.phone_entry = ctk.CTkEntry(
            self.input_frame,
            width=200,
            corner_radius=10,
            border_width=1,
            placeholder_text="Enter your phone number",
            fg_color=("#3A3B5B", "#FFFFFF"),
            text_color=("#EDF2F4", "#2B2D42"),
            border_color=("#4A4B6B", "#D3D3D3")
        )
        self.phone_entry.pack(padx=17,pady=(10, 5), anchor="w")
        self.phone_label = ctk.CTkLabel(
            self.input_frame,
            text="Phone Number",
            font=ctk.CTkFont(size=15),
            text_color=("#D3D3D3", "#4A4B6B"),
            anchor="w"
        )
        self.phone_label.pack(anchor="w", pady=(0, 10), padx=20)

        # Button Frame
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(fill="x", padx=20, pady=20)

        # Buttons with hover effect
        self.add_button = ctk.CTkButton(
            self.button_frame,
            text="Add",
            width=120,
            height=40,
            corner_radius=8,
            fg_color=("#EF233C", "#D90429"),
            hover_color=("#32b324")
        )
        self.add_button.pack(side="left", padx=10)

        self.remove_button = ctk.CTkButton(
            self.button_frame,
            text="Remove",
            width=120,
            height=40,
            corner_radius=8,
            fg_color=("#EF233C", "#D90429"),
            hover_color=("#32b324")
        )
        self.remove_button.pack(side="left", padx=10)

        self.update_button = ctk.CTkButton(
            self.button_frame,
            text="Update",
            width=120,
            height=40,
            corner_radius=8,
            fg_color=("#EF233C", "#D90429"),
            hover_color=("#32b324")
        )
        self.update_button.pack(side="left", padx=10)

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="Clear",
            width=120,
            height=40,
            corner_radius=8,
            fg_color=("#EF233C", "#D90429"),
            hover_color=("#32b324"),
            command=self.clear_fields
        )
        self.clear_button.pack(side="left", padx=10)

        self.download_button = ctk.CTkButton(
            self.button_frame,
            text="Download",
            width=120,
            height=40,
            corner_radius=8,
            fg_color=("#EF233C", "#D90429"),
            hover_color=("#32b324")
        )
        self.download_button.pack(side="left", padx=10)

        self.exit_button = ctk.CTkButton(
            self.button_frame,
            text="Exit",
            width=120,
            height=40,
            corner_radius=8,
            fg_color=("#EF233C", "#D90429"),
            hover_color=("#32b324"),
            command=self.root.destroy
        )
        self.exit_button.pack(side="left", padx=10)

        # Treeview Frame
        self.tree_frame = ctk.CTkFrame(self.main_frame, fg_color=("#2B2D42", "#EDF2F4"))
        self.tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Treeview with styled columns
        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=("RegNo", "FirstName", "LastName", "Class", "School", "Competition", "Phone"),
            show="headings",
            height=15,
            style="Custom.Treeview"
        )
        self.tree.heading("RegNo", text="Reg. No.")
        self.tree.heading("FirstName", text="First Name")
        self.tree.heading("LastName", text="Last Name")
        self.tree.heading("Class", text="Class")
        self.tree.heading("School", text="School")
        self.tree.heading("Competition", text="Competition")
        self.tree.heading("Phone", text="Phone")
        self.tree.column("RegNo", width=1, anchor="center")
        self.tree.column("FirstName", width=100, anchor="center")
        self.tree.column("LastName", width=80, anchor="center")
        self.tree.column("Class", width=1, anchor="center")
        self.tree.column("School", width=400, anchor="center")
        self.tree.column("Competition", width=110, anchor="center")
        self.tree.column("Phone", width=70, anchor="center")
        self.tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Scrollbar
        self.tree_scroll = ctk.CTkScrollbar(
            self.tree_frame,
            orientation="vertical",
            command=self.tree.yview,
            fg_color=("#2B2D42", "#EDF2F4"),
            button_color=("#4A4B6B", "#D3D3D3"),
            button_hover_color=("#EF233C", "#D90429")
        )
        self.tree_scroll.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.tree_scroll.set)

        # Configure Treeview style
        self.style = ttk.Style()
        self.update_treeview_style()

    def update_treeview_style(self):
        # Define colors based on current theme
        tree_bg = "#3A3B5B" if self.current_theme == "dark" else "#FFFFFF"
        tree_fg = "#EDF2F4" if self.current_theme == "dark" else "#2B2D42"
        heading_bg = "#4A4B6B" if self.current_theme == "dark" else "#A9A9A9"  # Darker gray for light theme
        heading_fg = "#000000" if self.current_theme == "dark" else "#1C2526"  # Darker text for light theme
        odd_row_bg = "#2B2D42" if self.current_theme == "dark" else "#F5F5F5"
        even_row_bg = "#3A3B5B" if self.current_theme == "dark" else "#FFFFFF"

        self.style.configure(
            "Custom.Treeview",
            background=tree_bg,
            foreground=tree_fg,
            fieldbackground=tree_bg,
            font=("Helvetica", 11),
            rowheight=30
        )
        self.style.configure(
            "Custom.Treeview.Heading",
            background=heading_bg,
            foreground=heading_fg,
            font=("Helvetica", 12, "bold"),
            borderwidth=1,
            relief="raised",
            padding=5
        )
        self.style.map(
            "Custom.Treeview.Heading",
            background=[("active", "#EF233C" if self.current_theme == "dark" else "#D90429")],
            foreground=[("active", "#FFFFFF" if self.current_theme == "dark" else "#1C2526")]
        )
        self.style.configure(
            "Custom.Treeview",
            highlightthickness=0,
            bd=0
        )
        self.style.map(
            "Custom.Treeview",
            background=[("selected", "#EF233C" if self.current_theme == "dark" else "#D90429")],
            foreground=[("selected", "#FFFFFF" if self.current_theme == "dark" else "#1C2526")]
        )
        # Configure row tags
        self.tree.tag_configure("oddrow", background=odd_row_bg)
        self.tree.tag_configure("evenrow", background=even_row_bg)


 #-----------------------------------------------------Functions------------------------------------------------------------------------------->
    #Toggle Button
    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        ctk.set_appearance_mode(self.current_theme)
        self.toggle_button.configure(text=f"{'Light' if self.current_theme == 'dark' else 'Dark'}")
        self.update_treeview_style()

    #Clear Button
    def clear_fields(self):
        # Clear text entry fields
        #self.reg_entry.delete(0, tk.END)                   ❌It is auto fill
        self.fname_entry.delete(0, tk.END)
        self.lname_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

        # Reset dropdowns
        self.class_var.set("Select Class")
        self.school_dropdown.set("Select your school")
        self.comp_dropdown.set("Select a Competition")

if __name__ == "__main__":
    root = ctk.CTk()
    app = RegistrationApp(root)
    root.mainloop()