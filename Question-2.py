import tkinter as tk
from tkinter import messagebox

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail Store")

        # Create a dictionary to store product details
        self.products = {
            "Product1": {"price": 5.99},
            "Product2": {"price": 10.99},
            # Add more products here
        }

        # Create variables to track cart and total cost
        self.cart = {}
        self.total_cost = tk.DoubleVar()
        self.total_cost.set(0.0)

        # Create a label for the product details
        self.product_label = tk.Label(root, text="Product Details:")
        self.product_label.pack()

        # Create a listbox to display product names
        self.product_listbox = tk.Listbox(root)
        for product in self.products.keys():
            self.product_listbox.insert(tk.END, product)
        self.product_listbox.pack()

        # Create an "Add to Cart" button
        self.add_to_cart_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack()

        # Create a label to display the cart
        self.cart_label = tk.Label(root, text="Cart:")
        self.cart_label.pack()

        # Create a listbox to display cart items
        self.cart_listbox = tk.Listbox(root)
        self.cart_listbox.pack()

        # Create a label to display the total cost
        self.total_cost_label = tk.Label(root, text="Total Cost:")
        self.total_cost_label.pack()

        # Create a label to display the total cost
        self.total_cost_display = tk.Label(root, textvariable=self.total_cost)
        self.total_cost_display.pack()

        # Create an "Place Order" button
        self.place_order_button = tk.Button(root, text="Place Order", command=self.place_order)
        self.place_order_button.pack()

    def add_to_cart(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            price = self.products.get(selected_product, {}).get("price", 0.0)
            self.cart[selected_product] = price
            self.cart_listbox.insert(tk.END, selected_product)
            self.total_cost.set(self.total_cost.get() + price)

    def place_order(self):
        if not self.cart:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")
        else:
            messagebox.showinfo("Order Placed", f"Total Cost: ${self.total_cost.get()}")
            self.cart = {}
            self.cart_listbox.delete(0, tk.END)
            self.total_cost.set(0.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()
