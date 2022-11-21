# funcao que altera todas as colunas do tipo float para int usando a funcao .loc

def float_to_int(df):
    for col in df.columns:
        if df[col].dtype == 'float64':
            df.loc[:,col] = df[col].astype('int64')
    return df