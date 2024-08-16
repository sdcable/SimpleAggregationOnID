
def aggregatingRows(file_path, id_col, excel_output=True):
    """
        filepath (str): filepath to file
        id_col (str): Column of aggregating the rows
        excel_output (bool, optional): If you want to output the excel file or just return df. Defaults to True.
    """
    import pandas as pd
    df = pd.read_excel(file_path)
    
    result_df = pd.DataFrame()
    aggregated_data = df.groupby(id_col).sum().reset_index()

    for name in df[id_col].unique():
        person_data = df[df[id_col] == name]
        # Extract aggregated row for the current person
        aggregate_row = aggregated_data[aggregated_data[id_col] == name]
        # Append the original data and aggregated row
        result_df = pd.concat([result_df, person_data, aggregate_row])


    output_file_path = f'aggregated_data_of_{id_col}.xlsx'
    
    #Based on output, do this
    if excel_output:
        print(f"Aggregated data has been saved to {output_file_path}")
        result_df.to_excel(output_file_path, index=False)
    else:
        print(f"DataFrame returned")
        return result_df

    