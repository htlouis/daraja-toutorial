import tkinter as tk
from tkinter import messagebox

class InventoryAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory App")
        
        self.inventory = []

        self.label = tk.Label(root, text="Inventory App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.name_label = tk.Label(root, text="Item Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=10)

        self.display_button = tk.Button(root, text="Display Inventory", command=self.display_inventory)
        self.display_button.pack(pady=10)

    def add_item(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if name and quantity and price:
            self.inventory.append({"name": name, "quantity": quantity, "price": price})
            messagebox.showinfo("Success", "Item added to inventory.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def display_inventory(self):
        if self.inventory:
            inventory_window = tk.Toplevel(self.root)
            inventory_window.title("Inventory")
            
            inventory_label = tk.Label(inventory_window, text="Inventory", font=("Helvetica", 14))
            inventory_label.pack()

            for item in self.inventory:
                item_label = tk.Label(inventory_window, text=f"{item['name']} - Quantity: {item['quantity']} - Price: {item['price']}")
                item_label.pack()

        else:
            messagebox.showinfo("Inventory", "Inventory is empty.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryAppGUI(root)
    root.mainloop()
