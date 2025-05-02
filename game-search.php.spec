original content generated with claude.ai 3.7 sonnet from the search page source and an example request
updated based on content from search-filter-content.php by gemini-2.5-flash-preview-04-17

# game-search.php API Specification

## Overview
Endpoint for searching games in the Adventure Game Studio database.

## Endpoint
URL: https://www.adventuregamestudio.co.uk/site/mvc/services/game-search.php
Method: POST
Content-Type: application/json

## Known Request Parameters
- page-number (integer string): Page number for pagination (e.g., "1", "2")
- title-or-author (string): Search text for game title or author name. Can be empty.
- sort (string): Sorting method ID, options include:
  - "1": Title A-Z
  - "2": Title Z-A
  - "3": Author A-Z
  - "4": Author Z-A
  - "5": Newest Releases (default)
  - "6": Oldest Releases
  - "7": Highest Panel Rating
  - "8": Lowest Panel Rating
  - "9": Highest Player Rating
  - "10": Lowest Player Rating
  - "11": AGS Awards Won
  - "12": Most Popular Ever
  - "13": Most Popular This Month
  - "14": Newest Comments
  - "15": Newest Picks of the Month
  - "16": Newest Panel Rating
  - "17": Oldest Panel Rating

## Filter Parameters
Filter parameters are included in the POST request if the corresponding checkbox is selected in the search form. The parameter name is derived from the `name` attribute of the checkbox, and the value from its `value` attribute. Most checkbox filters send a value of `1` when checked, but some use specific numerical identifiers (e.g., ratings, lengths, languages). Multiple filters can be selected within and across categories.

The filter parameters identified from `search-filter-content.php` are:

### Rating
- **Panel Rating:** Filter by panel rating level. Value is the rating (1-5) or 0 for no rating.
  - `panel-5-stars` (integer): Value 5
  - `panel-4-stars` (integer): Value 4
  - `panel-3-stars` (integer): Value 3
  - `panel-2-stars` (integer): Value 2
  - `panel-1-star` (integer): Value 1
  - `panel-no-rating` (integer): Value 0 (No panel rating)
- **Player Rating:** Filter by player rating level or status. Value is the rating (1-5) or -1.
  - `player-5-stars` (integer): Value 5
  - `player-4-stars` (integer): Value 4
  - `player-3-stars` (integer): Value 3
  - `player-2-stars` (integer): Value 2
  - `player-1-star` (integer): Value 1
  - `player-not-enough-votes` (integer): Value -1 (Not enough player votes)

### AGS Awards
- `ags-award-winners` (integer): Include games that won an AGS Award. Value is 1 if checked.
- `ags-award-nominees` (integer): Include games that were nominated for an AGS Award. Value is 1 if checked.

### Game Length
- Filter by game length category. Value is a numerical ID for the length type.
  - `length-full-length-games` (integer): Value 1
  - `length-medium-length-games` (integer): Value 6
  - `length-short-games` (integer): Value 0
  - `length-non-adventure-games` (integer): Value 3
  - `length-training-games` (integer): Value 7
  - `length-joke-games` (integer): Value 4
  - `length-demo-games` (integer): Value 5
  - `length-length-not-set` (integer): Value 15

### Release Type
- Filter by release type. Value is a numerical ID.
  - `release-commercial` (integer): Value 1
  - `release-freeware` (integer): Value 0

### Operating System
- Filter by compatible operating system. Value is a numerical ID.
  - `os-windows` (integer): Value 1
  - `os-linux` (integer): Value 2
  - `os-macos` (integer): Value 3
  - `os-android` (integer): Value 4
  - `os-ios` (integer): Value 4 (Note: Shares value with Android)

### Setting
- Filter by game setting. Value is a numerical ID.
  - `setting-contemporary` (integer): Value 1
  - `setting-historical` (integer): Value 2
  - `setting-fantasy` (integer): Value 3
  - `setting-sci-fi` (integer): Value 4
  - `setting-other` (integer): Value 5
  - `setting-not-set` (integer): Value 0

### Genre
- Filter by game genre. Value is a numerical ID.
  - `genre-comedy` (integer): Value 1
  - `genre-drama` (integer): Value 2
  - `genre-horror` (integer): Value 3
  - `genre-investigative` (integer): Value 4
  - `genre-other` (integer): Value 5
  - `genre-not-set` (integer): Value 0

### Story Type
- Filter by story type. Value is a numerical ID.
  - `story-type-original` (integer): Value 1
  - `story-type-parody` (integer): Value 2
  - `story-type-remake` (integer): Value 3
  - `story-type-fan-game` (integer): Value 4
  - `story-type-other` (integer): Value 5
  - `story-type-not-set` (integer): Value 0

### Language
- Filter by game language. Parameter name uses `language-` followed by the language name. Value is a numerical language ID. Examples:
  - `language-czech` (integer): Value 30
  - `language-dutch` (integer): Value 35
  - `language-english` (integer): Value 36
  - `language-espanol` (integer): Value 38
  - `language-finnish` (integer): Value 41
  - `language-french` (integer): Value 43
  - `language-georgian` (integer): Value 52
  - `language-german` (integer): Value 53
  - `language-greek` (integer): Value 55
  - `language-hakka-chinese` (integer): Value 59
  - `language-hebrew` (integer): Value 61
  - `language-hungarian` (integer): Value 64
  - `language-icelandic` (integer): Value 66
  - `language-italian` (integer): Value 71
  - `language-japanese` (integer): Value 73
  - `language-korean` (integer): Value 83
  - `language-norwegian` (integer): Value 115
  - `language-polish` (integer): Value 123
  - `language-portuguese` (integer): Value 125
  - `language-romanian` (integer): Value 131
  - `language-russian` (integer): Value 132
  - `language-slovak` (integer): Value 140
  - `language-spanish` (integer): Value 143
  - `language-swedish` (integer): Value 148
  - `language-turkish` (integer): Value 164
  *(This list includes all languages found in the source)*

