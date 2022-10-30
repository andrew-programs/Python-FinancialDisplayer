from dataclasses import dataclass
import pandas as pd
import csv

@dataclass(frozen=True)
class BankCSV:
    # Read bank CSV and return a list of strings and numbers.
    def readBankCSV(self, fileName: str) -> list:
        with open(f"./csv/{fileName}", "r") as csvFile:
            csvReader = csv.reader(csvFile)
        return csvData
    
    # Display CSV data return nothing.
    def displayBankCSV(self, bankData, x: str="Posting Date", y: str="Amount", graphType: str="Line") -> None: 
        data = pd.read_csv()
        df.plot(x=x, y=y, kind=graphType)
    
    # Export CSV data if somehow stuff got changed.
    def exportBankCSV(self):
        raise NotImplementedError()

def main() -> None:
    bankCSV = BankCSV()
    bankData = bankCSV.readBankCSV("bankinfo.CSV")
    print(bankData)
    bankCSV.displayBankCSV(bankData)

if __name__ == "__main__":
    main()