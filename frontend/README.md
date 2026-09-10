# Angular Frontend

The client dashboard is an Angular standalone application. It displays the client directory, filters the already loaded list by name, email, or phone number, and looks up individual clients through the FastAPI backend.

The dashboard uses Angular signals for local UI state, including client data, loading and error states, search input, and ID lookup results. Its filtered directory is derived with a computed signal, so it updates automatically as data or the search term changes.

## Prerequisites

- Node.js 20.19 or later
- npm
- The API running at `http://localhost:8000`

## Development

From this directory, install dependencies and start the application:

```powershell
npm install
npm start
```

The dashboard is available at `http://localhost:4200`. The development server proxies `/api` requests to `http://localhost:8000`; no client-side API URL change is needed for local development.

## Commands

```powershell
npm start       # Start the Angular development server
npm run build   # Create a production build in dist/
```

## Structure

- `src/app/app.ts` - Dashboard component and user interactions
- `src/app/client.service.ts` - API requests to the client endpoints
- `src/app/client.ts` - Client API data type
- `proxy.conf.json` - Local development API proxy
