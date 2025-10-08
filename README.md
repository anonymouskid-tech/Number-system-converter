# Number Converter — Program Documentation

## Overview
Small desktop GUI application built with Kivy to convert numbers between Binary, Octal, Decimal, and Hexadecimal. Single-file implementation.

## Purpose
Provide a simple, colorized UI for quick base conversions and serve as a learning/refactorable example.

## Requirements (Windows)
- Python 3.8+
- Kivy (install via `pip install kivy`)
- Optional: Visual Studio Code for editing/debugging

## Installation & Run (Windows PowerShell)
1. Create & activate virtual environment:
   .venv\Scripts\Activate.ps1
2. Install dependencies:
   pip install kivy
3. Run the app:
   python c:\Users\ADIX.C\main.py

## Files
- c:\Users\ADIX.C\main.py — GUI and conversion logic (current single-file app)
- c:\Users\ADIX.C\Documents\process.md — this documentation

## UI Layout (high level)
1. Title bar (blue)
2. Input row (white) — TextInput for source number
3. Dropdowns (green) — "From" and "To" number systems (Spinner widgets)
4. Buttons (purple) — Convert and Clear
5. Output area (faded black) — readonly TextInput showing results/errors

## Conversion Logic
- Supported systems: Binary (base 2), Octal (8), Decimal (10), Hexadecimal (16)
- Mapping: `base_map = {"Decimal":10, "Binary":2, "Octal":8, "Hexadecimal":16}`
- Parse source: `decimal_val = int(value, base_map[from_sys])`
- Format target:
  - Decimal: `str(decimal_val)`
  - Binary: `bin(decimal_val)[2:]`
  - Hexadecimal: `hex(decimal_val)[2:].upper()`
  - Octal: `oct(decimal_val)[2:]`
- Errors caught and displayed in output box.

## Suggested Refactor (for testability)
Extract conversion to a pure function:
def convert_number(value: str, from_sys: str, to_sys: str) -> str

Benefits:
- Unit testing with pytest
- Simpler error handling & input validation
- Keeps UI code focused on presentation

## Example conversions
- "10" from Decimal to Binary -> "1010"
- "FF" from Hexadecimal to Decimal -> "255"

## Testing
- Add pytest tests for:
  - Valid conversions
  - Invalid input (raise ValueError or return explicit error)
  - Edge cases (negative numbers, zero, very large values)

## Troubleshooting
- Kivy install failures: check Python version and Kivy Windows docs (SDL2 dependencies).
- Input parsing errors: ensure correct digits for selected input base.
- UI rendering issues: run from terminal to view Kivy logs.

## Next steps / Improvements
- Move conversion logic to a module and add tests.
- Add input validation per base and informative error messages.
- Add copy-to-clipboard, conversion history, and keyboard shortcuts.

## Changelog
- v1.0 — Initial single-file implementation and documentation.
## Authors

This project was completed by the following team members:

- **Adrian Mwangi** - [@adchase521](https://github.com/adchase521)
- **Caren Koskei** 
- **Martin Nzioki** 
- **Cylvia Amdany** 
- **Antony Kariuki** 
