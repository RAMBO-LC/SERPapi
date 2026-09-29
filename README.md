PhotoCheck
Detect reused rental / PG listing photos before you pay a deposit.
PhotoCheck checks whether a listing photo has appeared on other listings, in other cities, or in older posts — using SerpApi’s Google Lens engine.
How it works

Submit a photo — upload a file or paste an image URL. Optionally include the city the listing claims to be in.
Find matches — the backend calls SerpApi Google Lens to discover every other page on the web using that same image.
Extract features — raw matches are turned into structured signals: number of matches, distinct sites, cities that appear, and whether the claimed city lines up.
Score the result — a scoring layer produces a clear verdict (likely reused / no strong signal), a confidence score, and plain-English reasoning. Ships with a transparent heuristic scorer by default; can be swapped for a TypeSafe/Jev structured-decision model (see backend/scorer.py).
Review the evidence — the frontend shows the verdict plus every matching source.

Setup
Bashcd backend
cp .env.example .env        # paste in your SerpApi key
pip install -r requirements.txt
uvicorn main:app --reload
Then open frontend/index.html in a browser, or serve it with:
Bashcd frontend && python -m http.server
Important: public image URLs for the demo
SerpApi’s Lens engine must fetch your image from a public URL. Localhost is not reachable. For a hackathon demo, pick one of:

Run the backend through a tunnel (ngrok http 8000) and set PUBLIC_BASE_URL in .env to the ngrok URL
Deploy the backend somewhere public (Render, Railway, Fly.io free tiers work same-day)
Skip file upload and paste a public image URL directly (e.g. from a real listing site) — no tunnel needed

Project structure
textbackend/
  main.py           FastAPI app — /api/analyze endpoint
  lens_client.py    SerpApi Google Lens wrapper
  scorer.py         Feature extraction + heuristic / Jev scoring
  requirements.txt
  .env.example
frontend/
  index.html        Single-file UI, no build step
AGENT_BUILD_INSTRUCTIONS.md   Full spec for handing this to a coding agent
Known v1 limitations
These are intentional so a working demo ships quickly:

Heuristic scorer only — Jev integration is stubbed, not live (see scorer.py)
No Maps-based geo cross-check yet (planned Stage 4; not required for v1)
Uploaded images are stored unauthenticated and unencrypted on disk with no cleanup job — fine for a demo, not for production
City matching uses a short hardcoded list of major Indian cities, not a real gazetteer or NER model


Copy-paste ready for your repo. Want a shorter version for the GitHub “About” blurb or a badges section at the top?i want some icons etc and beautifyHere’s a more polished README with icons, badges, and clearer visual hierarchy:

🔍 PhotoCheck
Detect reused rental / PG listing photos before you pay a deposit.



 [blocked]
PhotoCheck checks whether a listing photo has appeared on other listings, in other cities, or in older posts — using SerpApi’s Google Lens engine — so you can spot recycled images before handing over a deposit.

✨ How it works





























StepWhat happens1. SubmitUpload a listing photo or paste an image URL. Optionally add the city the listing claims to be in.2. SearchBackend calls SerpApi Google Lens and finds every other page on the web using that same image.3. ExtractRaw matches become structured features: match count, distinct sites, cities that appear, city consistency.4. ScoreA scoring layer returns a verdict (likely reused / no strong signal), confidence, and plain-English reasoning. Default: transparent heuristic. Optional: TypeSafe/Jev model (see backend/scorer.py).5. ReviewFrontend shows the verdict plus every matching source as evidence.

🚀 Setup
Bashcd backend
cp .env.example .env        # paste your SerpApi key
pip install -r requirements.txt
uvicorn main:app --reload
Open frontend/index.html in a browser, or serve it:
Bashcd frontend && python -m http.server
⚠️ Public image URLs (required for demo)
SerpApi’s Lens engine must fetch the image from a public URL. Localhost is not reachable. For a hackathon demo, use one of:

Tunnel — ngrok http 8000, then set PUBLIC_BASE_URL in .env to the ngrok URL
Deploy — Render, Railway, or Fly.io free tiers work same-day
Public URL only — paste an image URL from a real listing site (no tunnel needed)


📁 Project structure
textbackend/
  main.py           # FastAPI app — /api/analyze endpoint
  lens_client.py    # SerpApi Google Lens wrapper
  scorer.py         # Feature extraction + heuristic / Jev scoring
  requirements.txt
  .env.example
frontend/
  index.html        # Single-file UI, no build step
AGENT_BUILD_INSTRUCTIONS.md   # Full spec for a coding agent

📌 Known v1 limitations
Built to ship a working demo quickly:

🧮 Heuristic scorer only — Jev integration is stubbed, not live (scorer.py)
🗺️ No Maps geo cross-check yet — planned Stage 4; not required for v1
💾 Uploads stored on disk — unauthenticated, unencrypted, no cleanup (demo only)
🏙️ City matching — short hardcoded list of major Indian cities (not a full gazetteer/NER)


🛠️ Tech stack

Backend: FastAPI · Python
Image search: SerpApi Google Lens
Frontend: Single-file HTML (no build step)
Scoring: Heuristic (default) · TypeSafe/Jev
