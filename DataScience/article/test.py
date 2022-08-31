import pyreadstat as prs
import pandas as pd
from sas7bdat import *

file_name = "Dicionario/input_PNS_2019.sas7bdat"
foo = SAS7BDAT(file_name)
my_df = foo.to_data_frame()
my_df = my_df.head()
my_df.to_csv('PNS_2019.csv', index=False)

# url = 'Dicionario/input_PNS_2019.sas'
# df = pd.read_sas(url)
# df.head()
# df.to_csv('PNS_2019.csv', index=False)

# df, meta = prs.read_sas7bdat('dicionario/input_PNS_2019.sas')
# df.head()
# df.to_csv('PNS_2019.csv', index=False)

