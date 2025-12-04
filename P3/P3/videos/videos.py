"""
Sistema de Registro de Usuarios - Python Tkinter
Interfaz gráfica personalizada con validaciones completas
"""

import tkinter as tk
from tkinter import ttk, messagebox
import re
from typing import Dict, Optional

class GradientFrame(tk.Canvas):
    """Frame con gradiente personalizado"""
    def __init__(self, parent, color1="#a0e7e5", color2="#7dd3c0", **kwargs):
        super().__init__(parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind("<Configure>", self._draw_gradient)
    
    def _draw_gradient(self, event=None):
        """Dibuja el gradiente"""
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = height
        
        r1, g1, b1 = self._hex_to_rgb(self.color1)
        r2, g2, b2 = self._hex_to_rgb(self.color2)
        
        for i in range(limit):
            nr = int(r1 + (r2 - r1) * i / limit)
            ng = int(g1 + (g2 - g1) * i / limit)
            nb = int(b1 + (b2 - b1) * i / limit)
            color = f"#{nr:02x}{ng:02x}{nb:02x}"
            self.create_line(0, i, width, i, fill=color, tags="gradient")
    
    def _hex_to_rgb(self, hex_color):
        """Convierte color hexadecimal a RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


class PlaceholderEntry(tk.Entry):
    """Entry personalizado con placeholder"""
    def __init__(self, parent, placeholder="", show="", **kwargs):
        super().__init__(parent, **kwargs)
        self.placeholder = placeholder
        self.show_char = show
        self.placeholder_color = "#999999"
        self.default_color = "#0a0a0a"
        self.has_placeholder = True
        
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
        self._add_placeholder()
    
    def _clear_placeholder(self, event=None):
        if self.has_placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_color, show=self.show_char)
            self.has_placeholder = False
    
    def _add_placeholder(self, event=None):
        if not self.get():
            self.config(show="")
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)
            self.has_placeholder = True
    
    def get_value(self):
        """Obtiene el valor real del entry"""
        if self.has_placeholder:
            return ""
        return self.get()


class PasswordEntry(tk.Frame):
    """Entry de contraseña con botón de mostrar/ocultar"""
    def __init__(self, parent, placeholder="", **kwargs):
        super().__init__(parent, bg="white")
        self.show_password = False
        
        self.entry = PlaceholderEntry(
            self, 
            placeholder=placeholder,
            show="•",
            font=("Arial", 11),
            bg="white",
            fg="#0a0a0a",
            relief="flat",
            bd=0
        )
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0), pady=8)
        
        self.toggle_btn = tk.Button(
            self,
            text="👁",
            font=("Arial", 10),
            bg="white",
            fg="#6a7282",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self._toggle_password
        )
        self.toggle_btn.pack(side=tk.RIGHT, padx=8)
    
    def _toggle_password(self):
        """Alterna entre mostrar/ocultar contraseña"""
        self.show_password = not self.show_password
        if not self.entry.has_placeholder:
            if self.show_password:
                self.entry.config(show="")
                self.toggle_btn.config(text="👁‍🗨")
            else:
                self.entry.config(show="•")
                self.toggle_btn.config(text="👁")
    
    def get_value(self):
        return self.entry.get_value()


class RoundedButton(tk.Canvas):
    """Botón redondeado personalizado"""
    def __init__(self, parent, text="", command=None, bg_color="#7dd3c0", 
                 fg_color="white", hover_color="#6bc4b1", **kwargs):
        super().__init__(parent, highlightthickness=0, **kwargs)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.fg_color = fg_color
        self.text = text
        self.command = command
        
        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Configure>", self._draw_button)
    
    def _draw_button(self, event=None):
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        
        # Dibuja rectángulo redondeado
        radius = 10
        self.create_arc(0, 0, radius*2, radius*2, start=90, extent=90, 
                       fill=self.bg_color, outline="")
        self.create_arc(width-radius*2, 0, width, radius*2, start=0, extent=90, 
                       fill=self.bg_color, outline="")
        self.create_arc(0, height-radius*2, radius*2, height, start=180, extent=90, 
                       fill=self.bg_color, outline="")
        self.create_arc(width-radius*2, height-radius*2, width, height, start=270, extent=90, 
                       fill=self.bg_color, outline="")
        
        self.create_rectangle(radius, 0, width-radius, height, 
                            fill=self.bg_color, outline="")
        self.create_rectangle(0, radius, width, height-radius, 
                            fill=self.bg_color, outline="")
        
        # Dibuja texto
        self.create_text(width/2, height/2, text=self.text, 
                        fill=self.fg_color, font=("Arial", 11, "bold"))
    
    def _on_click(self, event):
        if self.command:
            self.command()
    
    def _on_enter(self, event):
        old_color = self.bg_color
        self.bg_color = self.hover_color
        self._draw_button()
        self.bg_color = old_color
    
    def _on_leave(self, event):
        self._draw_button()


class RegistroApp:
    """Aplicación principal de registro"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Usuarios")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Variables del formulario
        self.form_data = {
            'nombre': None,
            'apellido_paterno': None,
            'apellido_materno': None,
            'tipo': None,
            'email': None,
            'password': None,
            'confirm_password': None
        }
        
        self.error_labels = {}
        
        self._create_ui()
    
    def _create_ui(self):
        """Crea la interfaz de usuario"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f1f5f9")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Frame contenedor con sombra simulada
        container = tk.Frame(main_frame, bg="white", relief="flat")
        container.pack(fill=tk.BOTH, expand=True)
        
        # Panel lateral izquierdo con gradiente
        left_panel = GradientFrame(container, color1="#a0e7e5", color2="#7dd3c0", 
                                   width=250, highlightthickness=0)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH)
        
        # Icono en el panel izquierdo (simulando transparencia con color más claro)
        icon_frame = tk.Frame(left_panel, bg="#b8e9e7", width=80, height=80)
        icon_frame.place(x=35, y=200)
        
        icon_label = tk.Label(icon_frame, text="🏠", font=("Arial", 35), 
                             bg="#b8e9e7", fg="white")
        icon_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Texto de bienvenida
        welcome_label = tk.Label(left_panel, text="Bienvenido", 
                                font=("Arial", 14), bg="#a0e7e5", fg="white")
        left_panel.create_window(35, 304, anchor="nw", window=welcome_label)
        
        desc_label = tk.Label(left_panel, text="Crea tu cuenta en\nsolo unos minutos", 
                             font=("Arial", 11), bg="#8adcd8", fg="white", justify="left")
        left_panel.create_window(35, 340, anchor="nw", window=desc_label)
        
        # Panel derecho con formulario
        right_panel = tk.Frame(container, bg="white")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Canvas con scrollbar para el formulario
        canvas = tk.Canvas(right_panel, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(right_panel, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Título del formulario
        title_frame = tk.Frame(scrollable_frame, bg="white")
        title_frame.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        title_label = tk.Label(title_frame, text="Crear cuenta", 
                              font=("Arial", 18, "bold"), bg="white", fg="#101828")
        title_label.pack(anchor="w")
        
        subtitle_label = tk.Label(title_frame, text="Ingresa tus datos personales", 
                                 font=("Arial", 10), bg="white", fg="#6a7282")
        subtitle_label.pack(anchor="w")
        
        # Formulario
        form_frame = tk.Frame(scrollable_frame, bg="white")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Campo: Nombre
        self._create_field(form_frame, "Nombre(s)", "nombre", "Juan Carlos")
        
        # Campo: Apellido Paterno
        self._create_field(form_frame, "Apellido Paterno", "apellido_paterno", "García")
        
        # Campo: Apellido Materno
        self._create_field(form_frame, "Apellido Materno", "apellido_materno", "López")
        
        # Campo: Tipo de Usuario
        self._create_combobox_field(form_frame, "Tipo de Usuario", "tipo", 
                                   ["Directivo", "Admin", "Estudiante", "Trabajador"])
        
        # Campo: Email
        self._create_field(form_frame, "Correo Electrónico", "email", 
                          "correo@ejemplo.com")
        
        # Campo: Contraseña
        self._create_password_field(form_frame, "Contraseña", "password", "••••••••")
        
        # Campo: Confirmar Contraseña
        self._create_password_field(form_frame, "Confirmar Contraseña", 
                                   "confirm_password", "••••••••")
        
        # Botones
        button_frame = tk.Frame(form_frame, bg="white")
        button_frame.pack(fill=tk.X, pady=(15, 10))
        
        create_btn = RoundedButton(
            button_frame, 
            text="Crear cuenta",
            command=self._submit_form,
            bg_color="#7dd3c0",
            hover_color="#6bc4b1",
            height=40,
            bg="white"
        )
        create_btn.pack(fill=tk.X, pady=(0, 8))
        
        reset_btn = RoundedButton(
            button_frame,
            text="🏠 Volver a inicio",
            command=self._reset_form,
            bg_color="white",
            fg_color="#7dd3c0",
            hover_color="#f8f9fa",
            height=40,
            bg="white"
        )
        reset_btn.pack(fill=tk.X)
        
        # Configura el canvas y scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Habilita scroll con rueda del mouse
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def _create_field(self, parent, label_text, field_name, placeholder):
        """Crea un campo de texto estándar"""
        field_frame = tk.Frame(parent, bg="white")
        field_frame.pack(fill=tk.X, pady=(0, 8))
        
        # Label
        label = tk.Label(field_frame, text=f"{label_text} *", 
                        font=("Arial", 10), bg="white", fg="#364153")
        label.pack(anchor="w", pady=(0, 4))
        
        # Entry con borde
        entry_container = tk.Frame(field_frame, bg="#d1d5dc", bd=1)
        entry_container.pack(fill=tk.X)
        
        entry = PlaceholderEntry(entry_container, placeholder=placeholder,
                                font=("Arial", 11), bg="white", fg="#0a0a0a",
                                relief="flat", bd=0)
        entry.pack(fill=tk.BOTH, padx=1, pady=1, ipady=6, ipadx=8)
        
        self.form_data[field_name] = entry
        
        # Label de error
        error_label = tk.Label(field_frame, text="", font=("Arial", 9), 
                              bg="white", fg="#fb2c36")
        error_label.pack(anchor="w")
        self.error_labels[field_name] = error_label
    
    def _create_password_field(self, parent, label_text, field_name, placeholder):
        """Crea un campo de contraseña con botón de mostrar/ocultar"""
        field_frame = tk.Frame(parent, bg="white")
        field_frame.pack(fill=tk.X, pady=(0, 8))
        
        # Label
        label = tk.Label(field_frame, text=f"{label_text} *", 
                        font=("Arial", 10), bg="white", fg="#364153")
        label.pack(anchor="w", pady=(0, 4))
        
        # Entry container con borde
        entry_container = tk.Frame(field_frame, bg="#d1d5dc", bd=1)
        entry_container.pack(fill=tk.X)
        
        password_entry = PasswordEntry(entry_container, placeholder=placeholder)
        password_entry.pack(fill=tk.BOTH, padx=1, pady=1)
        
        self.form_data[field_name] = password_entry
        
        # Label de error
        error_label = tk.Label(field_frame, text="", font=("Arial", 9), 
                              bg="white", fg="#fb2c36")
        error_label.pack(anchor="w")
        self.error_labels[field_name] = error_label
    
    def _create_combobox_field(self, parent, label_text, field_name, values):
        """Crea un campo de selección (combobox)"""
        field_frame = tk.Frame(parent, bg="white")
        field_frame.pack(fill=tk.X, pady=(0, 8))
        
        # Label
        label = tk.Label(field_frame, text=f"{label_text} *", 
                        font=("Arial", 10), bg="white", fg="#364153")
        label.pack(anchor="w", pady=(0, 4))
        
        # Combobox con estilo personalizado
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.TCombobox',
                       fieldbackground="white",
                       background="white",
                       bordercolor="#d1d5dc",
                       arrowcolor="#6a7282")
        
        combo_var = tk.StringVar()
        combo = ttk.Combobox(field_frame, textvariable=combo_var, 
                            values=values, state="readonly",
                            font=("Arial", 11), style='Custom.TCombobox')
        combo.set("Selecciona un tipo")
        combo.pack(fill=tk.X, ipady=6)
        
        self.form_data[field_name] = combo_var
        
        # Label de error
        error_label = tk.Label(field_frame, text="", font=("Arial", 9), 
                              bg="white", fg="#fb2c36")
        error_label.pack(anchor="w")
        self.error_labels[field_name] = error_label
    
    def _clear_errors(self):
        """Limpia todos los mensajes de error"""
        for error_label in self.error_labels.values():
            error_label.config(text="")
    
    def _show_error(self, field_name, message):
        """Muestra un mensaje de error en un campo"""
        if field_name in self.error_labels:
            self.error_labels[field_name].config(text=message)
    
    def _validate_form(self) -> bool:
        """Valida el formulario completo"""
        self._clear_errors()
        is_valid = True
        
        # Validar nombre
        nombre = self.form_data['nombre'].get_value()
        if not nombre.strip():
            self._show_error('nombre', "El nombre es requerido")
            is_valid = False
        
        # Validar apellido paterno
        apellido_paterno = self.form_data['apellido_paterno'].get_value()
        if not apellido_paterno.strip():
            self._show_error('apellido_paterno', "El apellido paterno es requerido")
            is_valid = False
        
        # Validar apellido materno
        apellido_materno = self.form_data['apellido_materno'].get_value()
        if not apellido_materno.strip():
            self._show_error('apellido_materno', "El apellido materno es requerido")
            is_valid = False
        
        # Validar tipo
        tipo = self.form_data['tipo'].get()
        if not tipo or tipo == "Selecciona un tipo":
            self._show_error('tipo', "Selecciona un tipo de usuario")
            is_valid = False
        
        # Validar email
        email = self.form_data['email'].get_value()
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not email.strip():
            self._show_error('email', "El correo electrónico es requerido")
            is_valid = False
        elif not re.match(email_regex, email):
            self._show_error('email', "El correo electrónico no es válido")
            is_valid = False
        
        # Validar contraseña
        password = self.form_data['password'].get_value()
        if not password:
            self._show_error('password', "La contraseña es requerida")
            is_valid = False
        elif len(password) < 8:
            self._show_error('password', "La contraseña debe tener al menos 8 caracteres")
            is_valid = False
        
        # Validar confirmación de contraseña
        confirm_password = self.form_data['confirm_password'].get_value()
        if not confirm_password:
            self._show_error('confirm_password', "Confirma tu contraseña")
            is_valid = False
        elif password != confirm_password:
            self._show_error('confirm_password', "Las contraseñas no coinciden")
            is_valid = False
        
        return is_valid
    
    def _submit_form(self):
        """Procesa el envío del formulario"""
        if self._validate_form():
            nombre = self.form_data['nombre'].get_value()
            apellido_paterno = self.form_data['apellido_paterno'].get_value()
            apellido_materno = self.form_data['apellido_materno'].get_value()
            tipo = self.form_data['tipo'].get()
            email = self.form_data['email'].get_value()
            
            mensaje = f"""¡Cuenta creada exitosamente!

Nombre: {nombre} {apellido_paterno} {apellido_materno}
Email: {email}
Tipo: {tipo}

Los datos han sido registrados correctamente."""
            
            messagebox.showinfo("Registro Exitoso", mensaje)
            self._reset_form()
    
    def _reset_form(self):
        """Reinicia el formulario"""
        self._clear_errors()
        
        # Reiniciar campos de texto
        for field_name, widget in self.form_data.items():
            if isinstance(widget, PlaceholderEntry):
                widget.delete(0, tk.END)
                widget._add_placeholder()
            elif isinstance(widget, PasswordEntry):
                widget.entry.delete(0, tk.END)
                widget.entry._add_placeholder()
                widget.show_password = False
                widget.toggle_btn.config(text="👁")
            elif isinstance(widget, tk.StringVar):
                widget.set("Selecciona un tipo")


def main():
    """Función principal"""
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()