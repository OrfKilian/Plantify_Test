# Plantify Test Monorepo

Dieses Repository enthält nun zwei getrennte Projekte:

- **backend/** – Flask API mit allen Endpunkten
- **frontend/** – Vite/React Frontend

## Entwicklung starten

### Backend

```bash
cd backend/app/Plantify/smartplant_api
python app.py
```

Die Abhängigkeiten befinden sich in `backend/requirements.txt`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Die Vite-Konfiguration leitet Aufrufe auf `/api` im Development-Modus automatisch an die lokale Backend-URL weiter.

In Produktion wird die Basis-URL der API über `VITE_API_URL` aus der jeweiligen `.env` Datei gesteuert.
