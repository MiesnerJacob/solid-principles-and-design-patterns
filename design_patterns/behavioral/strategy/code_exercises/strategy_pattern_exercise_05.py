from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
import json
import csv

class Contact:
    def __init__(self, full_name: str, email: str, phone_number: str, is_friend: bool):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_friend = is_friend

    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.phone_number} - {'(Friend)' if self.is_friend else ''}"
    

class FileReader(ABC):
    def __init__(self, file_name: str):
        self.file_name = file_name

    @abstractmethod
    def read(self) -> str:
        pass


class ContactsAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source

    @abstractmethod
    def get_contacts(self) -> List[Contact]:
        pass
    

class XMLContactsAdapter(ContactsAdapter):
    def get_contacts(self) -> List[Contact]:
        root = ET.fromstring(self.data_source.read())
        contacts = []
        for elem in root.iter():
            if elem.tag == "contact":
                full_name = elem.find("full_name").text
                email = elem.find("email").text
                phone_number = elem.find("phone_number").text
                is_friend = elem.find("is_friend").text
                contact = Contact(full_name, email, phone_number, is_friend)
                contacts.append(contact)
        return contacts
    

class JSONContactsAdapter(ContactsAdapter):
    def get_contacts(self) -> List[Contact]:
        data_dict = json.loads(self.data_source.read())
        contacts = []
        for contact_data in data_dict["contacts"]:
            full_name = contact_data["full_name"]
            email = contact_data["email"]
            phone_number = contact_data["phone_number"]
            is_friend = contact_data["is_friend"]
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)
        return contacts
    

class CSVContactsAdapter(ContactsAdapter):
    def get_contacts(self) -> List[Contact]:
        csv_data = self.data_source.read()
        contacts = []
        for row in csv_data[1:]:  # Skip header row
            full_name, email, phone_number, is_friend = row
            contact = Contact(full_name, email, phone_number, is_friend.lower() == 'true')
            contacts.append(contact)
        return contacts
    

class XMLReader(FileReader):
    def read(self) -> str:
        with open(self.file_name, "r") as f:
            return f.read()
        

class JSONReader(FileReader):
    def read(self) -> str:
        with open(self.file_name, "r") as f:
            return f.read()
        

class CSVReader(FileReader):
    def read(self) -> List[List[str]]:
        with open(self.file_name, "r") as f:
            return list(csv.reader(f))

class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, contact: Contact) -> str:
        pass


class DefaultDisplayStrategy(DisplayStrategy):
    def display(self, contact: Contact) -> str:
        return str(contact)


class FriendlyDisplayStrategy(DisplayStrategy):
    def display(self, contact: Contact) -> str:
        friend_status = "Friend" if contact.is_friend else "Not a friend"
        return f"{contact.full_name} - {friend_status}"


class ContactManager:
    def __init__(self, contacts_source: ContactsAdapter, display_strategy: DisplayStrategy = DefaultDisplayStrategy()):
        self.contacts_source = contacts_source
        self.display_strategy = display_strategy

    def set_display_strategy(self, display_strategy: DisplayStrategy):
        self.display_strategy = display_strategy

    def print_contact_data(self):
        contacts = self.contacts_source.get_contacts()
        for contact in contacts:
            print(self.display_strategy.display(contact))


if __name__ == "__main__":
    xml_reader = XMLReader("./data/contacts.xml")
    xml_adapter = XMLContactsAdapter(xml_reader)
    json_reader = JSONReader("./data/contacts.json")
    json_adapter = JSONContactsAdapter(json_reader)
    csv_reader = CSVReader("./data/contacts.csv")
    csv_adapter = CSVContactsAdapter(csv_reader)

    contact_manager = ContactManager(xml_adapter)
    print("XML Contacts (Default Display):")
    contact_manager.print_contact_data()

    contact_manager.set_display_strategy(FriendlyDisplayStrategy())
    print("\nXML Contacts (Friendly Display):")
    contact_manager.print_contact_data()

    contact_manager = ContactManager(json_adapter, FriendlyDisplayStrategy())
    print("\nJSON Contacts (Friendly Display):")
    contact_manager.print_contact_data()

    contact_manager = ContactManager(csv_adapter)
    print("\nCSV Contacts (Default Display):")
    contact_manager.print_contact_data()

    contact_manager.set_display_strategy(FriendlyDisplayStrategy())
    print("\nCSV Contacts (Friendly Display):")
    contact_manager.print_contact_data()