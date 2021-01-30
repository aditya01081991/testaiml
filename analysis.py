import pandas as pd
import json
def analysistpt():
    df = pd.read_csv('final_data.csv')
    # df['Start_Date'] =  pd.to_datetime(df['Start_Date'], infer_datetime_format=True)
    df = df.sort_values('Vehicle State')
    df['Combination'] = df['Destination_short'] + ' ' + df['Vehicle State']
    df1 = df['Combination'].value_counts().to_frame()
    df1.reset_index(level = 0, inplace = True)
    df1.columns = ['Comb', 'Count']
    df1[['Source', 'Dest']] = df1.Comb.str.split(' ', expand = True)
    df2 = df[['Destination_short', 'Vehicle State','Start_Date' , 'Transporter', 'Size', 'Shipline']]
    return(json.dumps(df2.to_dict('records')).replace('\"',''))
