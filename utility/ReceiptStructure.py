# '''
#     Data structure to store decoded receipt details.
# '''

# from typing import Any


# class Name:
#     def __init__(self, name: str):
#         self.name = name

#     def __repr__(self):
#         return self.name
    
#     def __call__(self):
#         return "Name"

# class ABN:
#     def __init__(self, abn: str):
#         self.abn = abn

#     def __repr__(self):
#         return self.abn

# class Tele:
#     def __init__(self, tele: str):
#         self.tele = tele

#     def __repr__(self):
#         return self.tele
    
# class Company:
#     def __init__(self, name: Name, abn: ABN, tele: Tele):
#         self.name = name
#         self.abn = abn
#         self.tele = tele

#     def __repr__(self):
#         return {Name: self.name, ABN: self.name, Tele: self.tele}

# class Heading:
#     def __init__(self):
#         pass

# class Body:
#     def __init__(self):
#         pass

# class Foot:
#     def __init__(self):
#         pass

# class Receipt:
#     def __init__(self, heading: Heading, body: Body, foot: Foot):
#         pass


from typing import List, Dict

# Class representing an item in the receipt
class Item:
    def __init__(self, name: str, quantity: int, unit_price: float, total_price: float, other: str):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price
        self.other = other

    def __repr__(self) -> Dict[str, str]:
        return {
            "Name": self.name,
            "Quantity": str(self.quantity),
            "UnitPrice": f"{self.unit_price:.2f}",
            "TotalPrice": f"{self.total_price:.2f}",
            "Other": self.other
        }

# Class representing a collection of products
class Products:
    def __init__(self, items: List[Item]):
        self.items = items

    def __repr__(self) -> Dict[str, List[Dict[str, str]]]:
        return {
            "Items": [repr(item) for item in self.items]
        }

# Class representing the body of the receipt
class Body:
    def __init__(self, products: Products, gst: float, total_with_tax: float, total: float):
        self.products = products
        self.gst = gst
        self.total_with_tax = total_with_tax
        self.total = total

    def __repr__(self) -> Dict[str, Dict]:
        return {
            "Products": repr(self.products),
            "GST": f"{self.gst:.2f}",
            "TotalWithTax": f"{self.total_with_tax:.2f}",
            "Total": f"{self.total:.2f}"
        }

# Class representing a company
class Company:
    def __init__(self, name: str, address: str, abn: str, tele: str):
        self.name = name
        self.address = address
        self.abn = abn
        self.tele = tele

    def __repr__(self) -> Dict[str, str]:
        return {
            "Name": self.name,
            "Address": self.address,
            "ABN": self.abn,
            "Tele": self.tele
        }

# Class representing a customer
class Customer:
    def __init__(self, name: str, address: str, tele: str):
        self.name = name
        self.address = address
        self.tele = tele

    def __repr__(self) -> Dict[str, str]:
        return {
            "Name": self.name,
            "Address": self.address,
            "Tele": self.tele
        }

# Class representing the heading of the receipt
class Heading:
    def __init__(self, company: Company, customer: Customer):
        self.company = company
        self.customer = customer

    def __repr__(self) -> Dict[str, Dict[str, str]]:
        return {
            "Company": repr(self.company),
            "Customer": repr(self.customer)
        }

# Class representing the footer of the receipt
class Foot:
    def __init__(self, card_number: str):
        self.card_number = card_number

    def __repr__(self) -> Dict[str, str]:
        return {
            "CardNumber": self.card_number
        }

# Class representing the entire receipt
class Receipt:
    def __init__(self, heading: Heading, body: Body, foot: Foot):
        self.heading = heading
        self.body = body
        self.foot = foot

    def __repr__(self) -> Dict[str, Dict]:
        return {
            "Heading": repr(self.heading),
            "Body": repr(self.body),
            "Foot": repr(self.foot)
        }

# Example Usage
if __name__ == "__main__":
    # Define the company details
    company = Company(
        name="ABC Store",
        address="123 Main St, Cityville",
        abn="987654321",
        tele="123-456-7890"
    )

    # Define the customer details
    customer = Customer(
        name="John Doe",
        address="456 Elm St, Townsville",
        tele="098-765-4321"
    )

    # Define the products
    items = [
        Item(name="Widget", quantity=2, unit_price=10.00, total_price=20.00, other="N/A"),
        Item(name="Gadget", quantity=1, unit_price=15.00, total_price=15.00, other="N/A")
    ]
    products = Products(items=items)

    # Define the body of the receipt
    body = Body(
        products=products,
        gst=3.50,
        total_with_tax=38.50,
        total=35.00
    )

    # Define the footer
    foot = Foot(card_number="**** **** **** 1234")

    # Create the heading
    heading = Heading(company=company, customer=customer)

    # Create the complete receipt
    receipt = Receipt(heading=heading, body=body, foot=foot)

    # Print the receipt
    print(receipt)
