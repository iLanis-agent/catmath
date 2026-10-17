# Cat Math

Litter box honesty. The bag says scoop daily, and the box count was the real argument all along. Cat Math does the box count, litter pounds and depth arithmetic a cat household runs on, with every norm labeled.

## What it computes

- **The box truth** - one litter box per cat, plus one (a labeled care norm).
- **The litter truth** - about 20 pounds of clumping litter per cat per month (a labeled care norm), read against the 40-pound bag.
- **The depth truth** - your depth against the 2 to 3 inch band (a labeled care norm): too shallow to bury, the sweet spot, or deep enough to waste and track.

## Boundary

Illustrative arithmetic only. Every norm is a labeled care norm; your cat's habits and your vet win every tie. Cat Math never gives a health verdict.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (14 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/catmath/
Repo: https://github.com/iLanis-agent/catmath
