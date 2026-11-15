"""
RECORD CHECK  -  my version
===========================

Name  :Sriya Raghavajosyula
Lane  :  AI
Date  :14-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def parse_line(raw_line):
    """Cleans and parses the messy survey record into a dictionary."""

    parts = raw_line.strip().split(",")

    answers = {}

    survey_id = parts[0].strip().upper()
    answers["survey_id"] = survey_id

    for item in parts[1:]:

        if "=" not in item:
            raise ValueError("Invalid record: missing '=' in " + item.strip())

        key, value = item.split("=", 1)

        key = key.strip().lower()
        value = value.strip()

    
        if key in ("rating", "age"):
            answers[key] = int(value)

        else:
            answers[key] = value

    
    required_fields = ["survey_id", "rating", "age"]

    for field in required_fields:
        if field not in answers:
            raise ValueError("Missing required field: " + field)

    return answers


def status_of(answers):
    """Flags survey records with a rating below 3."""

    if answers["rating"] < 3:
        return "FLAGGED"

    else:
        return "OK"

raw_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "SURVEY_2027,rating=2,age=19",
    "  survey_2028 , RATING = 5 , AGE = 21 ",
    "Survey_2029, Rating=1, Age=25",
    "   SURVEY_2030 , rating = 3 , age = 18   ",
    "survey_2031, RATING=4, AGE=22",
    "  survey_2032 , Rating = 2 , AGE = 20  "
]
with open("survey_records.txt", "w") as file:

    for record in raw_records:
        file.write(record + "\n")


record_count = 0
flagged_count = 0

print("=" * 50)
print("       SURVEY RECORD PROCESSING SYSTEM")
print("=" * 50)

with open("survey_records.txt", "r") as file:

    for raw_record in file:

        
        if raw_record.strip():

            try:
                
                answers = parse_line(raw_record)

                
                status = status_of(answers)

                
                print("\nCleaned survey:", answers)
                print("Status:", status)
                print("-" * 50)

                record_count += 1

                if status == "FLAGGED":
                    flagged_count += 1

            except ValueError as error:
                print("Error:", error)

print("\n" + "=" * 50)
print("                SURVEY SUMMARY")
print("=" * 50)

print("Total records processed:", record_count)
print("Flagged records:", flagged_count)
print("OK records:", record_count - flagged_count)

print("=" * 50)


print("\nERROR HANDLING TEST")
print("-" * 50)

try:

    invalid_record = "Survey_2033, rating=unknown, age=20"

    parse_line(invalid_record)

except ValueError as error:

    print("Invalid record tested:", invalid_record)
    print("Error found:", error)
    print("The program successfully handled the invalid value.")

print("-" * 50)

