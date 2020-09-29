import pandas as pd
def getContacts():
    data = pd.read_excel (r'/home/lino/Documents/Contacts.xlsx') 
    df = pd.DataFrame(data, columns= ['Nombre'])
    for i in df['Nombre']:
        print(i)
    return df['Nombre']