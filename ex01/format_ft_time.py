import time
import datetime

"""
Get current time in seconds since January 1, 1970
"""
current_time = time.time()

"""
Get the current date
"""
current_date = datetime.date.today()

"""
Formatting the current time to display
with comma separation and 4 decimal places
"""
formatted_seconds = f"{current_time:,.4f}"

"""
Formatting the current time to display in
scientific notation with 2 decimal places.
"""
scientific_notation = f"{current_time:.2e}"

"""
Print the formatted results
"""
print(f"Seconds since January 1, 1970: {formatted_seconds} \
or {scientific_notation} in scientific notation")
print(f"{current_date.strftime('%b %d %Y')}")
