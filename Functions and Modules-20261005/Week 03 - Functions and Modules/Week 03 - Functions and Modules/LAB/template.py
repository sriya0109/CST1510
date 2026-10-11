"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent):
    """Return a status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = value - limit
    percent = value / limit * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"{'Value:':<18}{value:>10.2f}")
    print(f"{'Limit:':<18}{limit:>10.2f}")
    print(f"{'Difference:':<18}{difference:>10.2f}")
    print(f"{'Percent:':<18}{percent:>9.2f}%")
    print(f"{'Status:':<18}{status:>10}")
    print("=" * 34)


# Input, process and output multiple records
over_limit_count = 0

while True:
    label = input("Enter a label (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"\nTotal records OVER LIMIT: {over_limit_count}")
