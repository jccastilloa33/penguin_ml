# Bucle principal
#while not pd.isnull(df['Recupero acumulado'].iloc[0]):
if INICIO == 0:
        TPI_SIN_R = 0
        TPI_CON_R = 0
        PROV = df['Stock Provisiones'].iloc[0]
        Perdida = df['Pérdida Acumulada Prox. 12 meses'].iloc[0]
        Recupero = df['Recupero acumulado'].iloc[0]
else:
    TPI_SIN_R = 0
    TPI_CON_R = 0
    PROV = df['Stock Provisiones'].iloc[0]
    Perdida = df['Pérdida Acumulada Prox. 12 meses'].iloc[0]
    Recupero = df['Recupero acumulado'].iloc[0]
    N = 12

# Bucle interior
while TPI_SIN_R <= 0:
    Perdida_1 = Perdida + df['CASTIGOS MENSUALES'].iloc[N + 1]
    Perdida = Perdida_1
    Recupero_1 = Recupero + df['RECUPEROS MENSUALES'].iloc[N + 1]
    Recupero = Recupero_1
    NETA = Perdida_1 - Recupero_1
    TPI_CON_R = (NETA / PROV) - 1
    TPI_SIN_R = Perdida_1 / PROV - 1
    N += 1

# Actualizar el valor en la columna correspondiente
#df['Meses Cobertura Sin Recupero'].iloc[0] = N - 1
df.loc[0, 'Meses Cobertura Sin Recupero'] = N - 1

if INICIO == 0:
    N = 12
    TPI_SIN_R = 0
    TPI_SIN_R = 0
    TPI_CON_R = 0
    PROV = df['Stock Provisiones'].iloc[0]
    Perdida = df['Pérdida Acumulada Prox. 12 meses'].iloc[0]
    Recupero = df['Recupero acumulado'].iloc[0]
else:
    N = 12
    TPI_SIN_R = 0
    TPI_CON_R = 0
    PROV = df['Stock Provisiones'].iloc[0]
    Perdida = df['Pérdida Acumulada Prox. 12 meses'].iloc[0]
    Recupero = df['Recupero acumulado'].iloc[0]

# Bucle interior
while TPI_CON_R <= 0:
    Perdida_1 = Perdida + df['CASTIGOS MENSUALES'].iloc[N + 1]
    Perdida = Perdida_1
    Recupero_1 = Recupero + df['RECUPEROS MENSUALES'].iloc[N + 1]
    Recupero = Recupero_1
    NETA = Perdida_1 - Recupero_1
    TPI_CON_R = (NETA / PROV) - 1
    TPI_SIN_R = Perdida_1 / PROV - 1
    N += 1

# Actualizar el valor en la columna correspondiente
#df['Meses Cobertura Con Recupero'].iloc[0] = N - 1
df.loc[0, 'Meses Cobertura Con Recupero'] = N - 1