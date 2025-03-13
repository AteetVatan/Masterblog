"""Module to create, read and write JSON data"""
import json
import os
from .print_helper import PrintHelper


class JsonFileHelper:
    """Helper Class responsible for JSON file operations."""

    @staticmethod
    def read_data(file_path):
        """Method to read JSON data."""
        d = None
        try:
            with open(file_path, mode="r", encoding="utf-8") as data:
                d = json.load(data)
        except FileNotFoundError as f:
            PrintHelper.pr_error(f)
            raise f
        except IOError as e:
            PrintHelper.pr_error("I/O error occurred: ", os.strerror(e.errno))
            raise e
        return d

    @staticmethod
    def write_data(self, data, file_path):
        """Method to write JSON data to file"""
        try:
            if not file_path:
                file_path = self.file_path
            if data is None:
                data = {}
            with open(file_path, mode="w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as f:
            PrintHelper.pr_error(f)
        except IOError as e:
            PrintHelper.pr_error("I/O error occurred: ", os.strerror(e.errno))
