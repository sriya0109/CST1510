"""
RECORD CHECK  -  my version
===========================

Name  : Sriya Raghavajosyula
Lane  :  AI 
Date  : 28-09-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)


print("=" * 34)

label = input("Enter a name, hostname, or IP: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

difference = second - first
percent = (first / second) * 100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  First:      {first:>10.2f}")
print(f"  Second:     {second:>10.2f}")
print(f"  Difference: {difference:>+10.2f}")
print(f"  Percent:    {percent:>10.2f}%")
print(f"  Numbers checked: {first:.2f} and {second:.2f}")

print("=" * 34)