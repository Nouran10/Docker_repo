import argparse
import pandas as pd 

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading the dataset: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Load a dataset from a specified file path.")
    parser.add_argument("file_path", help="Path to the dataset file")

    args = parser.parse_args()
    file_path = args.file_path

    df = load_dataset(file_path) 
    if df is not None:
        print("Dataset loaded successfully.")

    from dpre import dpre
    dpre(df)

    from eda import eda
    eda(df)

    from vis import vis
    vis(df)

    from model import model
    model(df)

main()

