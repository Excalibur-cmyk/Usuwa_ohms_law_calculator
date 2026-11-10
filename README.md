# Ohm's Law and Power Calculator

## What it does
This program lets the user choose whether to find voltage, current, resistance or power. It asks for the known values, calculates the answer and shows it with units. It keeps running until the user chooses to quit.

## How to run it
Install Python 3, then run: python ohms_law.py

## Sample output
```
=== Ohm's Law and Power Calculator ===

What do you want to find?
1. Voltage (V)
2. Current (A)
3. Resistance (ohms)
4. Power (W)
5. Quit
Choose 1-5: 2
Enter voltage (V): 12
Enter resistance (ohms): 4
  Answer: Current = 3.00 A

Choose 1-5: 5

--- Your calculations this session ---
1. Current = 3.00 A
Goodbye!
```

## My own twist
The program saves every calculation in a history list and prints a summary of all of them when the user quits.

## What I learned
- How to use try/except so the program does not crash when someone types a letter instead of a number.
- How to stop a divide-by-zero error by checking the value before dividing.

## Author
USUWA FAVOUR, ND1 Mechatronics Engineering, YabaTech.
