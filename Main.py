import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime

class Employee:
    """Represents an employee with various personal and professional details."""
    def __init__(self, employeeID, name, department, jobTitle, basicSalary, managerID):
        self.employeeID = employeeID
        self.name = name
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.managerID = managerID

    def get_details(self):
        return f"{self.name}, {self.department}, {self.jobTitle}, Salary: ${self.basicSalary}, Manager ID: {self.managerID}"

class Event:
    """Represents an event managed by the company."""
    def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, guests,
                 caterer, cleaner, decorator, entertainer, furnitureSupplier, invoice):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress
        self.clientID = clientID
        self.guests = guests  # List of guest IDs
        self.caterer = caterer
        self.cleaner = cleaner
        self.decorator = decorator
        self.entertainer = entertainer
        self.furnitureSupplier = furnitureSupplier
        self.invoice = invoice

    def get_details(self):
        guest_ids = ', '.join(map(str, self.guests))
        details = (f"Type: {self.type}, Theme: {self.theme}, Date: {self.date.date()}, Time: {self.time}, "
                   f"Duration: {self.duration} hours, Venue: {self.venueAddress}, Client ID: {self.clientID}, "
                   f"Guests: {guest_ids}, Catering: {self.caterer}, Cleaning: {self.cleaner}, "
                   f"Decorations: {self.decorator}, Entertainment: {self.entertainer}, "
                   f"Furniture: {self.furnitureSupplier}, Invoice: {self.invoice}")
        return details


class Client:
    """Represents a client who organizes events."""
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

    def get_details(self):
        return f"Name: {self.name}, Address: {self.address}, Contact: {self.contactDetails}, Budget: ${self.budget}"
class Guest:
    """Represents a guest attending an event."""
    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

    def get_details(self):
        return f"Name: {self.name}, Address: {self.address}, Contact: {self.contactDetails}"
class Supplier:
    """Represents a supplier providing services for an event."""
    def __init__(self, supplierID, name, service, contactDetails):
        self.supplierID = supplierID
        self.name = name
        self.service = service
        self.contactDetails = contactDetails

    def get_details(self):
        return f"Name: {self.name}, Service: {self.service}, Contact: {self.contactDetails}"
class Venue:
    """Represents a venue where events are held."""
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    def get_details(self):
        return f"Name: {self.name}, Address: {self.address}, Contact: {self.contact}, Capacity: {self.minGuests}-{self.maxGuests} guests"
class Caterer:
    """Specific supplier type for catering services at events."""
    def __init__(self, catererID, name, address, contactDetails, menu, minGuests, maxGuests):
        self.catererID = catererID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.menu = menu
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    def get_details(self):
        return (f"Name: {self.name}, Address: {self.address}, Contact: {self.contactDetails}, "
                f"Menu: {self.menu}, Min Guests: {self.minGuests}, Max Guests: {self.maxGuests}")

class EventManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.load_data()
        self.create_management_buttons()

    def load_data(self):
        try:
            with open('employees.pkl', 'rb') as f:
                self.employees = pickle.load(f)
        except FileNotFoundError:
            self.employees = {}

        try:
            with open('events.pkl', 'rb') as f:
                self.events = pickle.load(f)
        except FileNotFoundError:
            self.events = {}

        try:
            with open('clients.pkl', 'rb') as f:
                self.clients = pickle.load(f)
        except FileNotFoundError:
            self.clients = {}

        try:
            with open('guests.pkl', 'rb') as f:
                self.guests = pickle.load(f)
        except FileNotFoundError:
            self.guests = {}

        try:
            with open('suppliers.pkl', 'rb') as f:
                self.suppliers = pickle.load(f)
        except FileNotFoundError:
            self.suppliers = {}

        try:
            with open('venues.pkl', 'rb') as f:
                self.venues = pickle.load(f)
        except FileNotFoundError:
            self.venues = {}

        try:
            with open('caterers.pkl', 'rb') as f:
                self.caterers = pickle.load(f)
        except FileNotFoundError:
            self.caterers = {}

    def save_data(self):
        with open('employees.pkl', 'wb') as f:
            pickle.dump(self.employees, f)

        with open('events.pkl', 'wb') as f:
            pickle.dump(self.events, f)

        with open('clients.pkl', 'wb') as f:
            pickle.dump(self.clients, f)

        with open('guests.pkl', 'wb') as f:
            pickle.dump(self.guests, f)

        with open('suppliers.pkl', 'wb') as f:
            pickle.dump(self.suppliers, f)

        with open('venues.pkl', 'wb') as f:
            pickle.dump(self.venues, f)

        with open('caterers.pkl', 'wb') as f:
            pickle.dump(self.caterers, f)


    def create_management_buttons(self):
        tk.Button(self.root, text="Manage Employees", command=self.manage_employees).pack()
        tk.Button(self.root, text="Manage Events", command=self.manage_events).pack()
        tk.Button(self.root, text="Manage Clients", command=self.manage_clients).pack()
        tk.Button(self.root, text="Manage Guests", command=self.manage_guests).pack()
        tk.Button(self.root, text="Manage Suppliers", command=self.manage_suppliers).pack()
        tk.Button(self.root, text="Manage Venue", command=self.manage_venues).pack()
        tk.Button(self.root, text="Manage Caterer", command=self.manage_caterers).pack()

    def manage_employees(self):
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Manage Employees")

        labels = ["Employee ID", "Name", "Department", "Job Title", "Basic Salary", "Manager ID"]
        entries = {}
        for idx, label in enumerate(labels):
            tk.Label(employee_window, text=label + ":").grid(row=idx, column=0)
            entry = tk.Entry(employee_window)
            entry.grid(row=idx, column=1)
            entries[label] = entry



        add_button = tk.Button(employee_window, text="Add Employee",
                               command=lambda: self.add_employee(entries))
        add_button.grid(row=len(labels), column=0)

        display_button = tk.Button(employee_window, text="Display Employee",
                                   command=lambda: self.display_employee(entries["Employee ID"].get()))
        display_button.grid(row=len(labels), column=1)

        delete_button = tk.Button(employee_window, text="Delete Employee",
                                  command=lambda: self.delete_employee(entries["Employee ID"].get()))
        delete_button.grid(row=len(labels) + 1, column=0, columnspan=2)

    def add_employee(self, entries):
        try:
            emp_id = int(entries["Employee ID"].get())
            name = entries["Name"].get()
            department = entries["Department"].get()
            jobTitle = entries["Job Title"].get()
            basicSalary = float(entries["Basic Salary"].get())
            managerID = int(entries["Manager ID"].get())

            if emp_id in self.employees:
                messagebox.showerror("Error", "Employee with ID already exists.")
            else:
                new_employee = Employee(emp_id, name, department, jobTitle, basicSalary, managerID)
                self.employees[emp_id] = new_employee
                self.save_data()
                messagebox.showinfo("Success", "Employee added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def display_employee(self, emp_id_str):
        try:
            emp_id = int(emp_id_str)
            if emp_id in self.employees:
                employee = self.employees[emp_id]
                details = employee.get_details()
                messagebox.showinfo("Employee Details", details)
            else:
                messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Employee ID must be an integer")

    def delete_employee(self, emp_id_str):
        try:
            emp_id = int(emp_id_str)
            if emp_id in self.employees:
                del self.employees[emp_id]
                self.save_data()
                messagebox.showinfo("Success", "Employee deleted successfully.")
            else:
                messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Employee ID must be an integer")



    def manage_events(self):
        event_window = tk.Toplevel(self.root)
        event_window.title("Manage Events")

        labels = ["Event ID", "Type", "Theme", "Date (YYYY-MM-DD)", "Time (HH:MM)", "Duration (hours)",
                  "Venue Address", "Client ID", "Guest IDs (comma-separated)", "Supplier IDs (comma-separated)", "Invoice"]
        entries = {}
        for idx, label in enumerate(labels):
            tk.Label(event_window, text=label+":").grid(row=idx, column=0)
            entry = tk.Entry(event_window)
            entry.grid(row=idx, column=1)
            entries[label] = entry

        add_event1 = tk.Button(event_window, text="Add Event", command=lambda: self.add_event(entries))
        add_event1.grid(row=len(labels), column=0)
        tk.Button(event_window, text="Display Event", command=lambda: self.display_event(entries["Event ID"].get())).grid(row=len(labels), column=1)
        tk.Button(event_window, text="Delete Event", command=lambda: self.delete_event(entries["Event ID"].get())).grid(row=len(labels)+1, column=0, columnspan=2)

    def add_event(self, entries):
        try:
            event_id = int(entries["Event ID"].get())
            type = entries["Type"].get()
            theme = entries["Theme"].get()
            date = entries["Date (YYYY-MM-DD)"].get()
            time = entries["Time (HH:MM)"].get()
            duration = float(entries["Duration (hours)"].get())
            venue_address = entries["Venue Address"].get()
            client_id = int(entries["Client ID"].get())

            # Convert guest IDs from comma-separated string to list of integers
            guest_ids = [int(g.strip()) for g in entries["Guest IDs (comma-separated)"].get().split(',') if
                         g.strip().isdigit()]
            # Convert supplier IDs from comma-separated string to list of integers
            supplier_ids = [int(s.strip()) for s in entries["Supplier IDs (comma-separated)"].get().split(',') if
                            s.strip().isdigit()]

            invoice = entries["Invoice"].get()

            if event_id in self.events:
                messagebox.showerror("Error", "Event with ID already exists.")
            else:
                # Create a new Event instance
                new_event = Event(event_id, type, theme, date, time, duration, venue_address, client_id, guest_ids,
                                  supplier_ids, invoice)
                # Add the new event to the events dictionary
                self.events[event_id] = new_event
                # Save data to file
                self.save_data()
                messagebox.showinfo("Success", "Event added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def display_event(self, event_id_str):
        try:
            event_id = int(event_id_str)
            if event_id in self.events:
                event = self.events[event_id]
                details = event.get_details()
                messagebox.showinfo("Event Details", details)
            else:
                messagebox.showerror("Error", "Event not found.")
        except ValueError:
            messagebox.showerror("Error", "Event ID must be an integer")

    def delete_event(self, event_id_str):
        try:
            event_id = int(event_id_str)
            if event_id in self.events:
                del self.events[event_id]
                self.save_data()
                messagebox.showinfo("Success", "Event deleted successfully.")
            else:
                messagebox.showerror("Error", "Event not found.")
        except ValueError:
            messagebox.showerror("Error", "Event ID must be an integer")

    def manage_clients(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Manage Clients")

        labels = ["Client ID", "Name", "Address", "Contact Details", "Budget"]
        entries = {}
        for idx, label in enumerate(labels):
            tk.Label(client_window, text=label + ":").grid(row=idx, column=0)
            entry = tk.Entry(client_window)
            entry.grid(row=idx, column=1)
            entries[label] = entry

        tk.Button(client_window, text="Add Client",
                  command=lambda: self.add_client(entries)).grid(row=len(labels), column=0)
        tk.Button(client_window, text="Display Client",
                  command=lambda: self.display_client(entries["Client ID"].get())).grid(row=len(labels), column=1)
        tk.Button(client_window, text="Delete Client",
                  command=lambda: self.delete_client(entries["Client ID"].get())).grid(row=len(labels) + 1, column=0,
                                                                                       columnspan=2)

    def add_client(self, entries):
        try:
            client_id = int(entries["Client ID"].get())
            name = entries["Name"].get()
            address = entries["Address"].get()
            contact_details = entries["Contact Details"].get()
            budget = float(entries["Budget"].get())

            if client_id in self.clients:
                messagebox.showerror("Error", "Client with ID already exists.")
            else:
                new_client = Client(client_id, name, address, contact_details, budget)
                self.clients[client_id] = new_client
                self.save_data()
                messagebox.showinfo("Success", "Client added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def display_client(self, client_id_str):
        try:
            client_id = int(client_id_str)
            if client_id in self.clients:
                client = self.clients[client_id]
                details = client.get_details()
                messagebox.showinfo("Client Details", details)
            else:
                messagebox.showerror("Error", "Client not found.")
        except ValueError:
            messagebox.showerror("Error", "Client ID must be an integer")

    def delete_client(self, client_id_str):
        try:
            client_id = int(client_id_str)
            if client_id in self.clients:
                del self.clients[client_id]
                self.save_data()
                messagebox.showinfo("Success", "Client deleted successfully.")
            else:
                messagebox.showerror("Error", "Client not found.")
        except ValueError:
            messagebox.showerror("Error", "Client ID must be an integer")

    def manage_guests(self):
        guest_window = tk.Toplevel(self.root)
        guest_window.title("Manage Guests")

        labels = ["Guest ID", "Name", "Address", "Contact Details"]
        entries = {}
        for idx, label in enumerate(labels):
            tk.Label(guest_window, text=label + ":").grid(row=idx, column=0)
            entry = tk.Entry(guest_window)
            entry.grid(row=idx, column=1)
            entries[label] = entry

        tk.Button(guest_window, text="Add Guest",
                  command=lambda: self.add_guest(entries)).grid(row=len(labels), column=0)
        tk.Button(guest_window, text="Display Guest",
                  command=lambda: self.display_guest(entries["Guest ID"].get())).grid(row=len(labels), column=1)
        tk.Button(guest_window, text="Delete Guest",
                  command=lambda: self.delete_guest(entries["Guest ID"].get())).grid(row=len(labels) + 1, column=0,
                                                                                     columnspan=2)

    def add_guest(self, entries):
        try:
            guest_id = int(entries["Guest ID"].get())
            name = entries["Name"].get()
            address = entries["Address"].get()
            contact_details = entries["Contact Details"].get()

            if guest_id in self.guests:
                messagebox.showerror("Error", "Guest with ID already exists.")
            else:
                new_guest = Guest(guest_id, name, address, contact_details)
                self.guests[guest_id] = new_guest
                self.save_data()
                messagebox.showinfo("Success", "Guest added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def display_guest(self, guest_id_str):
        try:
            guest_id = int(guest_id_str)
            if guest_id in self.guests:
                guest = self.guests[guest_id]
                details = guest.get_details()
                messagebox.showinfo("Guest Details", details)
            else:
                messagebox.showerror("Error", "Guest not found.")
        except ValueError:
            messagebox.showerror("Error", "Guest ID must be an integer")

    def delete_guest(self, guest_id_str):
        try:
            guest_id = int(guest_id_str)
            if guest_id in self.guests:
                del self.guests[guest_id]
                self.save_data()
                messagebox.showinfo("Success", "Guest deleted successfully.")
            else:
                messagebox.showerror("Error", "Guest not found.")
        except ValueError:
            messagebox.showerror("Error", "Guest ID must be an integer")

    def manage_suppliers(self):
        supplier_window = tk.Toplevel(self.root)
        supplier_window.title("Manage Suppliers")

        labels = ["Supplier ID", "Name", "Service", "Contact Details"]
        entries = {}
        for idx, label in enumerate(labels):
            tk.Label(supplier_window, text=label + ":").grid(row=idx, column=0)
            entry = tk.Entry(supplier_window)
            entry.grid(row=idx, column=1)
            entries[label] = entry

        tk.Button(supplier_window, text="Add Supplier",
                  command=lambda: self.add_supplier(entries)).grid(row=len(labels), column=0)
        tk.Button(supplier_window, text="Display Supplier",
                  command=lambda: self.display_supplier(entries["Supplier ID"].get())).grid(row=len(labels), column=1)
        tk.Button(supplier_window, text="Delete Supplier",
                  command=lambda: self.delete_supplier(entries["Supplier ID"].get())).grid(row=len(labels) + 1,
                                                                                           column=0, columnspan=2)

    def add_supplier(self, entries):
        try:
            supplier_id = int(entries["Supplier ID"].get())
            name = entries["Name"].get()
            service = entries["Service"].get()
            contact_details = entries["Contact Details"].get()

            if supplier_id in self.suppliers:
                messagebox.showerror("Error", "Supplier with ID already exists.")
            else:
                new_supplier = Supplier(supplier_id, name, service, contact_details)
                self.suppliers[supplier_id] = new_supplier
                self.save_data()
                messagebox.showinfo("Success", "Supplier added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def display_supplier(self, supplier_id_str):
        try:
            supplier_id = int(supplier_id_str)
            if supplier_id in self.suppliers:
                supplier = self.suppliers[supplier_id]
                details = supplier.get_details()
                messagebox.showinfo("Supplier Details", details)
            else:
                messagebox.showerror("Error", "Supplier not found.")
        except ValueError:
            messagebox.showerror("Error", "Supplier ID must be an integer")

    def delete_supplier(self, supplier_id_str):
        try:
            supplier_id = int(supplier_id_str)
            if supplier_id in self.suppliers:
                del self.suppliers[supplier_id]
                self.save_data()
                messagebox.showinfo("Success", "Supplier deleted successfully.")
            else:
                messagebox.showerror("Error", "Supplier not found.")
        except ValueError:
            messagebox.showerror("Error", "Supplier ID must be an integer")

    def manage_venues(self):
        venue_window = tk.Toplevel(self.root)
        venue_window.title("Manage Venues")

        labels = ["Venue ID", "Name", "Address", "Contact", "Min Guests", "Max Guests"]
        entries = {}
        for idx, label in enumerate(labels):
            tk.Label(venue_window, text=label + ":").grid(row=idx, column=0)
            entry = tk.Entry(venue_window)
            entry.grid(row=idx, column=1)
            entries[label] = entry

        tk.Button(venue_window, text="Add Venue",
                  command=lambda: self.add_venue(entries)).grid(row=len(labels), column=0)
        tk.Button(venue_window, text="Display Venue",
                  command=lambda: self.display_venue(entries["Venue ID"].get())).grid(row=len(labels), column=1)
        tk.Button(venue_window, text="Delete Venue",
                  command=lambda: self.delete_venue(entries["Venue ID"].get())).grid(row=len(labels) + 1, column=0,
                                                                                     columnspan=2)

    def add_venue(self, entries):
        try:
            venue_id = int(entries["Venue ID"].get())
            name = entries["Name"].get()
            address = entries["Address"].get()
            contact = entries["Contact"].get()
            min_guests = int(entries["Min Guests"].get())
            max_guests = int(entries["Max Guests"].get())

            if venue_id in self.venues:
                messagebox.showerror("Error", "Venue with ID already exists.")
            else:
                new_venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
                self.venues[venue_id] = new_venue
                self.save_data()
                messagebox.showinfo("Success", "Venue added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def display_venue(self, venue_id_str):
        try:
            venue_id = int(venue_id_str)
            if venue_id in self.venues:
                venue = self.venues[venue_id]
                details = venue.get_details()
                messagebox.showinfo("Venue Details", details)
            else:
                messagebox.showerror("Error", "Venue not found.")
        except ValueError:
            messagebox.showerror("Error", "Venue ID must be an integer")

    def delete_venue(self, venue_id_str):
        try:
            venue_id = int(venue_id_str)
            if venue_id in self.venues:
                del self.venues[venue_id]
                self.save_data()
                messagebox.showinfo("Success", "Venue deleted successfully.")
            else:
                messagebox.showerror("Error", "Venue not found.")
        except ValueError:
            messagebox.showerror("Error", "Venue ID must be an integer")

    def manage_caterers(self):
        caterer_window = tk.Toplevel(self.root)
        caterer_window.title("Manage Caterers")

        labels = ["Caterer ID", "Name", "Address", "Contact Details", "Menu", "Min Guests", "Max Guests"]
        entries = {}
        for idx, label in enumerate(labels):
            tk.Label(caterer_window, text=label + ":").grid(row=idx, column=0)
            entry = tk.Entry(caterer_window)
            entry.grid(row=idx, column=1)
            entries[label] = entry

        tk.Button(caterer_window, text="Add Caterer",
                  command=lambda: self.add_caterer(entries)).grid(row=len(labels), column=0)
        tk.Button(caterer_window, text="Display Caterer",
                  command=lambda: self.display_caterer(entries["Caterer ID"].get())).grid(row=len(labels), column=1)
        tk.Button(caterer_window, text="Delete Caterer",
                  command=lambda: self.delete_caterer(entries["Caterer ID"].get())).grid(row=len(labels) + 1, column=0,
                                                                                         columnspan=2)

    def add_caterer(self, entries):
        try:
            caterer_id = int(entries["Caterer ID"].get())
            name = entries["Name"].get()
            address = entries["Address"].get()
            contact_details = entries["Contact Details"].get()
            menu = entries["Menu"].get()
            min_guests = int(entries["Min Guests"].get())
            max_guests = int(entries["Max Guests"].get())

            if caterer_id in self.caterers:
                messagebox.showerror("Error", "Caterer with ID already exists.")
            else:
                new_caterer = Caterer(caterer_id, name, address, contact_details, menu, min_guests, max_guests)
                self.caterers[caterer_id] = new_caterer
                self.save_data()
                messagebox.showinfo("Success", "Caterer added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def display_caterer(self, caterer_id_str):
        try:
            caterer_id = int(caterer_id_str)
            if caterer_id in self.caterers:
                caterer = self.caterers[caterer_id]
                details = caterer.get_details()
                messagebox.showinfo("Caterer Details", details)
            else:
                messagebox.showerror("Error", "Caterer not found.")
        except ValueError:
            messagebox.showerror("Error", "Caterer ID must be an integer")

    def delete_caterer(self, caterer_id_str):
        try:
            caterer_id = int(caterer_id_str)
            if caterer_id in self.caterers:
                del self.caterers[caterer_id]
                self.save_data()
                messagebox.showinfo("Success", "Caterer deleted successfully.")
            else:
                messagebox.showerror("Error", "Caterer not found.")
        except ValueError:
            messagebox.showerror("Error", "Caterer ID must be an integer")


if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()
