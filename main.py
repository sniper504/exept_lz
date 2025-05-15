from data_processing import DataProcessing 

def main():
    file_path = "var3.csv"
    processor = DataProcessing(file_path)
    processor.process()

if __name__ == "__main__":
    main() 