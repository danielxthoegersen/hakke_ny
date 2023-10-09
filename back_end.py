import pandas as pd

def main():

    data = collect_data()
    print(data)

def collect_data():
    # Hent data og rens data
    df = pd.read_csv("database_dummy.csv")
    for col in df.select_dtypes(include=[object]).columns:
        df[col] = df[col].str.replace(r'\[', '', regex=True)
        df[col] = df[col].str.replace(r'\]', '', regex=True)
    return df


# def sort_by_total_score_function():

    
if __name__ == "__main__":
    main()