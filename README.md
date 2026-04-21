# Poincaré Recurrence (Urn Game)

This repository demonstrates the intuition behind the **Poincaré recurrence idea** using a simple two-urn random process.

## Concept

Start with two urns:

- **Urn A** contains `n` numbered elements.
- **Urn B** starts empty.

After random initialization, one random element is selected repeatedly and moved between urns depending on where it currently exists. The process stops when Urn B becomes empty again (a recurrence to the initial-style state), and the step count is reported.

## Repository contents

- `Poincare Recurrence.cpp` — C++ implementation.
- `Poincare Recurrence.py` — Python script printing a table of steps/time for increasing `n`.
- `NewPCareRecur.py` — Python interactive variant.

## Run in VSCode

This repo includes VSCode tasks and launch configurations in `.vscode/`.

### Tasks (`Terminal` → `Run Task`)

- `C++: Run Poincare Recurrence`
- `Python: Run simulation table`
- `Python: Run interactive game`

### Debug/Run (`Run and Debug` panel)

- `C++: Launch Poincare Recurrence`
- `Python: Simulation table`
- `Python: Interactive game`

## Run from terminal

From repository root:

```bash
g++ -std=c++17 -O2 -Wall -Wextra -pedantic "Poincare Recurrence.cpp" -o poincare_recurrence
./poincare_recurrence
```

```bash
python3 "Poincare Recurrence.py"
python3 "NewPCareRecur.py"
```

## Notes

- Large input sizes can take a long time due to random transitions.
- Results vary run-to-run because the process is stochastic.
