# software-update-age-reporter

List applications by days since their last update and flag the ones past (or nearly past) the update policy, oldest first.

## How to run

```sh
python3 main.py apps.csv --max-days 90
```

## Example output

```
LegacyApp: OVERDUE (153 days since update)
Browser: OK (17 days since update)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
