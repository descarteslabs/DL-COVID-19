# Data for Mobility Changes in Response to COVID-19

[ [U.S. mobility Data (ndjson)](DL-us-mobility.ndjson) |
[U.S. mobility Data (csv)](DL-us-mobility-daterow.csv) |
[U.S. m50_index Data (alternate csv)](DL-us-m50_index.csv) 
]

[Descartes Labs](https://descarteslabs.com/) is releasing mobility
statistics (representing the distance a typical member of a given
population moves in a day) at the US admin1 (state) and admin2
(county) level.  A technical report describing the motivation behind
this work with methodology and definitions is available at
[descarteslabs.com/mobility-v097](https://www.descarteslabs.com/mobility-v097).
We intend to update the data in this repository regularly.

## Mobility Data

[NDJSON](https://github.com/ndjson/ndjson-spec) format data can be found in the
[DL-us-mobility.ndjson](DL-us-mobility.ndjson) file.

```json
{"cc": "US", "admin_level": 2, 
"admin1": "New Mexico", "admin2": "Santa Fe County", "fips": "35049", 
"date": ["2020-03-24", "2020-03-25", "2020-03-26"], 
"samples": [1337, 1292, 1331], 
"m50": [0.155, 0.278, 0.095], 
"m50_index": [2, 4, 1]}
...
```

The same data is available in CSV format in the
[DL-us-mobility-daterow.csv](DL-us-mobility-daterow.csv) file.

```csv
date,country_code,admin_level,admin1,admin2,fips,samples,m50,m50_index
2020-03-26,US,2,"New Mexico","Santa Fe County","35049",1331,0.095,1
...
```

An alternate arrangement of the same data in CSV format with dates in
the header, which may be preferable for some users, is in the
[DL-us-m50.csv](DL-us-m50.csv),
[DL-us-m50_index.csv](DL-us-m50_index.csv) and
[DL-us-samples.csv](DL-us-samples.csv) files.

```csv
country_code,admin_level,admin1,admin2,fips,2020-03-24,2020-03-25,2020-03-26
US,2,"New Mexico","Santa Fe County","35049",2,4,1
...
```

### Field description

- **country_code**: ISO 3166-1 alpha-2 code.
- **admin_level**: 0 for country, 1 for admin1, 2 for admin2 granularity.
- **admin1**: [GeoNames](https://www.geonames.org/) ADM1 feature name for the first-order administrative division, such as a state in the United States.
- **admin2**: [GeoNames](https://www.geonames.org/) ADM2 feature name for the second-order administrative division, such as a county or borough in the United States.
- **fips**: [FIPS code](https://www.census.gov/quickfacts/fact/note/US/fips), a
standard geographic identifier, to make it easier to combine this data
with other data sets.
- **samples**: The number of samples observed in the specified region.
- **m50**: The median of the max-distance mobility for all samples in the specified region.
- **m50_index**: The percent of normal m50 in the region, with normal m50 defined during 2020-02-17 to 2020-03-07.

## License and Attribution

This data is licensed under a [Creative Commons Attribution 4.0
International License](https://creativecommons.org/licenses/by/4.0/), which requires attribution to "Descartes
Labs."  Scientific publications may cite,

Warren, Michael S. & Skillman, Samuel W. "Mobility Changes in Response
to COVID-19".  *Descartes Labs Technical
Report*. 2020. [www.descarteslabs.com/mobility-v097/](https://www.descarteslabs.com/mobility-v097)

For online use, please additionally link to our page at
[descarteslabs.com/mobility/](https://descarteslabs.com/mobility/).

See the [LICENSE](LICENSE) for the terms of use for this data.

## Contact Us

If you have questions, please contact us at:

<dl-covid-19@descarteslabs.com>

We also encourage you to register with us in order to receive updates about the
analysis methodology or changes to this data.

## Related Press Coverage

* *New York Times* - [How Has Your State Reacted to Social
  Distancing?](https://www.nytimes.com/interactive/2020/03/23/opinion/coronavirus-economy-recession.html) March
  23, 2020.
* *Axios* - [Mobile location data shows just how much travel has dropped off](https://www.axios.com/coronavirus-travel-9596d671-0a07-4586-841c-45bb31d20d7b.html). March 25, 2020.
* *GeekWire* - [Pandemic data mining underscores the importance of
  social distancing in China — and in
  Seattle](https://www.geekwire.com/2020/pandemic-data-mining-underscores-importance-social-distancing-china-seattle/).
  March 25, 2020.
* *Los Angeles Times* - [Empty freeways, canceled flights: How life in
  California has changed since the coronavirus
  outbreak](https://www.latimes.com/projects/california-coronavirus-effects-how-life-changed/).
  March 26, 2020.
* *Albuquerque Journal* - [Closing in on a Killer](https://www.abqjournal.com/1437618). March 29, 2020.
* *New York Times* - Where Social Distance is Practiced, and Isn't (Sunday Review, Print Edition). March 29, 2020.
* *Medium Coronavirus Blog* - [A Graph to Watch](https://coronavirus.medium.com/a-graph-to-watch-b86f37e12d80). March 30, 2020.
* *ABC 6 Philadelphia* - [INTERACTIVE: Cell phone data shows residents staying at home during COVID-19 outbreak](https://6abc.com/covid19-new-jersey-delaware-pennsylvania-philadelphia/6064079/). March 30, 2020.
* *ABC 7 Chicago* - [Coronavirus Chicago: Cell phone data shows Cook County travel plummets after stay-at-home order](https://abc7chicago.com/health/cell-phone-data-shows-chicagoans-are-in-fact-staying-home-during-pandemic/6063906/). March 30, 2020.
* *ABC 7 Los Angeles* - [Coronavirus: Physical distancing lags in Inland Empire, data shows](https://abc7.com/inland-empire-california-san-bernardino-socal/6063550/). March 30, 2020.
* *ABC 11 Raleigh* - [Cellphone data shows how well North Carolina counties are following social distancing rules](https://abc11.com/health/hows-north-carolina-doing-with-social-distancing-weve-got-the-data/6064282/). March 30, 2020.
* *ABC 13 Houston* - [Cell phone data shows people moving around less after stay-at-home order](https://abc13.com/houston-stay-home-order-are-people-really-following-in-lockdown-shelter-place/6064419/). March 30, 2020.
* *San Francisco Business Times* - [Bay Area transit is running almost empty in midst of COVID-19 shutdown](https://www.bizjournals.com/sanfrancisco/news/2020/03/31/bay-area-transit-is-running-almost-empty-in-midst.html). March 31, 2020.
