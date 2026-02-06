"""UI style utilities for the Tkinter/ttk app.

Best practice: keep styling separated from logic. This module provides
`UIStyle` to apply a consistent HD-friendly look and feel.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont


class UIStyle:
    """Apply HD-friendly ttk theme, fonts, and widget styles."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.style = ttk.Style()

    def apply(self):
        # Window size for HD screens; start maximized on Windows for full-width UI
        self.root.geometry("1280x720")
        self.root.minsize(1000, 700)
        try:
            # Windows full screen (maximized) for HD look
            self.root.state("zoomed")
        except Exception:
            pass
        self._set_scaling(1.15)

        # Theme selection: use 'clam' (reliable for custom colors), fallback to default
        self._set_theme(preferred=("clam", "vista", "default"))

        # Base fonts (slightly larger than defaults for HD)
        self._configure_fonts()

        # Basic widget styles and a primary button style
        self._configure_styles()

        # Layout (grid) is configured in main.py; keep style class focused on visuals

    # --- internals ---
    def _set_scaling(self, factor: float):
        try:
            # Increase logical pixel scaling for high-DPI displays
            self.root.tk.call("tk", "scaling", factor)
        except Exception:
            pass

    def _set_theme(self, preferred=("clam",)):
        available = set(self.style.theme_names())
        for name in preferred:
            if name in available:
                self.style.theme_use(name)
                return
        # fallback to current theme

    def _configure_fonts(self):
        try:
            default = tkfont.nametofont("TkDefaultFont")
            default.configure(size=11)
            textfont = tkfont.nametofont("TkTextFont")
            textfont.configure(size=11)
            heading = tkfont.nametofont("TkHeadingFont")
            heading.configure(size=12, weight="bold")
        except Exception:
            pass

    def _configure_styles(self):
        # Padding
        self.style.configure("TLabel", padding=2)
        self.style.configure("TEntry", padding=2)
        self.style.configure("TButton", padding=6)

        # Primary button style (works well with 'clam')
        primary_bg = "#2563EB"  # blue 600
        primary_bg_active = "#1D4ED8"  # blue 700
        self.style.configure(
            "Primary.TButton",
            foreground="white",
            background=primary_bg,
            borderwidth=0,
        )
        self.style.map(
            "Primary.TButton",
            background=[("active", primary_bg_active), ("pressed", primary_bg_active)],
            foreground=[("disabled", "#cccccc")],
        )
