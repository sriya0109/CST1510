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

import pandas as pd
import matplotlib.pyplot as plt

# ====================================================================
df = pd.read_csv("servers.csv")


# ====================================================================
# PROCESS

# Add percent column
df["percent"] = (df["used"] / df["total"]) * 100

# Add status column using lambda
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100
    else "WARNING" if x >= 90
    else "OK"
)


# ====================================================================
# OUTPUT

# Print the full DataFrame
print(df)

# Filter and print rows that are not OK
print(df[df["status"] != "OK"])

# Group by status and count servers
print(df.groupby("status").size())

# Save full DataFrame to a new CSV
df.to_csv("servers_final.csv", index=False)

# Count servers per status
status_counts = df["status"].value_counts()

# Apply ggplot style
plt.style.use("ggplot")

# Create bar chart
status_counts.plot(kind="bar")

plt.title("Number of Servers per Status")
plt.xlabel("Status")
plt.ylabel("Number of Servers")

plt.tight_layout()
plt.savefig("status_chart.png")
plt.show()

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
