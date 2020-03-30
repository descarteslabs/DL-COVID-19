import sys
import json
import glob
import base64
import numpy as np
from collections import OrderedDict
from operator import getitem
import datetime as dt
from datetime import timedelta
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import WeekdayLocator, DayLocator, DateFormatter, date2num
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
import logging

logging.getLogger("matplotlib.font_manager").disabled = True

dl_logo64 = BytesIO(
    base64.decodebytes(
        b"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"
    )
)


def plot_covid(
    loc,
    cat,
    cty_state,
    wknd="skip weekends",
    start="2020-03-02",
    end=str(dt.date.today()),
    in_fn=f"DL-us-mobility.ndjson",
    out_fn=f"DL_mobility-index_{str(dt.date.today())}",
):

    """ 
    Parameters
    ----------
    loc : list
        a list of strings with names of counties, states, or both. default is a
        list containing: California, Texas, New York, Illinois, Washington, Florida.
    cat : list
        categorizes loc as states, counties, both, or rank; "rank" specifies 
        to rank top ten counties within a state or states. default is state.
    cty_state : str or list
        a string or list of strings with the state that corresponds to
        counties if that is what is specified in loc
    wknd : bool
        if weekends, include weekend dates; if skip_weekends, only include
        weekdays. default is False.
    start : str
        starting date for plot. optional.
    end: str
        ending date for plot. optional.
    in_fn: str
        input filename for plotting. optional.
    out_fn: str
        output filename for figure. default is "DL_mobility-index_{today}.png. optional. 
        
    Returns
    -------
    plot of mobility indices for specified locations and dates
    """

    # organize data
    data = {}
    states = []

    if (cat == "county" or cat == "both") and cty_state == None:
        print(
            "Please specify states for your county or counties to ensure you're getting the expected data."
        )

    for line in open(in_fn):
        d = json.loads(line)

        for aoi in loc:

            aoi = aoi.title()

            # state or default for county / both for if county states aren't specified
            if (
                cat == "state"
                or (cat == "county" and cty_state == None)
                or (cat == "both" and cty_state == None)
            ):

                if (aoi in d["admin1"] and d["admin_level"] == 1) or (
                    aoi in d["admin2"] and d["admin_level"] == 2
                ):
                    states.append(d["admin1"])
                    data[aoi] = {}
                    data[aoi]["dates"] = d["date"]
                    data[aoi]["m50"] = d["m50_index"]
                    data[aoi]["samples"] = d["samples"]

            # counties all from the same state
            if (cat == "county" or cat == "both") and len(cty_state) == 1:

                state = cty_state[0].title()

                if (aoi in d["admin2"] or aoi in d["admin1"]) and state in d["admin1"]:
                    states.append(d["admin1"])
                    data[aoi] = {}
                    data[aoi]["dates"] = d["date"]
                    data[aoi]["m50"] = d["m50_index"]
                    data[aoi]["samples"] = d["samples"]

            # counties from different states
            if (cat == "county" or cat == "both") and len(cty_state) > 1:

                for cty_st in cty_state:

                    if loc.index(aoi.lower()) == cty_state.index(cty_st):
                        state = cty_st.title()

                        if aoi.title() in d["admin2"] and state in d["admin1"]:
                            states.append(d["admin1"])
                            data[aoi] = {}
                            data[aoi]["dates"] = d["date"]
                            data[aoi]["m50"] = d["m50_index"]
                            data[aoi]["samples"] = d["samples"]
                            data[aoi]["state"] = d["admin1"]

            # counties ranked for a specific state
            if cat == "rank":

                if aoi in d["admin1"] and d["admin_level"] == 2:
                    data[d["admin2"]] = {}
                    data[d["admin2"]]["dates"] = d["date"]
                    data[d["admin2"]]["m50"] = d["m50_index"]
                    data[d["admin2"]]["samples"] = d["samples"]

    # prepare for plotting
    orddata = OrderedDict(sorted(data.items(), key=lambda x: getitem(x[1], "samples")))

    if cat == "rank":
        items = list(orddata.items())[-10:]
    else:
        items = list(orddata.items())

    mindex = {"x": [], "y": [], "label": []}

    for item in items:

        aoi = {"x": [], "y": []}

        for n in range(len(item[1]["dates"])):
            date = item[1]["dates"][n]
            m50 = item[1]["m50"][n]

            day = dt.date(int(date[:4]), int(date[5:7]), int(date[8:10])).weekday()

            if not wknd and (day == 5 or day == 6):
                continue

            if not wknd and (day != 5 or day != 6):
                aoi["x"].append([dt.datetime.strptime(date, "%Y-%m-%d")])
                aoi["y"].append(m50)

            if wknd:
                aoi["x"].append([dt.datetime.strptime(date, "%Y-%m-%d")])
                aoi["y"].append(m50)

        mindex["x"].append(aoi["x"])
        mindex["y"].append(aoi["y"])
        mindex["label"].append(item[0])

    # plot data
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Source Sans Pro"]

    fig, ax = plt.subplots(figsize=(8, 6))

    filled_markers = ["v", "^", "<", ">", "8", "s", "p"]

    for i in range(len(mindex["label"])):
        if i <= 8:
            plt.plot(
                mindex["x"][i], mindex["y"][i], marker="o", label=mindex["label"][i]
            )
        if i > 8:
            plt.plot(
                mindex["x"][i],
                mindex["y"][i],
                marker=filled_markers[i % 7],
                label=mindex["label"][i],
            )

    ax.set_ylabel("Mobility Index", fontsize=12)
    ax.set_ylim(0, 200)

    ax.set_xlim(
        dt.datetime.strptime(start, "%Y-%m-%d"), dt.datetime.strptime(end, "%Y-%m-%d")
    )
    plt.setp(ax.get_xticklabels(), rotation=50)

    plt.grid(axis="y")

    ax.xaxis.set_major_locator(WeekdayLocator(byweekday=MO))
    ax.xaxis.set_major_formatter(DateFormatter("%b %d"))

    logo = plt.imread(dl_logo64)

    if len(loc) <= 5 and cat != "rank":
        ax.legend(
            loc="upper center",
            fontsize=11,
            bbox_to_anchor=(0.75, -0.16),
            ncol=2,
            frameon=False,
        )
        ax.figure.figimage(logo, 200, 100, alpha=1.0, zorder=1)
        plt.figtext(
            0.08,
            -0.15,
            "CC BY 4.0  descarteslabs.com/mobility",
            ha="left",
            va="bottom",
            alpha=0.5,
            fontsize=8,
        )

    if len(loc) > 5 and len(loc) <= 12 or cat == "rank":
        ax.legend(
            loc="upper center",
            fontsize=11,
            bbox_to_anchor=(0.75, -0.16),
            ncol=2,
            frameon=False,
        )
        ax.figure.figimage(logo, 200, 100, alpha=1.0, zorder=1)
        plt.figtext(
            0.08,
            -0.05,
            "CC BY 4.0  descarteslabs.com/mobility",
            ha="left",
            va="bottom",
            alpha=0.5,
            fontsize=8,
        )

    if len(loc) > 12:
        ax.legend(
            loc="upper center",
            fontsize=11,
            bbox_to_anchor=(0.75, -0.16),
            ncol=3,
            frameon=False,
        )
        ax.figure.figimage(logo, 130, 130, alpha=1.0, zorder=1)
        plt.figtext(
            0.08,
            -0.05,
            "CC BY 4.0  descarteslabs.com/mobility",
            ha="left",
            va="bottom",
            alpha=0.5,
            fontsize=8,
        )

    plt.subplots_adjust(bottom=0.7)
    fig.tight_layout()

    # format titles based on user input
    if cat == "state":
        plt.title("United States")

    if cat == "county" or cat == "both":
        if len(set(states)) == 1:
            plt.title(states[0] + " Counties")

        if len(set(states)) != 1:
            plt.title("United States: Counties")

    if cat == "rank" and len(loc) == 1:
        plt.title(loc[0].title())

    if cat == "rank" and len(loc) > 1:
        plt.title("United States county comparisons")

    if cat == "both" and len(set(states)) != 1:
        plt.title("United States + Counties")

    # plot and save figure
    plt.draw()
    fig.savefig("{}.png".format(out_fn), bbox_inches="tight", pad_inches=0.1, dpi=200)


