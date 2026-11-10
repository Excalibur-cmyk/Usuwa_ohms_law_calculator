# Ohm's Law and Power Calculator
# Finds voltage, current, resistance or power from known values.
# My own twist: the program keeps a history of every calculation
# and prints it when the user quits.

# List that stores every calculation done in this session (my twist)
history = []


def get_number(prompt):
    """Keep asking until the user types a valid number, then return it as a float."""
    while True:
        text = input(prompt)
        try:
            return float(text)  # convert the text to a decimal number
        except ValueError:
            # Runs when the user types letters or leaves it empty
            print("  Invalid input. Please type a number, e.g. 12 or 4.7")


def calculate(choice):
    """Ask for the known values, do the maths and return (name, value, unit).
    Returns None if the calculation is not possible."""

    if choice == "1":
        # Voltage: V = I x R
        current = get_number("Enter current (A): ")
        resistance = get_number("Enter resistance (ohms): ")
        return ("Voltage", current * resistance, "V")

    elif choice == "2":
        # Current: I = V / R
        voltage = get_number("Enter voltage (V): ")
        resistance = get_number("Enter resistance (ohms): ")
        if resistance == 0:
            print("  Error: resistance cannot be zero (cannot divide by zero).")
            return None
        return ("Current", voltage / resistance, "A")

    elif choice == "3":
        # Resistance: R = V / I
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")
        if current == 0:
            print("  Error: current cannot be zero (cannot divide by zero).")
            return None
        return ("Resistance", voltage / current, "ohms")

    elif choice == "4":
        # Power: P = V x I
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")
        return ("Power", voltage * current, "W")

    else:
        print("  Please choose a number from 1 to 5.")
        return None


def main():
    """Show the menu again and again until the user chooses to quit."""
    print("=== Ohm's Law and Power Calculator ===")

    while True:  # the loop repeats until the user quits
        print("\nWhat do you want to find?")
        print("1. Voltage (V)")
        print("2. Current (A)")
        print("3. Resistance (ohms)")
        print("4. Power (W)")
        print("5. Quit")
        choice = input("Choose 1-5: ").strip()

        if choice == "5":
            break  # leave the loop

        result = calculate(choice)

        if result is not None:
            name, value, unit = result
            print(f"  Answer: {name} = {value:.2f} {unit}")
            history.append(f"{name} = {value:.2f} {unit}")  # save to history

    # Show the history of this session before closing (my twist)
    print("\n--- Your calculations this session ---")
    if len(history) == 0:
        print("No calculations were done.")
    else:
        for number, item in enumerate(history, start=1):
            print(f"{number}. {item}")
    print("Goodbye!")


# Run the program only when this file is run directly
if __name__ == "__main__":
    main()
