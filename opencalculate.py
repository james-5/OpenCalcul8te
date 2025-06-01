import tkinter as tk
from tkinter import ttk, messagebox
from calculations import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)
        self.create_home_tab()
        self.create_physics_tab()
        self.create_astronomy_tab()
        self.create_electromagnetism_tab()
        self.create_chemistry_tab()
        self.create_calculus_tab()
        self.create_fluid_dynamics_tab()
        self.root.geometry("800x600")
        self.physics_frame = self.notebook.nametowidget(self.notebook.tabs()[1])
        self.astro_frame = self.notebook.nametowidget(self.notebook.tabs()[2])
        self.em_frame = self.notebook.nametowidget(self.notebook.tabs()[3])
        self.chem_frame = self.notebook.nametowidget(self.notebook.tabs()[4])
        self.calculus_frame = self.notebook.nametowidget(self.notebook.tabs()[5])
        self.fluid_dynamics_frame = self.notebook.nametowidget(self.notebook.tabs()[6])

    def create_home_tab(self):
        home_frame = ttk.Frame(self.notebook)
        self.notebook.add(home_frame, text="Home")
        buttons = [
            ("Physics", lambda: self.notebook.select(1)),
            ("Astronomy", lambda: self.notebook.select(2)),
            ("Electromagnetism", lambda: self.notebook.select(3)),
            ("Chemistry", lambda: self.notebook.select(4)),
            ("Calculus", lambda: self.notebook.select(5)),
            ("Fluid Dynamics", lambda: self.notebook.select(6)),
            ("Exit", self.root.quit)
        ]
        for text, command in buttons:
            ttk.Button(home_frame, text=text, command=command).pack(pady=5)

    def create_physics_tab(self):
        self.physics_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.physics_frame, text="Physics")
        self.show_physics_menu()

    def show_physics_menu(self):
        for widget in self.physics_frame.winfo_children():
            widget.destroy()
        ttk.Button(self.physics_frame, text="Elastic Collision", command=self.show_elastic_collision).pack(pady=5)
        ttk.Button(self.physics_frame, text="Momentum", command=self.show_momentum).pack(pady=5)
        ttk.Button(self.physics_frame, text="Back to Home", command=lambda: self.notebook.select(0)).pack(pady=5)

    def show_elastic_collision(self):
        for widget in self.physics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.physics_frame, text="Elastic Collision: v1' = (m1-m2)/(m1+m2)*v1 + 2*m2*v2/(m1+m2)").pack(pady=10)
        main_frame = ttk.Frame(self.physics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.m1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="m1 (kg)").pack()
        self.m1_entry.pack(pady=5)
        self.m2_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="m2 (kg)").pack()
        self.m2_entry.pack(pady=5)
        self.v1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="v1 (m/s)").pack()
        self.v1_entry.pack(pady=5)
        self.v2_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="v2 (m/s)").pack()
        self.v2_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.v1_output = ttk.Label(outputs_frame, text="v1 new: - m/s")
        self.v1_output.pack(pady=5)
        self.v2_output = ttk.Label(outputs_frame, text="v2 new: - m/s")
        self.v2_output.pack(pady=5)
        button_frame = ttk.Frame(self.physics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_elastic).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_elastic).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_physics_menu).pack(side="left", padx=5)

    def calculate_elastic(self):
        try:
            m1 = float(self.m1_entry.get() or 0)
            m2 = float(self.m2_entry.get() or 0)
            v1 = float(self.v1_entry.get() or 0)
            v2 = float(self.v2_entry.get() or 0)
            v1_new, v2_new = calculate_elastic_collision(m1, m2, v1, v2)
            self.v1_output.config(text=f"v1 new: {v1_new:.2f} m/s")
            self.v2_output.config(text=f"v2 new: {v2_new:.2f} m/s")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Use numbers only.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Total mass cannot be zero.")

    def clear_elastic(self):
        self.m1_entry.delete(0, tk.END)
        self.m2_entry.delete(0, tk.END)
        self.v1_entry.delete(0, tk.END)
        self.v2_entry.delete(0, tk.END)
        self.v1_output.config(text="v1 new: - m/s")
        self.v2_output.config(text="v2 new: - m/s")

    def show_momentum(self):
        for widget in self.physics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.physics_frame, text="Momentum: p = m * v").pack(pady=10)
        main_frame = ttk.Frame(self.physics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.m_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="m (kg)").pack()
        self.m_entry.pack(pady=5)
        self.v_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="v (m/s)").pack()
        self.v_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.p_output = ttk.Label(outputs_frame, text="p: - kg·m/s")
        self.p_output.pack(pady=5)
        button_frame = ttk.Frame(self.physics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_momentum).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_momentum).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_physics_menu).pack(side="left", padx=5)

    def calculate_momentum(self):
        try:
            m = float(self.m_entry.get() or 0)
            v = float(self.v_entry.get() or 0)
            p = calculate_momentum(m, v)
            self.p_output.config(text=f"p: {p:.2f} kg·m/s")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Use numbers only.")

    def clear_momentum(self):
        self.m_entry.delete(0, tk.END)
        self.v_entry.delete(0, tk.END)
        self.p_output.config(text="p: - kg·m/s")

    def create_astronomy_tab(self):
        self.astro_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.astro_frame, text="Astronomy")
        self.show_astronomy_menu()

    def show_astronomy_menu(self):
        for widget in self.astro_frame.winfo_children():
            widget.destroy()
        ttk.Button(self.astro_frame, text="Parallax", command=self.show_parallax).pack(pady=5)
        ttk.Button(self.astro_frame, text="Back to Home", command=lambda: self.notebook.select(0)).pack(pady=5)

    def show_parallax(self):
        for widget in self.astro_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.astro_frame, text="Parallax: d = 1/p").pack(pady=10)
        main_frame = ttk.Frame(self.astro_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.p_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="p (arcseconds)").pack()
        self.p_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.d_output = ttk.Label(outputs_frame, text="d: - parsecs")
        self.d_output.pack(pady=5)
        button_frame = ttk.Frame(self.astro_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_parallax).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_parallax).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_astronomy_menu).pack(side="left", padx=5)

    def calculate_parallax(self):
        try:
            p = float(self.p_entry.get() or 0)
            d = calculate_parallax(p)
            self.d_output.config(text=f"d: {d:.2f} parsecs")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Use numbers only.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Parallax angle cannot be zero.")

    def clear_parallax(self):
        self.p_entry.delete(0, tk.END)
        self.d_output.config(text="d: - parsecs")

    def create_electromagnetism_tab(self):
        self.em_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.em_frame, text="Electromagnetism")
        self.show_electromagnetism_menu()

    def show_electromagnetism_menu(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Button(self.em_frame, text="Ohm's Law", command=self.show_ohms_law).pack(pady=5)
        ttk.Button(self.em_frame, text="Power Calculation", command=self.show_power_calculation).pack(pady=5)
        ttk.Button(self.em_frame, text="Resistors in Series", command=self.show_resistors_series).pack(pady=5)
        ttk.Button(self.em_frame, text="Resistors in Parallel", command=self.show_resistors_parallel).pack(pady=5)
        ttk.Button(self.em_frame, text="Gauss's Law (E)", command=self.show_gauss_law_e).pack(pady=5)
        ttk.Button(self.em_frame, text="Gauss's Law (B)", command=self.show_gauss_law_b).pack(pady=5)
        ttk.Button(self.em_frame, text="Faraday's Law", command=self.show_faraday_law).pack(pady=5)
        ttk.Button(self.em_frame, text="Ampère's Law", command=self.show_ampere_law).pack(pady=5)
        ttk.Button(self.em_frame, text="Back to Home", command=lambda: self.notebook.select(0)).pack(pady=5)

    def show_ohms_law(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Ohm's Law: V = I * R").pack(pady=10)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.v_ohm_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="V (volts, leave blank to solve)").pack()
        self.v_ohm_entry.pack(pady=5)
        self.i_ohm_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="I (amps, leave blank to solve)").pack()
        self.i_ohm_entry.pack(pady=5)
        self.r_ohm_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="R (ohms, leave blank to solve)").pack()
        self.r_ohm_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.v_ohm_output = ttk.Label(outputs_frame, text="V: - V")
        self.v_ohm_output.pack(pady=5)
        self.i_ohm_output = ttk.Label(outputs_frame, text="I: - A")
        self.i_ohm_output.pack(pady=5)
        self.r_ohm_output = ttk.Label(outputs_frame, text="R: - Ω")
        self.r_ohm_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_ohms_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_ohms_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_ohms_law(self):
        try:
            v = self.v_ohm_entry.get()
            i = self.i_ohm_entry.get()
            r = self.r_ohm_entry.get()
            v, i, r = calculate_ohms_law(v, i, r)
            self.v_ohm_output.config(text=f"V: {v:.2f} V")
            self.i_ohm_output.config(text=f"I: {i:.2f} A")
            self.r_ohm_output.config(text=f"R: {r:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_ohms_law(self):
        self.v_ohm_entry.delete(0, tk.END)
        self.i_ohm_entry.delete(0, tk.END)
        self.r_ohm_entry.delete(0, tk.END)
        self.v_ohm_output.config(text="V: - V")
        self.i_ohm_output.config(text="I: - A")
        self.r_ohm_output.config(text="R: - Ω")

    def show_power_calculation(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Power: P = V * I (or I^2*R, V^2/R)").pack(pady=10)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.v_power_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="V (volts, optional)").pack()
        self.v_power_entry.pack(pady=5)
        self.i_power_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="I (amps, optional)").pack()
        self.i_power_entry.pack(pady=5)
        self.r_power_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="R (ohms, optional)").pack()
        self.r_power_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.p_output = ttk.Label(outputs_frame, text="P: - W")
        self.p_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_power).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_power).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_power(self):
        try:
            v = self.v_power_entry.get()
            i = self.i_power_entry.get()
            r = self.r_power_entry.get()
            p = calculate_power(v, i, r)
            self.p_output.config(text=f"P: {p:.2f} W")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_power(self):
        self.v_power_entry.delete(0, tk.END)
        self.i_power_entry.delete(0, tk.END)
        self.r_power_entry.delete(0, tk.END)
        self.p_output.config(text="P: - W")

    def show_resistors_series(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Resistors in Series: Rtotal = R1 + R2").pack(pady=10)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.r1_series_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="R1 (ohms)").pack()
        self.r1_series_entry.pack(pady=5)
        self.r2_series_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="R2 (ohms)").pack()
        self.r2_series_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.rtotal_series_output = ttk.Label(outputs_frame, text="Rtotal: - Ω")
        self.rtotal_series_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_resistors_series).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_resistors_series).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_resistors_series(self):
        try:
            r1 = float(self.r1_series_entry.get() or 0)
            r2 = float(self.r2_series_entry.get() or 0)
            rtotal = calculate_resistors_series(r1, r2)
            self.rtotal_series_output.config(text=f"Rtotal: {rtotal:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_resistors_series(self):
        self.r1_series_entry.delete(0, tk.END)
        self.r2_series_entry.delete(0, tk.END)
        self.rtotal_series_output.config(text="Rtotal: - Ω")

    def show_resistors_parallel(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Resistors in Parallel: 1/Rtotal = 1/R1 + 1/R2").pack(pady=10)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.r1_parallel_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="R1 (ohms)").pack()
        self.r1_parallel_entry.pack(pady=5)
        self.r2_parallel_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="R2 (ohms)").pack()
        self.r2_parallel_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.rtotal_parallel_output = ttk.Label(outputs_frame, text="Rtotal: - Ω")
        self.rtotal_parallel_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_resistors_parallel).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_resistors_parallel).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_resistors_parallel(self):
        try:
            r1 = float(self.r1_parallel_entry.get() or 0)
            r2 = float(self.r2_parallel_entry.get() or 0)
            rtotal = calculate_resistors_parallel(r1, r2)
            self.rtotal_parallel_output.config(text=f"Rtotal: {rtotal:.2f} Ω")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_resistors_parallel(self):
        self.r1_parallel_entry.delete(0, tk.END)
        self.r2_parallel_entry.delete(0, tk.END)
        self.rtotal_parallel_output.config(text="Rtotal: - Ω")

    def show_gauss_law_e(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Gauss's Law (E): E * A = Q / ε₀ (ε₀ = 8.85e-12 C²/N·m²)").pack(pady=10)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.q_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Q (C)").pack()
        self.q_entry.pack(pady=5)
        self.a_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="A (m²)").pack()
        self.a_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.e_output = ttk.Label(outputs_frame, text="E: - V/m")
        self.e_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_gauss_law_e).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_gauss_law_e).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_gauss_law_e(self):
        try:
            q = float(self.q_entry.get() or 0)
            a = float(self.a_entry.get() or 0)
            e = calculate_gauss_law_e(q, a)
            self.e_output.config(text=f"E: {e:.2e} V/m")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_gauss_law_e(self):
        self.q_entry.delete(0, tk.END)
        self.a_entry.delete(0, tk.END)
        self.e_output.config(text="E: - V/m")

    def show_gauss_law_b(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Gauss's Law (B): Magnetic flux = 0 (no monopoles)").pack(pady=10)
        ttk.Label(self.em_frame, text="Enter any flux value to verify:").pack(pady=5)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.flux_b_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Flux (Wb)").pack()
        self.flux_b_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.flux_b_output = ttk.Label(outputs_frame, text="Result: -")
        self.flux_b_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Verify", command=self.calculate_gauss_law_b).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_gauss_law_b).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_gauss_law_b(self):
        try:
            flux = float(self.flux_b_entry.get() or 0)
            result = calculate_gauss_law_b(flux)
            self.flux_b_output.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Use numbers only.")

    def clear_gauss_law_b(self):
        self.flux_b_entry.delete(0, tk.END)
        self.flux_b_output.config(text="Result: -")

    def show_faraday_law(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Faraday's Law: ℰ = -dΦ_B/dt").pack(pady=10)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.dphi_b_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="ΔΦ_B (Wb)").pack()
        self.dphi_b_entry.pack(pady=5)
        self.dt_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Δt (s)").pack()
        self.dt_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.emf_output = ttk.Label(outputs_frame, text="ℰ: - V")
        self.emf_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_faraday_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_faraday_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_faraday_law(self):
        try:
            dphi_b = float(self.dphi_b_entry.get() or 0)
            dt = float(self.dt_entry.get() or 0)
            emf = calculate_faraday_law(dphi_b, dt)
            self.emf_output.config(text=f"ℰ: {emf:.2f} V")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_faraday_law(self):
        self.dphi_b_entry.delete(0, tk.END)
        self.dt_entry.delete(0, tk.END)
        self.emf_output.config(text="ℰ: - V")

    def show_ampere_law(self):
        for widget in self.em_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.em_frame, text="Ampère's Law: B * l = μ₀(I + ε₀ dΦ_E/dt) (μ₀ = 4πe-7 T·m/A, ε₀ = 8.85e-12 C²/N·m²)").pack(pady=10)
        main_frame = ttk.Frame(self.em_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.i_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="I (A)").pack()
        self.i_entry.pack(pady=5)
        self.dphi_e_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="ΔΦ_E (V·s)").pack()
        self.dphi_e_entry.pack(pady=5)
        self.dt_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Δt (s)").pack()
        self.dt_entry.pack(pady=5)
        self.l_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="l (m)").pack()
        self.l_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.b_output = ttk.Label(outputs_frame, text="B: - T")
        self.b_output.pack(pady=5)
        button_frame = ttk.Frame(self.em_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_ampere_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_ampere_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_electromagnetism_menu).pack(side="left", padx=5)

    def calculate_ampere_law(self):
        try:
            i = float(self.i_entry.get() or 0)
            dphi_e = float(self.dphi_e_entry.get() or 0)
            dt = float(self.dt_entry.get() or 0)
            l = float(self.l_entry.get() or 0)
            b = calculate_ampere_law(i, dphi_e, dt, l)
            self.b_output.config(text=f"B: {b:.2e} T")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_ampere_law(self):
        self.i_entry.delete(0, tk.END)
        self.dphi_e_entry.delete(0, tk.END)
        self.dt_entry.delete(0, tk.END)
        self.l_entry.delete(0, tk.END)
        self.b_output.config(text="B: - T")

    def create_chemistry_tab(self):
        self.chem_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.chem_frame, text="Chemistry")
        self.show_chemistry_menu()

    def show_chemistry_menu(self):
        for widget in self.chem_frame.winfo_children():
            widget.destroy()
        ttk.Button(self.chem_frame, text="pH Calculation", command=self.show_ph_calculation).pack(pady=5)
        ttk.Button(self.chem_frame, text="Back to Home", command=lambda: self.notebook.select(0)).pack(pady=5)

    def show_ph_calculation(self):
        for widget in self.chem_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.chem_frame, text="pH Calculation: pH = -log10[H+]").pack(pady=10)
        main_frame = ttk.Frame(self.chem_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.h_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="H+ conc (mol/L)").pack()
        self.h_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.ph_output = ttk.Label(outputs_frame, text="pH: -")
        self.ph_output.pack(pady=5)
        button_frame = ttk.Frame(self.chem_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_ph).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_ph).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_chemistry_menu).pack(side="left", padx=5)

    def calculate_ph(self):
        try:
            h = float(self.h_entry.get() or 0)
            ph = calculate_ph(h)
            self.ph_output.config(text=f"pH: {ph:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_ph(self):
        self.h_entry.delete(0, tk.END)
        self.ph_output.config(text="pH: -")

    def create_calculus_tab(self):
        self.calculus_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.calculus_frame, text="Calculus")
        self.show_calculus_menu()

    def show_calculus_menu(self):
        for widget in self.calculus_frame.winfo_children():
            widget.destroy()
        ttk.Button(self.calculus_frame, text="L'Hôpital's Rule", command=self.show_lhopital_rule).pack(pady=5)
        ttk.Button(self.calculus_frame, text="Derivative", command=self.show_derivative).pack(pady=5)
        ttk.Button(self.calculus_frame, text="Integral", command=self.show_integral).pack(pady=5)
        ttk.Button(self.calculus_frame, text="Back to Home", command=lambda: self.notebook.select(0)).pack(pady=5)

    def show_lhopital_rule(self):
        for widget in self.calculus_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.calculus_frame, text="L'Hôpital's Rule: lim (f'/g') as x -> a").pack(pady=10)
        main_frame = ttk.Frame(self.calculus_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.f_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="f(x) (e.g., x^2)").pack()
        self.f_entry.pack(pady=5)
        self.g_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="g(x) (e.g., x)").pack()
        self.g_entry.pack(pady=5)
        self.x_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="x approaching").pack()
        self.x_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.limit_output = ttk.Label(outputs_frame, text="Limit: -")
        self.limit_output.pack(pady=5)
        button_frame = ttk.Frame(self.calculus_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_lhopital_rule).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_lhopital_rule).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_calculus_menu).pack(side="left", padx=5)

    def calculate_lhopital_rule(self):
        try:
            f_str = self.f_entry.get() or "0"
            g_str = self.g_entry.get() or "0"
            x = float(self.x_entry.get() or 0)
            limit = calculate_lhopital_rule(f_str, g_str, x)
            self.limit_output.config(text=f"Limit: {limit:.2f}" if isinstance(limit, (int, float)) else f"Limit: {limit}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_lhopital_rule(self):
        self.f_entry.delete(0, tk.END)
        self.g_entry.delete(0, tk.END)
        self.x_entry.delete(0, tk.END)
        self.limit_output.config(text="Limit: -")

    def show_derivative(self):
        for widget in self.calculus_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.calculus_frame, text="Derivative: f'(x) at x").pack(pady=10)
        main_frame = ttk.Frame(self.calculus_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.f_deriv_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="f(x) (e.g., x^2)").pack()
        self.f_deriv_entry.pack(pady=5)
        self.x_deriv_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="x").pack()
        self.x_deriv_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.deriv_output = ttk.Label(outputs_frame, text="f'(x): -")
        self.deriv_output.pack(pady=5)
        button_frame = ttk.Frame(self.calculus_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_derivative).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_derivative).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_calculus_menu).pack(side="left", padx=5)

    def calculate_derivative(self):
        try:
            f_str = self.f_deriv_entry.get() or "0"
            x = float(self.x_deriv_entry.get() or 0)
            deriv = calculate_derivative(f_str, x)
            self.deriv_output.config(text=f"f'(x): {deriv:.2f}" if deriv is not None else "f'(x): Undefined")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_derivative(self):
        self.f_deriv_entry.delete(0, tk.END)
        self.x_deriv_entry.delete(0, tk.END)
        self.deriv_output.config(text="f'(x): -")

    def show_integral(self):
        for widget in self.calculus_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.calculus_frame, text="Integral: ∫f(x)dx from a to b").pack(pady=10)
        main_frame = ttk.Frame(self.calculus_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.f_int_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="f(x) (e.g., x^2)").pack()
        self.f_int_entry.pack(pady=5)
        self.a_int_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="a").pack()
        self.a_int_entry.pack(pady=5)
        self.b_int_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="b").pack()
        self.b_int_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.int_output = ttk.Label(outputs_frame, text="∫: -")
        self.int_output.pack(pady=5)
        button_frame = ttk.Frame(self.calculus_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_integral).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_integral).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_calculus_menu).pack(side="left", padx=5)

    def calculate_integral(self):
        try:
            f_str = self.f_int_entry.get() or "0"
            a = float(self.a_int_entry.get() or 0)
            b = float(self.b_int_entry.get() or 0)
            integral = calculate_integral(f_str, a, b)
            self.int_output.config(text=f"∫: {integral:.2f}" if integral is not None else "∫: Undefined")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_integral(self):
        self.f_int_entry.delete(0, tk.END)
        self.a_int_entry.delete(0, tk.END)
        self.b_int_entry.delete(0, tk.END)
        self.int_output.config(text="∫: -")

    def create_fluid_dynamics_tab(self):
        self.fluid_dynamics_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.fluid_dynamics_frame, text="Fluid Dynamics")
        self.show_fluid_dynamics_menu()

    def show_fluid_dynamics_menu(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Button(self.fluid_dynamics_frame, text="Supersonic Flow", command=self.show_supersonic_flow).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Compressible Flow", command=self.show_compressible_flow).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Heat Capacity Ratio", command=self.show_heat_capacity_ratio).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Lagrangian vs Eulerian", command=self.show_lagrangian_eulerian).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Lagrangian Trajectory", command=self.show_lagrangian_trajectory).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Boyle's Law", command=self.show_boyles_law).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Ideal Gas Law", command=self.show_ideal_gas_law).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Isentropic Flow", command=self.show_isentropic_flow).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Poiseuille's Law", command=self.show_poiseuille_law).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Venturi's Principle", command=self.show_venturi_principle).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Isentropic Nozzle Flow", command=self.show_isentropic_nozzle_flow).pack(pady=5)
        ttk.Button(self.fluid_dynamics_frame, text="Back to Home", command=lambda: self.notebook.select(0)).pack(pady=5)

    def show_supersonic_flow(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Supersonic Flow (γ = 1.4): Isentropic Relations").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.mach_supersonic_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Mach Number (>1)").pack()
        self.mach_supersonic_entry.pack(pady=5)
        self.p0_supersonic_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="P0 (Pa)").pack()
        self.p0_supersonic_entry.pack(pady=5)
        self.t0_supersonic_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="T0 (K)").pack()
        self.t0_supersonic_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.p_ratio_output = ttk.Label(outputs_frame, text="P/P0: -")
        self.p_ratio_output.pack(pady=5)
        self.t_ratio_output = ttk.Label(outputs_frame, text="T/T0: -")
        self.t_ratio_output.pack(pady=5)
        self.rho_ratio_output = ttk.Label(outputs_frame, text="ρ/ρ0: -")
        self.rho_ratio_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_supersonic_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_supersonic_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_supersonic_flow(self):
        try:
            mach = float(self.mach_supersonic_entry.get() or 0)
            p0 = float(self.p0_supersonic_entry.get() or 0)
            t0 = float(self.t0_supersonic_entry.get() or 0)
            p_ratio, t_ratio, rho_ratio = calculate_supersonic_flow(mach, p0, t0)
            self.p_ratio_output.config(text=f"P/P0: {p_ratio:.4f}")
            self.t_ratio_output.config(text=f"T/T0: {t_ratio:.4f}")
            self.rho_ratio_output.config(text=f"ρ/ρ0: {rho_ratio:.4f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_supersonic_flow(self):
        self.mach_supersonic_entry.delete(0, tk.END)
        self.p0_supersonic_entry.delete(0, tk.END)
        self.t0_supersonic_entry.delete(0, tk.END)
        self.p_ratio_output.config(text="P/P0: -")
        self.t_ratio_output.config(text="T/T0: -")
        self.rho_ratio_output.config(text="ρ/ρ0: -")

    def show_compressible_flow(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Compressible Flow: Mass Flow Rate").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.p0_comp_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="P0 (Pa)").pack()
        self.p0_comp_entry.pack(pady=5)
        self.t0_comp_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="T0 (K)").pack()
        self.t0_comp_entry.pack(pady=5)
        self.a_comp_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="A (m²)").pack()
        self.a_comp_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.mdot_output = ttk.Label(outputs_frame, text="Mass Flow Rate (kg/s): -")
        self.mdot_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_compressible_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_compressible_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_compressible_flow(self):
        try:
            p0 = float(self.p0_comp_entry.get() or 0)
            t0 = float(self.t0_comp_entry.get() or 0)
            a = float(self.a_comp_entry.get() or 0)
            mdot = calculate_compressible_flow(p0, t0, a)
            self.mdot_output.config(text=f"Mass Flow Rate (kg/s): {mdot:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_compressible_flow(self):
        self.p0_comp_entry.delete(0, tk.END)
        self.t0_comp_entry.delete(0, tk.END)
        self.a_comp_entry.delete(0, tk.END)
        self.mdot_output.config(text="Mass Flow Rate (kg/s): -")

    def show_heat_capacity_ratio(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Heat Capacity Ratio: γ = Cp/Cv").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.cp_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Cp (J/kg·K)").pack()
        self.cp_entry.pack(pady=5)
        self.cv_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Cv (J/kg·K)").pack()
        self.cv_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.gamma_output = ttk.Label(outputs_frame, text="γ: -")
        self.gamma_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_heat_capacity_ratio).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_heat_capacity_ratio).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_heat_capacity_ratio(self):
        try:
            cp = float(self.cp_entry.get() or 0)
            cv = float(self.cv_entry.get() or 0)
            gamma = calculate_heat_capacity_ratio(cp, cv)
            self.gamma_output.config(text=f"γ: {gamma:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_heat_capacity_ratio(self):
        self.cp_entry.delete(0, tk.END)
        self.cv_entry.delete(0, tk.END)
        self.gamma_output.config(text="γ: -")

    def show_lagrangian_eulerian(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Lagrangian vs Eulerian: Simple Flow Field").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.x0_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="x0 (initial position, m)").pack()
        self.x0_entry.pack(pady=5)
        self.t_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="t (time, s)").pack()
        self.t_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.lagrangian_output = ttk.Label(outputs_frame, text="Lagrangian x(t): - m")
        self.lagrangian_output.pack(pady=5)
        self.eulerian_output = ttk.Label(outputs_frame, text="Eulerian v(x,t): - m/s")
        self.eulerian_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_lagrangian_eulerian).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_lagrangian_eulerian).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_lagrangian_eulerian(self):
        try:
            x0 = float(self.x0_entry.get() or 0)
            t = float(self.t_entry.get() or 0)
            x_lagrangian, v = calculate_lagrangian_eulerian(x0, t)
            self.lagrangian_output.config(text=f"Lagrangian x(t): {x_lagrangian:.2f} m")
            self.eulerian_output.config(text=f"Eulerian v(x,t): {v:.2f} m/s")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Use numbers only.")

    def clear_lagrangian_eulerian(self):
        self.x0_entry.delete(0, tk.END)
        self.t_entry.delete(0, tk.END)
        self.lagrangian_output.config(text="Lagrangian x(t): - m")
        self.eulerian_output.config(text="Eulerian v(x,t): - m/s")

    def show_lagrangian_trajectory(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Lagrangian Trajectory: x(t) = x0 + v0*t").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.x0_traj_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="x0 (initial position, m)").pack()
        self.x0_traj_entry.pack(pady=5)
        self.v0_traj_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="v0 (initial velocity, m/s)").pack()
        self.v0_traj_entry.pack(pady=5)
        self.t_traj_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="t (time, s)").pack()
        self.t_traj_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.x_traj_output = ttk.Label(outputs_frame, text="x(t): - m")
        self.x_traj_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_lagrangian_trajectory).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_lagrangian_trajectory).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_lagrangian_trajectory(self):
        try:
            x0 = float(self.x0_traj_entry.get() or 0)
            v0 = float(self.v0_traj_entry.get() or 0)
            t = float(self.t_traj_entry.get() or 0)
            x = calculate_lagrangian_trajectory(x0, v0, t)
            self.x_traj_output.config(text=f"x(t): {x:.2f} m")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Use numbers only.")

    def clear_lagrangian_trajectory(self):
        self.x0_traj_entry.delete(0, tk.END)
        self.v0_traj_entry.delete(0, tk.END)
        self.t_traj_entry.delete(0, tk.END)
        self.x_traj_output.config(text="x(t): - m")

    def show_boyles_law(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Boyle's Law: P1 V1 = P2 V2").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.p1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="P1 (Pa)").pack()
        self.p1_entry.pack(pady=5)
        self.v1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="V1 (m³)").pack()
        self.v1_entry.pack(pady=5)
        self.v2_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="V2 (m³)").pack()
        self.v2_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.p2_output = ttk.Label(outputs_frame, text="P2: - Pa")
        self.p2_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_boyles_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_boyles_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_boyles_law(self):
        try:
            p1 = float(self.p1_entry.get() or 0)
            v1 = float(self.v1_entry.get() or 0)
            v2 = float(self.v2_entry.get() or 0)
            p2 = calculate_boyles_law(p1, v1, v2)
            self.p2_output.config(text=f"P2: {p2:.2f} Pa")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_boyles_law(self):
        self.p1_entry.delete(0, tk.END)
        self.v1_entry.delete(0, tk.END)
        self.v2_entry.delete(0, tk.END)
        self.p2_output.config(text="P2: - Pa")

    def show_ideal_gas_law(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Ideal Gas Law: PV = nRT (R = 0.0821 L·atm/(mol·K))").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.p_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="P (atm)").pack()
        self.p_entry.pack(pady=5)
        self.v_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="V (L)").pack()
        self.v_entry.pack(pady=5)
        self.n_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="n (mol)").pack()
        self.n_entry.pack(pady=5)
        self.t_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="T (K)").pack()
        self.t_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.ratio_output = ttk.Label(outputs_frame, text="PV/nT: - L·atm/mol·K")
        self.ratio_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_ideal_gas_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_ideal_gas_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_ideal_gas_law(self):
        try:
            p = float(self.p_entry.get() or 0)
            v = float(self.v_entry.get() or 0)
            n = float(self.n_entry.get() or 0)
            t = float(self.t_entry.get() or 0)
            ratio = calculate_ideal_gas_law(p, v, n, t)
            self.ratio_output.config(text=f"PV/nT: {ratio:.2f} L·atm/mol·K")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_ideal_gas_law(self):
        self.p_entry.delete(0, tk.END)
        self.v_entry.delete(0, tk.END)
        self.n_entry.delete(0, tk.END)
        self.t_entry.delete(0, tk.END)
        self.ratio_output.config(text="PV/nT: - L·atm/mol·K")

    def show_isentropic_flow(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Isentropic Flow: T2/T1 = (P2/P1)^((gamma-1)/gamma) (gamma = 1.4)").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.t1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="T1 (K)").pack()
        self.t1_entry.pack(pady=5)
        self.p1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="P1 (Pa)").pack()
        self.p1_entry.pack(pady=5)
        self.p2_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="P2 (Pa)").pack()
        self.p2_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.t2_output = ttk.Label(outputs_frame, text="T2: - K")
        self.t2_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_isentropic_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_isentropic_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_isentropic_flow(self):
        try:
            t1 = float(self.t1_entry.get() or 0)
            p1 = float(self.p1_entry.get() or 0)
            p2 = float(self.p2_entry.get() or 0)
            t2 = calculate_isentropic_flow(t1, p1, p2)
            self.t2_output.config(text=f"T2: {t2:.2f} K")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_isentropic_flow(self):
        self.t1_entry.delete(0, tk.END)
        self.p1_entry.delete(0, tk.END)
        self.p2_entry.delete(0, tk.END)
        self.t2_output.config(text="T2: - K")

    def show_poiseuille_law(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Poiseuille's Law: Q = π r^4 ΔP / (8 η L)").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.r_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="r (m)").pack()
        self.r_entry.pack(pady=5)
        self.delta_p_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="ΔP (Pa)").pack()
        self.delta_p_entry.pack(pady=5)
        self.eta_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="η (Pa·s)").pack()
        self.eta_entry.pack(pady=5)
        self.l_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="L (m)").pack()
        self.l_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.q_output = ttk.Label(outputs_frame, text="Q: - m³/s")
        self.q_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_poiseuille_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_poiseuille_law).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_poiseuille_law(self):
        try:
            r = float(self.r_entry.get() or 0)
            delta_p = float(self.delta_p_entry.get() or 0)
            eta = float(self.eta_entry.get() or 0)
            l = float(self.l_entry.get() or 0)
            q = calculate_poiseuille_law(r, delta_p, eta, l)
            self.q_output.config(text=f"Q: {q:.2e} m³/s")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_poiseuille_law(self):
        self.r_entry.delete(0, tk.END)
        self.delta_p_entry.delete(0, tk.END)
        self.eta_entry.delete(0, tk.END)
        self.l_entry.delete(0, tk.END)
        self.q_output.config(text="Q: - m³/s")

    def show_venturi_principle(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Venturi's Principle: A1 v1 = A2 v2").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.a1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="A1 (m²)").pack()
        self.a1_entry.pack(pady=5)
        self.a2_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="A2 (m²)").pack()
        self.a2_entry.pack(pady=5)
        self.v1_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="v1 (m/s)").pack()
        self.v1_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.v2_output = ttk.Label(outputs_frame, text="v2: - m/s")
        self.v2_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_venturi_principle).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_venturi_principle).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_venturi_principle(self):
        try:
            a1 = float(self.a1_entry.get() or 0)
            a2 = float(self.a2_entry.get() or 0)
            v1 = float(self.v1_entry.get() or 0)
            v2 = calculate_venturi_principle(a1, a2, v1)
            self.v2_output.config(text=f"v2: {v2:.2f} m/s")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_venturi_principle(self):
        self.a1_entry.delete(0, tk.END)
        self.a2_entry.delete(0, tk.END)
        self.v1_entry.delete(0, tk.END)
        self.v2_output.config(text="v2: - m/s")

    def show_isentropic_nozzle_flow(self):
        for widget in self.fluid_dynamics_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.fluid_dynamics_frame, text="Isentropic Nozzle Flow: A/A* (γ = 1.4)").pack(pady=10)
        main_frame = ttk.Frame(self.fluid_dynamics_frame)
        main_frame.pack(fill="both", expand=True)
        inputs_frame = ttk.Frame(main_frame)
        inputs_frame.pack(side="left", padx=20, pady=20)
        self.mach_nozzle_entry = ttk.Entry(inputs_frame)
        ttk.Label(inputs_frame, text="Mach Number").pack()
        self.mach_nozzle_entry.pack(pady=5)
        outputs_frame = ttk.Frame(main_frame)
        outputs_frame.pack(side="right", padx=20, pady=20)
        self.area_ratio_output = ttk.Label(outputs_frame, text="A/A*: -")
        self.area_ratio_output.pack(pady=5)
        button_frame = ttk.Frame(self.fluid_dynamics_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate", command=self.calculate_isentropic_nozzle_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_isentropic_nozzle_flow).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_fluid_dynamics_menu).pack(side="left", padx=5)

    def calculate_isentropic_nozzle_flow(self):
        try:
            mach = float(self.mach_nozzle_entry.get() or 0)
            area_ratio = calculate_isentropic_nozzle_flow(mach)
            self.area_ratio_output.config(text=f"A/A*: {area_ratio:.4f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_isentropic_nozzle_flow(self):
        self.mach_nozzle_entry.delete(0, tk.END)
        self.area_ratio_output.config(text="A/A*: -")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()