if __name__ == "__main__":
    
    import argparse
    import datetime as dt

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--location", type=str, nargs="*", help="location names of interest"
    )
    parser.add_argument(
        "--category",
        type=str,
        choices=["state", "county", "both", "rank"],
        default="state",
    )
    parser.add_argument(
        "--county_state",
        type=str,
        nargs="*",
        default=None,
        help="specify the state for county inputs",
    )
    parser.add_argument("--weekends", dest="weekend", action="store_true")
    parser.add_argument("--skip_weekends", dest="weekend", action="store_false")
    parser.set_defaults(feature=True)
    parser.add_argument("--start_date", type=str, default="2020-03-02")
    parser.add_argument("--end_date", type=str, default=str(dt.date.today()))
    parser.add_argument(
        "--input_filename",
        type=str,
        default="DL-us-mobility.ndjson",
        help="ndjson file to load if not default",
    )
    parser.add_argument(
        "--output_filename",
        type=str,
        default=str(dt.date.today()),
        help="output filename for plot: DL_mobility-index_NAME.png",
    )

    args = parser.parse_args()

    if args.location is None:
        print(
            "No user-specified locations were entered. Using default locations California, Texas, New York, Illinois, Washington, Florida"
        )
        location = [
            "California",
            "Texas",
            "New York",
            "Illinois",
            "Washington",
            "Florida",
        ]
        category = "state"

    if args.location is not None:
        location = args.location

    category = args.category
    county_state = args.county_state
    weekend = args.weekend
    start_date = args.start_date
    end_date = args.end_date
    input_filename = args.input_filename
    output_filename = "DL_mobility-index_{}".format(args.output_filename)

    plot_covid(
        location,
        category,
        county_state,
        weekend,
        start_date,
        end_date,
        input_filename,
        output_filename,
    )
