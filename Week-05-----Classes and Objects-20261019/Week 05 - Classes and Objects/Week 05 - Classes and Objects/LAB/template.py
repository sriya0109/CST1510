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

class Record:
    """This stored information about a record"""

    def __init__(self, label, value, limit):
        """Store the label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on value compared with the limit."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 95.0, 100.0),
    Record("R-003", 105.0, 100.0),
    Record("R-004", 45.0, 50.0),
]

over_limit_count=0 


for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Value:  {record.value}")
    print(f"  Limit:  {record.limit}")
    print(f"  Status: {record.status()}")

    if record.status() == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)

print()
print(f"Total records OVER LIMIT: {over_limit_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
