import pandas as pd
import csv

def main(fileName: str):
    with open(f'{fileName}', 'r') as csvFile:
        data = csv.reader(csvFile)
    
    df = pd.DataFrame(data)
    
    print(df)
if __name__ == "__main__":
