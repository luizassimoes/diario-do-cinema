from app import db
import pandas as pd
from datetime import datetime
from model.movies import Movies

# Código projetado para adicinar grandes quantidades de filmes diretamente no SQL via arquivo CSV

csv_file = pd.read_csv(r'C:\Users\Luiza Simoes\OneDrive - Qualidados Engenharia e Informatica\Documentos\Luiza\Flask\lu-e-thi\filmes.csv', sep=";", encoding='latin1')

for i in range(csv_file.shape[0]):
    movie = csv_file.iloc[i, 0]
    date = datetime.strptime(str(csv_file.iloc[i, 1]), '%d/%m/%Y') if pd.notna(csv_file.iloc[i, 1]) else None
    grade1 = float(csv_file.iloc[i, 2].replace(',', '.')) if pd.notna(csv_file.iloc[i, 2]) else None
    grade2 = float(csv_file.iloc[i, 3].replace(',', '.')) if pd.notna(csv_file.iloc[i, 3]) else None
    image = None
    avg = float(csv_file.iloc[i, 4].replace(',', '.')) if pd.notna(csv_file.iloc[i, 4]) else None
    sd = float(csv_file.iloc[i, 5].replace(',', '.')) if pd.notna(csv_file.iloc[i, 5]) else None

    new_movie = Movies(name=movie, date=date, grade1=grade1, grade2=grade2, image=image, avg=avg, sd=sd)
    db.session.add(new_movie)
db.session.commit()
print('---------------- Filmes adicionados com sucesso! ----------------')