# Descartes Labs mobility index plotting script

## Example usage:

	python plot-mobility.py --location "Texas" "California" "Florida" "New York" "New Jersey" "New Mexico" "Washington" --category "state" --weekends --input_filename ../DL-us-mobility.ndjson

	python plot-mobility.py --location "alameda" "los angeles" "orange" "san francisco" "san diego" --category "county" --county_state "california" --start_date "2020-03-08" --end_date "2020-03-15" --input_filename ../DL-us-mobility.ndjson

	python plot-mobility.py --location "colorado" --category "rank" --input_filename ../DL-us-mobility.ndjson --output_filename "colorado_ranked-counties"


## User specifications:

### Arguments:

`--location` : A list of administrative units to plot. Can be a list of counties, states, or mixture of both. Case insensitive. Default is a list of six states: California, Texas, New York, Illinois, Washington, and Florida.

`--category`: Type of administrative units. Options are "state", "county", "both", or "rank". "rank" is available if a state is specified as the location and will choose the counties with the highest mobility index in the state. Default is state.

`--weekend`: Option to include data from weekends (`--weekends`) or to exclude data from weekends (`--skip_weekends`). Defaults to exclude weekend data.

`--start_date`: Start date for daily mobility indices. Defaults to "2020-03-02", which is the earliest date available to retreive data.

`--end_date`: End date for daily mobility indices. Defaults to the most recent date that data is available.

`--input_filename`: Advanced option to specify a data file generated on a specific day. The default corresponds to the DL-us-mobility.ndjson in the DL-COVID-19 repo.

`--output_filename`: Option to specify output filename for plot. Appends user specification to "DL_mobility-index_". The default is "DL_mobility-index_{CURRENT DATE}.png"


## Notes:

- The "rank" choice in the "category" flag returns the ten top-ranked counties for the specified state. Note that if you choose more than one state when using "rank," the top ten counties will be returned regardless of state.

- If your locations are counties, be sure to specify the state to which each county belongs to ensure you're getting the expected data (e.g. Orange County, FL vs Orange County, CA). If you list multiple counties from the same state, just specify the state once. If listing counties from multiple states, please list the states in the same order that their corresponding counties are listed (e.g. if your counties are Orange, Washington, and Santa Cruz, and you want data from Florida, Georgia, and Arizona, respectively, order your inputs as follows:

	`python plot-mobility.py --location "orange" "washington" "santa cruz" --category county --county_state "florida" "georgia" "arizona" --input_filename ../DL-us-mobility.ndjson`

- Also, for counties where there might be confusion between a state and a county (e.g. Washington State vs. many different states with a Washington County), it's best practice to specify the word "county" when calling the script:

	`python plot-mobility.py --location "Denver county" "santa fe county" "santa barbara county" "new york" --category both --county_state "colorado" "new mexico" "california" "new york" --input_filename ../DL-us-mobility.ndjson`

	or

	`python plot-mobility.py --location "california" "los angeles county" "new york" "new york county" --category both --county_state "california" "california" "new york" "new york" --input_filename ../DL-us-mobility.ndjson`

- If you choose to use the `--start_date` and `--end_date` flags, the date should be in ISO standard format (e.g YYYY-MM-DD ).

- Plots become difficult to interpret if you compare too many AOIs. For that reason, we recommend limiting your comparisons to less than 20.


## Dependencies

We use [Poetry](https://python-poetry.org/) to manage dependencies. After [installing Poetry](https://python-poetry.org/docs/#installation) and cloning this repository, just run `poetry install && poetry shell` from within the repo. Poetry will create a virtual environment, install the necessary dependencies, and launch a sub-shell within that virtual environment. Then you can run the scripts as described above.
