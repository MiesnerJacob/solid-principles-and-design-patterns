from abc import ABC, abstractmethod
from typing import List, Dict, Any
import csv
import json
import xml.etree.ElementTree as ET

class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass


class CSVParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data        
        

class JSONParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
        return data
        

class XMLParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for child in root:
            data.append(child.attrib)
        return data
        

class FileReader:
    def __init__(self, file_parser: FileParser):
        self.file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        return self.file_parser.parse_file(file_path)

if __name__ == "__main__":
    csv_reader = FileReader(CSVParser())
    csv_data = csv_reader.read_file("data/sample.csv")
    print("CSV Data:")
    print(csv_data)
    print("\n")

    json_reader = FileReader(JSONParser())
    json_data = json_reader.read_file("data/sample.json")
    print("JSON Data:")
    print(json_data)
    print("\n")

    xml_reader = FileReader(XMLParser())
    xml_data = xml_reader.read_file("data/sample.xml")
    print("XML Data:")
    print(xml_data)
