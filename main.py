import TkInter
import TkInter.messagebox

from TkInter import *

window = Tk()
window.title("Shipley Painters")

# The different grids
Label(window, text = "Name").grid(row = 0)
name = Entry(window)
name.grid(row = 0, column = 1)

Label(window, text = "Height").grid(row = 1)
height = Entry(window)
height.grid(row = 1, column = 1)

Label(window, text = "Length 1").grid(row = 2)
length1 = Entry(window)
length1.grid(row = 2, column = 1)

Label(window, text = "Length 2").grid(row = 3)
length2 = Entry(window)
length2.grid(row = 3, column = 1)

Label(window, text = "Length 3").grid(row = 4)
Length3 = Entry(window)
Length3.grid(row = 4, column = 1)

Label(window, text = "Length 4").grid(row = 5)
Length4 = Entry(window)
Length4.grid(row = 5, column = 1)

# The options
paint_choice = IntVar()
paint_choice.set(2)
Radiobutton(window, text = "Luxury", variable = paint_choice, value = 1).grid(row = 7, column = 0)
Radiobutton(window, text = "Standard", variable = paint_choice, value = 2).grid(row = 7, column = 1)
Radiobutton(window, text = "Economy", variable = paint_choice, value = 3).grid(row = 7, column = 2)


# Undercoat option
use_undercoat = IntVar()
undercoat = Checkbutton(window, text = "Undercoat", variable = use_undercoat)
undercoat.grid(row = 8, column = 8)

# Calculation
def perform_calc():
   print(use_undercoat.get())

   paint_quality = paint_choice.get()
   area = int(height.get()) * int((length1.get() + length2.get() + length3.get() + length4.get())
   print_cost = 0
   if paint_quality == 1:
      paint_cost = 1.90
   elif paint_quality == 2:
      paint_cost = 1.00
   else:
      paint_cost = 0.60

   if use_undercoat.get():
       paint_cost += 0.50

   total_paint_cost = paint_cost * area

   itemised_total = f"total area = {area} \n" # appears in the message box
   itemised_total += f"Paint cost = {total_paint_cost}" # appears in the message box

# Message box
   TkInter.messagebox.showinfo("Alert Message", itemised_total)


TkInter.Button(window, text ="Calculate", command = perform_calc).grid(row = 10, column = 1)


window.mainloop()
