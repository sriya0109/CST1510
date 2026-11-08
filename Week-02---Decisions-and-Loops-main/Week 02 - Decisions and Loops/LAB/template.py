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

while True:

    label = input("Enter a name, hostname, or IP (or quit): ")

    if label == "quit":
        break

    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))


    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


    if status == "OVER LIMIT":
        over_limit_count += 1



    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Value:       {value:>10.2f}")
    print(f"  Limit:       {limit:>10.2f}")
    print(f"  Difference:  {difference:>+10.2f}")
    print(f"  Percent:     {percent:>10.2f}%")
    print(f"  Status:      {status}")

    print("=" * 34)


print()
print(f"Records OVER LIMIT: {over_limit_count}")


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)



print("=" * 34)



