from datetime import datetime, timezone, timedelta

# naive
naive = datetime.now()
print("Naive DateTime:", naive)

# UTC aware
UTC = datetime.now(timezone.utc)
print("UTC DateTime", UTC)

# Creating a datetime with JST (Japan) TimeZone
jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'EST'))
print("In JST::", jst_dateTime)