### Year
- Filter by release year or age. Parameter name indicates the year or range. Value is 1 if checked.
  - `year-2025` (integer): Value 1
  - `year-2024` (integer): Value 1
  - `year-2023` (integer): Value 1
  - `year-2022` (integer): Value 1
  - `year-2021` (integer): Value 1
  - `year-2020` (integer): Value 1
  - `year-2019` (integer): Value 1
  - `year-2018` (integer): Value 1
  - `year-2017` (integer): Value 1
  - `year-2016` (integer): Value 1
  - `year-2015` (integer): Value 1
  - `year-older-than-2015` (integer): Value 1 (Includes 2014 and older)

### Tags
- Filter by tag. Parameter name uses `tag-` followed by the tag ID. Value is 1 if checked. Tag IDs correspond to the human-readable tag names provided in the labels.
  - `tag-1` (integer): Value 1 (Non-Adventure)
  - `tag-2` (integer): Value 1 (Fantasy)
  - `tag-3` (integer): Value 1 (Medieval)
  - `tag-4` (integer): Value 1 (Educational)
  - `tag-5` (integer): Value 1 (RPG)
  - `tag-6` (integer): Value 1 (Adventure)
  - `tag-7` (integer): Value 1 (Hybrid)
  - `tag-8` (integer): Value 1 (Quiz)
  - `tag-9` (integer): Value 1 (Child-friendly)
  - `tag-11` (integer): Value 1 (Hidden object)
  - `tag-13` (integer): Value 1 (Escape the room)
  - `tag-14` (integer): Value 1 (Gameboy)
  - `tag-15` (integer): Value 1 (Dystopian)
  - `tag-16` (integer): Value 1 (History)
  - `tag-17` (integer): Value 1 (Museum)
  - `tag-18` (integer): Value 1 (Retro)
  - `tag-20` (integer): Value 1 (90s)
  - `tag-21` (integer): Value 1 (Word Game)
  - `tag-22` (integer): Value 1 (simulation)
  - `tag-23` (integer): Value 1 (Chuck)
  - `tag-24` (integer): Value 1 (Maniac Mansion)
  - `tag-25` (integer): Value 1 (Choices Matter)
  - `tag-26` (integer): Value 1 (Wild West)
  - `tag-27` (integer): Value 1 (casual)
  *(This list includes all tags found in the source)*

### Other
- Various other filter options. Value is 1 if checked.
  - `other-play-in-browser` (integer): Value 1 (Play in Browser)
  - `other-mags` (integer): Value 1 (MAGS games)
  - `other-pick-of-the-month` (integer): Value 1 (Pick of the Month)
  - `other-voice-acting` (integer): Value 1 (Voice Acting)
  - `other-filthy` (integer): Value 1 (The Most Filthy games)
  - `other-broken-images` (integer): Value 1 (Marked as Broken Images)
  - `other-broken-videos` (integer): Value 1 (Marked as Broken Videos)
  - `other-broken-downloads` (integer): Value 1 (Marked as Broken Downloads)
  - `other-missing-downloads` (integer): Value 1 (Marked as Missing Downloads)

## Response Format
JSON object containing:
- game_results (array): List of game objects with properties:
  - id (integer): Unique game identifier
  - name (string): Game title
  - author (string): Game creator
  - filename (string): Path to thumbnail image
  - release_date (string): ISO format date/time of release
  - panel_rating (integer/float): Editorial rating (0-5, or null)
  - player_rating_avg (float): Average user rating (0-5, or -1 if none/not enough votes)
  - awards_winner (mixed): Award winner information (e.g., array of years, or null)
  - awards_nominee (mixed): Award nomination information (e.g., array of years, or null)
  - downloads_total (integer): Total download count
  - downloads_this_month (integer): Downloads in current month
  - panel_date (string): Date of panel rating (YYYY-MM-DD HH:MM:SS format, or null)
  - picks_month (mixed): Featured month information (e.g., array of month/year strings, or null)
  - total_results (integer): Total number of games matching criteria
  - sort_type (integer): Sort method used (corresponds to `sort` parameter values 1-17)
  - filter_type (integer): Internal filter identifier (likely not relevant to external use)
  - play_in_browser (integer): Browser playability flag (0/1)

## Sample Request
{
  "page-number": "1",
  "title-or-author": "",
  "sort": "5"
}

## Sample Response
{
  "game_results": [
    {
      "id": 2858,
      "name": "Another Heaven",
      "author": "Akril15",
      "filename": "/site/assets/img/games/thumbs/2858_1.png",
      "release_date": "2025-04-20 19:54:59",
      "panel_rating": 0,
      "player_rating_avg": -1,
      "awards_winner": null,
      "awards_nominee": null,
      "downloads_total": 36,
      "downloads_this_month": 36,
      "panel_date": null,
      "picks_month": null,
      "total_results": 2485,
      "sort_type": 5,
      "filter_type": 0,
      "play_in_browser": 0
    }
  ]
}

## Notes

- The "Filter Parameters" section is now documented based on the checkbox inputs found in `search-filter-content.php` but this has not been reviewed or tuned.
- Further network monitoring during form interactions would reveal further structure of responses.
- The application's JavaScript (particularly search.min.js) handles the collection of all checked form fields and filters before submitting the complete JSON payload to the API.
