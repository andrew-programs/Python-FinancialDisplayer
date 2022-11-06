from FinancialDisplayer import BankCSV

def main(fileName: str):
    bankStatementReader = BankCSV()
    bankData = bankStatementReader.readBankCSV(fileName)

    bankStatementReader.displayBankCSV(bankData, "Posting Date", "Amount")

if __name__ == "__main__":
    userInput = input("CSV file name > ")
    
    main(userInput)