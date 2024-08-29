import tkinter as tk
from gui import DailyPlannerGUI

def main():
    root = tk.Tk()
    app = DailyPlannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()