import requests
import time
from datetime import datetime

# Set the last report's timestamp to the current time
last_report_time = int(time.time() * 1000)  # Current time in milliseconds

while True:
    response = requests.get('https://diablo4.life/api/trackers/helltide/reportHistory')
    data = response.json()

    # Iterate through reports in reverse order, so that we process the most recent reports first
    for report in reversed(data['reports']):
        # Convert Unix timestamps to human-readable format
        report_time = datetime.fromtimestamp(report['reportTime'] / 1000.0)  # Timestamps are in milliseconds
        spawn_time = datetime.fromtimestamp(report['spawnTime'] / 1000.0)

        # If the report is newer than the last one we processed, print it
        if report['reportTime'] > last_report_time:
            print(f"New report: {report['name']} at {report['location']}, reported at {report_time} (spawned at {spawn_time}) - reported by: {report['user']['displayName']}")
            last_report_time = report['reportTime']

    # Sleep for 5 minutes (300 seconds) before checking again
    time.sleep(300)
