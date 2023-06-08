# Diablo 4 Helltide Tracker

This Python script periodically checks the Diablo 4 Helltide report history from the [Diablo 4 Life API](https://diablo4.life/api/trackers/helltide/reportHistory). When it detects new reports, it prints them to the console.

## Features

- Retrieves the Helltide report history every 5 minutes.
- Converts the Unix timestamps in the report data to human-readable times.
- Prints new reports to the console, including the boss name, location, report time, spawn time, and the user who reported it.

## Usage

1. Install the required Python library:

    ```
    pip3 install -r requirements.txt
    ```

2. Run the script:

    ```
    python d4_helltide_tracker.py
    ```

3. The script will run indefinitely, checking for new reports every 5 minutes. To stop the script, press Ctrl+C.

## Notes

- The script uses the `requests` library to send HTTP requests to the API.
- The script uses the `time.sleep()` function to wait for 5 minutes between each check. You can adjust this delay as needed, but be aware that making requests too frequently may result in your IP being blocked by the API.
- The script prints new reports to the console. If you'd like to send notifications in a different way (such as by email or desktop notification), you'll need to modify the script accordingly.

## Disclaimer

This script is provided as-is, with no guarantees of functionality or correctness. Use it at your own risk. The author is not responsible for any consequences resulting from the use of this script.
