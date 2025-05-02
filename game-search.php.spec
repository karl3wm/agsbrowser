generated with claude.ai 3.7 sonnet from the search page source and an example request

# game-search.php API Specification

## Overview
Endpoint for searching games in the Adventure Game Studio database.

## Endpoint
URL: https://www.adventuregamestudio.co.uk/site/mvc/services/game-search.php
Method: POST
Content-Type: application/json

## Known Request Parameters
- page-number (integer): Page number for pagination
- title-or-author (string): Search text for game title or author name
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
The search filter fields are dynamically loaded from
`search-filter-content.php` into the desktop and mobile filter
containers. These fields are likely to include:

- Genre filters
- Platform compatibility filters
- Release year filters
- Language filters
- Rating filters
- Special category filters (awards, featured games, etc.)

A comprehensive documentation of these fields would require
examination of the `search-filter-content.php` file, which is not
included in the provided source. The API likely accepts these filter
parameters in addition to the ones documented above.

## Response Format
JSON object containing:
- game_results (array): List of game objects with properties:
  - id (integer): Unique game identifier
  - name (string): Game title
  - author (string): Game creator
  - filename (string): Path to thumbnail image
  - release_date (string): ISO format date/time of release
  - panel_rating (integer/float): Editorial rating
  - player_rating_avg (float): Average user rating (-1 if none)
  - awards_winner (mixed): Award winner information
  - awards_nominee (mixed): Award nomination information
  - downloads_total (integer): Total download count
  - downloads_this_month (integer): Downloads in current month
  - panel_date (string): Date of panel rating
  - picks_month (mixed): Featured month information
  - total_results (integer): Total number of games matching criteria
  - sort_type (integer): Sort method used
  - filter_type (integer): Filter method used
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

- For complete documentation of filter parameters, the contents of
search-filter-content.php would need to be examined

- The application's JavaScript (particularly search.min.js) likely
handles the collection of all form fields and filters before
submitting to the API

- Network monitoring during form interactions would reveal the complete
structure of requests with filters applied
