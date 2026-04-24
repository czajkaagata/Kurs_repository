import os
import sys
from sqlalchemy import create_engine, inspect

# Dodajemy ścieżkę do modeli, żeby skrypt zadziałał
sys.path.append(os.path.join(os.getcwd(), "kurs_repository"))
from models import Base

# PODSTAW SWÓJ LINK Z OPCJI A
URL = 'postgresql://neondb_owner:npg_bvpQe2nNCS1V@ep-bold-thunder-am3vx9t9.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require'

engine = create_engine(URL)

def check_database():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    print(f"Tabele znalezione w bazie: {tables}")
    
    if 'products' in tables:
        print("✅ SUKCES: Tabela 'products' została poprawnie utworzona!")
    else:
        print("❌ BŁĄD: Nie znaleziono tabeli 'products'.")

if __name__ == "__main__":
    check_database()