import pandas as pd
import csv
import matplotlib.pyplot as plt

class BankCSV:
    def __init__(self) -> None:
        pass

    # Read bank CSV and return a list of strings and numbers.
    def readBankCSV(self, fileName: str) -> None:
        csvData = []

        with open(f"./csv/{fileName}", "r") as csvFile:
            csvData = list(csv.reader(csvFile))
        return csvData
    
    # Display CSV data and return nothing.
    def displayBankCSV(self, bankData: list, x: str, y: str) -> None: 
        df = pd.DataFrame(bankData)
        plt.plot(df[x], df[y])
        plt.show()
    
    # Export CSV data if somehow stuff got changed.
    def exportBankCSV(self):
        raise NotImplementedError()

def main() -> None:
    bankCSV = BankCSV()
    bankData = bankCSV.readBankCSV("bankinfo.CSV")
    bankCSV.displayBankCSV(bankData, 1, 5)

if __name__ == "__main__":
    main()