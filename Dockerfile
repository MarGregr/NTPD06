FROM python:3.10-slim

#Ustawiawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

#Kopiowanie pliku z wymaganiami i instalujemy biblioteki
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Kopiowanie reszty plików projektu
COPY . .
