import csv
import matplotlib.pyplot as plt
from .errors

class BankCSV:
    def __init__(self) -> None:
        pass

    # Read bank CSV and return a list of strings and numbers.
    def readBankCSV(self, fileName: str) -> list:
        try:
            with open(f"./csv/{fileName}", "r") as csvFile:
                csvData = list(csv.reader(csvFile))
                
                return csvData
        except FileNotFoundError:
            print("File was not found, did you forget the .csv?")
    
    # Display CSV data and return nothing.
    def displayBankCSV(self, bankData: list, x: str, y: str) -> None:
        xValues, yValues = []

        if x in bankData[0] and y in bankData[0]:
            for list in bankData:
                xValues.append(list[bankData[0].index(x)])
                yValues.append(list[bankData[0].index(y)])
        else:
            r

        print(xValues)