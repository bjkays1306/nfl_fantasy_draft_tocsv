## Export an NFL Fantasy Football Draft to CSV

For fantasy leagues on NFL.com Fantasy Football, it might be helpful to be able to export your draft results to a spreadsheet.

For example, you might want to manage a keeper league where the prior year's draft position determines the keeper's draft round value.

This script uses beautifulsoup to scrape the public draft results page from the league and parse into a CSV file.

### Setup
(Requires Python3)

1. Clone this repo:
`git clone https://github.com/rclegg/nfl_fantasy_draft_tocsv`
2. Run `pip install -r requirements.txt`
3. Open the config.py file and set your League ID Number
4. Run `python main.py`

