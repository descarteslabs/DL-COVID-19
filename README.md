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
[arxiv.org/pdf/2003.14228.pdf](https://arxiv.org/pdf/2003.14228.pdf).
We intend to update the data in this repository regularly.

Note: Data for 2020-04-20, 2020-05-29, 2020-10-08, 2020-12-11 through 2020-12-18, 2021-01-08 through 2021-01-14, 2021-04-07 and 2021-04-12 did not meet quality control standards, and was not released.

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

## Visualization and Analysis

* *GeoDS Lab @ UW-Madison* - [geods.geography.wisc.edu/covid19/physical-distancing/](https://geods.geography.wisc.edu/covid19/physical-distancing/)

* *Descartes Labs* - [www.descarteslabs.com/mobility/#overview](https://www.descarteslabs.com/mobility/#overview)

* *Nik Haldimann* - [Lockdown Hack #2: Towards proving that social distancing works](https://blog.nikhaldimann.com/2020/04/14/lockdown-hack-2-towards-proving-that-social-distancing-works/)

* *Ballad Health* - [COVID-19 Physical Distancing Scorecard](https://www.balladhealth.org/covid-19-physical-distancing-scorecard)

* *The Institute for Health Metrics and Evaluation (IHME)* - [COVID-19: What’s New for April 17, 2020](http://www.healthdata.org/sites/default/files/files/Projects/COVID/Estimation_update_041720.pdf)

* *DataHaven (Regional Data Cooperative)* - [COVID-19 in Connecticut](https://ct-data-haven.github.io/covidpub)

* *Mathematical Humanity Lab, Dartmouth College* - [When and how will
  the COVID-19 pandemic end in the United States?](https://fudab.github.io/covid-19/us)

* *Beyond Limits* - [Beyond Limits Coronavirus Dynamic Predictive Model](https://www.beyond.ai/news/beyond-limits-builds-dynamic-forecasting-model-to-help-in-fight-against-covid-19/)

* *City of Los Angeles and RMDS* - [2020 COVID-19 Computational Challenge](https://grmds.org/2020challenge)

* *Climate Central* - [Travel and Air Pollution During COVID-19](https://medialibrary.climatecentral.org/resources/travel-and-air-pollution-during-covid-19)

* *Russ Gerber* - [Communicating Disease - The Startup - Medium](https://medium.com/swlh/communicating-disease-56f8b72dc2f0)

* *Hawaii Data Collaborative* - [Tracking COVID-19 In Hawaii](https://www.hawaiidata.org/covid19)

* *Center for Data Innovation* - [Visualizing How Far People Are Traveling in the United States](https://www.datainnovation.org/2020/06/visualizing-how-far-people-are-traveling-in-the-united-states/)

* *Google Cloud AI and Harvard Global Health Institute* - [COVID-19 Public Forecasts](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-is-releasing-the-covid-19-public-forecasts)

## License and Attribution

This data is licensed under a [Creative Commons Attribution 4.0
International License](https://creativecommons.org/licenses/by/4.0/), which requires attribution to "Descartes
Labs."  Scientific publications may cite,

Warren, Michael S. & Skillman, Samuel W. "Mobility Changes in Response
to COVID-19". *arXiv:2003.14228 [cs.SI]*, Mar. 2020. [arxiv.org/abs/2003.14228](https://arxiv.org/abs/2003.14228)

For online use, please additionally link to our page at
[descarteslabs.com/mobility/](https://descarteslabs.com/mobility/).

See the [LICENSE](LICENSE) for the terms of use for this data.

## Contact Us

If you have questions, please contact us at:

<dl-covid-19@descarteslabs.com>

We also encourage you to register with us in order to receive updates about the
analysis methodology or changes to this data.

## Citations

Song Gao, Jinmeng Rao, Yuhao Kang, Yunlei Liang, Jake Kruse, "Mapping
county-level mobility pattern changes in the United States in response
to COVID-19". *arXiv:2004.04544 [physics.soc-ph]*,
Apr. 2020. [arxiv.org/abs/2004.04544](https://arxiv.org/abs/2004.04544)

Shuo Chen, Qin Li, Song Gao, Yuhao Kang, Xun Shi, "Mitigating COVID-19
outbreak via high testing capacity and strong
transmission-intervention in the United States". *medRxiv*, Apr. 2020.
[www.medrxiv.org/content/10.1101/2020.04.03.20052720v1](https://www.medrxiv.org/content/10.1101/2020.04.03.20052720v1)

IHME COVID-19 health service utilization forecasting team, Christopher
JL Murray, "Forecasting the impact of the first wave of the COVID-19
pandemic on hospital demand and deaths for the USA and European
Economic Area countries". *medRxiv*, Apr. 2020.
[www.medrxiv.org/content/10.1101/2020.04.21.20074732v1](https://www.medrxiv.org/content/10.1101/2020.04.21.20074732v1)

Song Gao, Jinmeng Rao, Yuhao Kang, Yunlei Liang, Jake Kruse, Doerte
Doepfer, Ajay K. Sethi, Juan Francisco Mandujano Reyes, Jonathan Patz,
Brian S. Yandell, "Mobile phone location data reveal the effect and
geographic variation of social distancing on the spread of the
COVID-19 epidemic". *arXiv:2004.11430 [cs.SI]*,
Apr. 2020. [arxiv.org/abs/2004.11430](https://arxiv.org/abs/2004.11430)

Sepehr Ghader, Jun Zhao, Minha Lee, Weiyi Zhou, Guangchen Zhao, Lei
Zhang, "Observed mobility behavior data reveal social distancing
inertia". *arXiv:2004.14748 [cs.CY]*,
Apr. 2020. [arxiv.org/abs/2004.14748](https://arxiv.org/abs/2004.14748)

Nabarun Dasgupta, Michele Jonsson Funk, Allison Lazard, Benjamin
Eugene White, Stephen W. Marshall, "Quantifying the social distancing
privilege gap: a longitudinal study of smartphone
movement". *medRxiv*, May 2020.
[www.medrxiv.org/content/10.1101/2020.05.03.20084624v1](https://www.medrxiv.org/content/10.1101/2020.05.03.20084624v1)

Donghai Liang, Liuhua Shi, Jingxuan Zhao, Pengfei Liu, Joel Schwartz,
Song Gao, Jeremy A Sarnat, Yang Liu, Stefanie T Ebelt, Noah C
Scovronick, Howard Chang, "Urban Air Pollution May Enhance COVID-19
Case-Fatality and Mortality Rates in the United States". *medRxiv*, May 2020.
[www.medrxiv.org/content/10.1101/2020.05.04.20090746v1](https://www.medrxiv.org/content/10.1101/2020.05.04.20090746v1)

Grant McKenzie, Benjamin Adams, "A country comparison of place-based
activity response to COVID-19 policies". *arXiv:2005.08738 [cs.SI]*,
May 2020. [arxiv.org/abs/2005.08738](https://arxiv.org/abs/2005.08738)

Teodoro Alamo, D. G. Reina, Pablo Millán, "Data-Driven Methods to
Monitor, Model, Forecast and Control Covid-19 Pandemic: Leveraging
Data Science, Epidemiology and Control Theory". *arXiv:2006.01731
[q-bio.PE]*,
June 2020. [arxiv.org/abs/2006.01731](https://arxiv.org/abs/2006.01731)

Ivan Franch-Pardo, Brian M. Napoletano, Fernando Rosete-Verges and Lawal Billa. "Spatial analysis and GIS in the study of COVID-19. A review." *Science of The Total Environment*, June 2020. 140033. [www.sciencedirect.com/science/article/pii/S0048969720335531](https://www.sciencedirect.com/science/article/pii/S0048969720335531)

Petrônio CL Silva, Paulo VC Batista, Hélder S. Lima, Marcos A. Alves,
Frederico G. Guimarães, and Rodrigo CP Silva. "COVID-ABS: An
Agent-Based Model of COVID-19 Epidemic to Simulate Health and Economic
Effects of Social Distancing Interventions." *Chaos, Solitons &
Fractals*, July 2020. 110088. [www.sciencedirect.com/science/article/abs/pii/S0960077920304859](https://www.sciencedirect.com/science/article/abs/pii/S0960077920304859)

Xiao Huang, Zhenlong Li, Yuqin Jiang, Xinyue Ye, Chengbin Deng, Jiajia
Zhang, Xiaoming Li, "The characteristics of multi-source mobility
datasets and how they reveal the luxury nature of social distancing in
the U.S. during the COVID-19 pandemic". *medRxiv*,
Aug. 2020. [www.medrxiv.org/content/10.1101/2020.07.31.20143016v1](https://www.medrxiv.org/content/10.1101/2020.07.31.20143016v1)


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
* *ABC 30 Fresno* - [Valley residents traveling farther than most Californians, cell phone data shows](https://abc30.com/health/valley-residents-traveling-farther-than-most-californians/6066684/) March 31, 2020.
* *San Francisco Business Times* - [Bay Area transit is running almost empty in midst of COVID-19 shutdown](https://www.bizjournals.com/sanfrancisco/news/2020/03/31/bay-area-transit-is-running-almost-empty-in-midst.html). March 31, 2020.
* *PBS Arizona* - [Why the air in metro Phoenix is fresher these days](https://cronkitenews.azpbs.org/2020/04/01/why-the-air-in-metro-phoenix-is-fresher-these-days/). April 1, 2020.
* *WBAL Maryland* - [Data shows social distancing during coronavirus pandemic works](https://www.wbaltv.com/article/coronavirus-pandemic-social-distancing-data/32007539). April 1, 2020.
* *Tucson Sentinel* - [Fresh air in Phoenix: ADEQ collecting data on CV-19 impact on emissions](http://www.tucsonsentinel.com/local/report/040220_cv_air_pollution/fresh-air-phoenix-adeq-collecting-data-cv-19-impact-emissions/). April 2, 2020.
* *Minnesota Star Tribune* - [Minnesota's COVID-19 response shows promise in helping to slow virus](https://www.startribune.com/keep-it-up-minnesota-covid-19-response-shows-promise/569384442/). April 5, 2020.
* *Albuquerque Journal* - [Tech startups, manufacturers help during crisis](https://www.abqjournal.com/1440528/tech-startups-manufacturers-help-during-crisis.html). April 6, 2020.
* *Fox News* - [Smartphones can track how much people are staying home](https://video.foxnews.com/v/6147456838001). April 6, 2020.
* *Washington Daily News* - [Beaufort County gets ‘F’ in social distancing](https://www.thewashingtondailynews.com/2020/04/06/beaufort-county-gets-f-in-social-distancing/). April 6, 2020.
* *ABC 7 New York* - [Coronavirus News: Some states more successful than others at staying home](https://abc7ny.com/travel/some-states-more-successful-than-others-at-staying-home-data-shows/6082621/). April 7, 2020.
* *Albuquerque Journal* - [NM residents cut travel amid outbreak](https://www.abqjournal.com/1441809/nm-residents-cut-travel-amid-outbreak.html). April 8, 2020.
* *CNN* - [New Mexico using cell phone data to create social distancing models and considering more restrictive travel measures](https://www.cnn.com/2020/04/09/us/new-mexico-cell-phone-data-track-residents/index.html). April 9, 2020.
* *Los Alamos Monitor* - [Los Alamos gets high marks in latest virus update](https://www.lamonitor.com/content/los-alamos-gets-high-marks-latest-virus-update). April 10, 2020.
* *The Virginian-Pilot* - [Travel in Hampton Roads has dropped dramatically amid the pandemic — and it appears to be helping](https://www.pilotonline.com/news/transportation/vp-nw-coronavirus-hampton-roads-traffic-20200410-nqgvbaohbngu7ohaaif2yi7yga-story.html). April 10, 2020.
* *WRAL Raleigh* - [COVID-19 mobility data highlights disparities in rural NC counties](https://www.wral.com/coronavirus/covid-19-mobility-data-highlights-disparities-in-rural-nc-counties/19046461/). April 10, 2020.
* *Denver Post* - [How Gov. Polis recruited private engineers to analyze Colorado cellphone data during coronavirus crisis](https://www.denverpost.com/2020/04/15/polis-coronavirus-cellphone-tracking-movement/). April 15, 2020.
* *USAID Policy* - [COVID-19 and New Pathways for Development Data](https://medium.com/@USAIDPPL/covid-19-and-new-pathways-for-development-data-43f852d3d03f). April 16, 2020.
* *KRQE Albuquerque* - [New Mexico based company helps state gauge social distancing](https://www.krqe.com/health/coronavirus-new-mexico/new-mexico-based-company-helps-state-gauge-social-distancing/). April 16, 2020.
* *Washington Post* - [Governments around the world are trying a new weapon against coronavirus: Your smartphone](https://www.washingtonpost.com/technology/2020/04/17/governments-around-world-are-trying-new-weapon-against-coronavirus-your-smartphone/). April 17, 2020.
* *Albuquerque Journal* - [State traffic down, not as much as hoped](https://www.abqjournal.com/1450752/state-traffic-down-not-as-much-as-hoped.html). May 3, 2020.
* *ABC 7 Los Angeles* - [CHP: 87% increase in tickets to drivers going more than 100 mph amid COVID-19 shutdown](https://abc7.com/traffic/chp-increase-in-tickets-to-extreme-speeders-amid-covid-19-shutdown/6153943/). May 5, 2020.
* *Seven Days Vermont* - [Vermonters On the Move Again After Weeks Under Stay-Home Order](https://www.sevendaysvt.com/OffMessage/archives/2020/05/06/vermonters-on-the-move-again-after-weeks-under-stay-home-order). May 6, 2020.
* *Boston 25 News* - [Researchers: Cellular data shows more Mass. residents are traveling farther](https://www.boston25news.com/news/health/researchers-cellular-data-shows-more-mass-residents-are-traveling-further/ZUGDMLMLIREDHOIQYZU22PONYM/). May 7, 2020.
* *Tampa Bay Times* - [How Florida slowed coronavirus: Everyone stayed
  home before they were told
  to](https://www.tampabay.com/news/health/2020/05/10/how-florida-slowed-coronavirus-everyone-stayed-home-before-they-were-told-to/). May
  10, 2020.
* *Axios* - [National mobility rising, signaling driving's revival](https://www.axios.com/coronavirus-national-mobility-rising-signaling-driving-revival-c598f3b3-ec8e-42ed-9eec-cc837ae08b93.html). May 12, 2020.
* *Magnolia State Live* - [Will people be willing to venture out as state reopens? Data suggests yes … but slowly](https://www.magnoliastatelive.com/2020/05/12/will-people-be-willing-to-venture-out-as-state-reopens-data-suggests-yes-but-slowly/). May 12, 2020.
* *WCNC Charlotte* - [People are traveling farther from home lately, cell phone data shows](https://www.wcnc.com/article/news/investigations/investigators/data-shows-charlotte-area-residents-traveling-farther-from-home/275-6a3042b8-c768-46f8-a0fe-45206b70874c). May 18, 2020.
* *FOX 6 Milwaukee* - [Travel in Wisconsin dropped over 90% at one point during COVID-19 lockdown](https://fox6now.com/2020/05/20/travel-in-wisconsin-dropped-over-90-at-one-point-during-covid-19-lockdown/). May 20, 2020.
* *NBC 6 South Florida* - [Much of South Florida Open, But Experts Say it May Take a While for Shoppers to Return](https://www.nbcmiami.com/news/local/much-of-south-florida-open-but-experts-say-it-may-take-a-while-for-shoppers-to-return/2236798/). May 21, 2020.
* *New York Times* - [The Coronavirus Is Deadliest Where Democrats Live](https://www.nytimes.com/2020/05/25/us/politics/coronavirus-red-blue-states.html). May 25, 2020.
* *Axios* - [National mobility keeps rising as more states reopen
  economies](https://www.axios.com/people-driving-more-be63dcc9-a2eb-400a-ae63-c6bf3911ecc8.html).
  May 29, 2020.
* *WCVB Boston* - [Cellphone data shows Massachusetts is
  moving](https://www.wcvb.com/article/cellphone-data-shows-massachusetts-is-on-the-move/32771942). June
  5, 2020.
* *KRQE Albuquerque* - [Mobility up in New Mexico as state
  reopens](https://www.krqe.com/health/coronavirus-new-mexico/mobility-up-in-new-mexico-as-state-reopens/). June
  11, 2020.
* *Miami Herald* - [A NUMBERS GAME Floridians flattened the COVID
curve. Then, amid upbeat talk, the numbers began to
rise](https://www.miamiherald.com/news/coronavirus/article243363086.html). June
12, 2020.
* *Miami Herald* - [A NUMBERS GAME
The Florida COVID-19 data said one thing while Gov. DeSantis sometimes said another](https://www.miamiherald.com/news/politics-government/state-politics/article242937591.html). June 12, 2020.
* *WCNC Charlotte* - [Location Data: June 5 marked most active day in
  Mecklenburg County since March
  13](https://www.wcnc.com/article/news/health/coronavirus/location-data-june-5-marked-most-active-day-in-mecklenburg-county-since-march-13/275-ccbdc5ad-7073-416a-aaf0-599cb3a1161e). June
  12, 2020.
* *IHME* - [New IHME COVID-19 Model Projects Nearly 180,000 US Deaths](http://www.healthdata.org/news-release/new-ihme-covid-19-model-projects-nearly-180000-us-deaths). June 24, 2020.
* *TechRepublic* - [Travel is making a comeback–just not by plane](https://www.techrepublic.com/article/travel-is-making-a-comeback-just-not-by-plane/). June 24, 2020.
* *Tampa Bay Times* - [Florida’s coronavirus spike: 5 things to know](https://www.tampabay.com/news/health/2020/06/26/floridas-coronavirus-spike-5-things-to-know/). June 26, 2020.
* *Forbes* - [Fourth Of July Holiday Day Travel This Year Is Going To Be, Well, Different, Thanks To Coronavirus](https://www.forbes.com/sites/danielreed/2020/07/01/fourth-of-july-holiday-day-travel-this-year-is-going-to-be-well-different-thanks-to-covid-19/#5d56277ce981). July 1, 2020.
* *Axios* - [How the coronavirus pandemic changed mobility habits, by
  state](https://www.axios.com/coronavirus-mobility-habits-by-state-272d3405-4c6b-4cdb-9ee2-fe8074b657d3.html). July
  8, 2020.
* *WCVB Boston* - [Researchers: Mass. residents leaving home almost as
  much as before
  pandemic](https://www.boston25news.com/news/health/researchers-mass-residents-leaving-home-almost-much-before-pandemic/W5SLADF44VETFMYOQMQSK4I2NI/). July
  9, 2020.
* *The Hill* - [Virginia suburb of DC retains title as 'America's
  Fittest
  City'](https://thehill.com/blogs/blog-briefing-room/507094-virginia-suburb-of-dc-retains-title-as-americas-fittest-city). July
  14, 2020.
* *Venture Beat* - [Google and Harvard release COVID-19 prediction models](https://venturebeat.com/2020/08/03/google-and-harvard-release-covid-19-prediction-models/). August 3, 2020.
