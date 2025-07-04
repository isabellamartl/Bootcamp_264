import pandas as pd
df = pd.read_csv("cinema.csv")
# print(df)
print(df ['Age'])#Para imprimir las columnas que quiero, sin recorrer c/u de ellas
columnas_a_imprimir = ['Ticket_ID','Age','Ticket_Price']#Nueva variable con columnas a imprimir
df_selec =df[columnas_a_imprimir]#Son los datos seleccionados
print(df_selec)
