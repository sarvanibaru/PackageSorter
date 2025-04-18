# PackageSorter

This project implements a Python function for sorting packages in a robotic automation factory, based on volume and mass rules.

## Function Overview

The function `sort(width, height, length, mass)` classifies packages into one of three stacks:

- **STANDARD**: Not bulky or heavy.
- **SPECIAL**: Either bulky or heavy.
- **REJECTED**: Both bulky and heavy.

### Criteria

- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³
  - Any dimension ≥ 150 cm

- A package is **heavy** if:
  - Mass ≥ 20 kg

## Running Tests

```bash
python test_sort_package.py
