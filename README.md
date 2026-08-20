# Amazon Selenium Scraper

A simple Python Selenium scraper that reads Amazon ASINs from a text file and retrieves available product information from Amazon.de.

## Features

- Reads ASINs from `asins.txt`
- Retrieves:
  - Product title
  - Price
  - Delivery information
- Displays `Not available` when a field cannot be found
- Stops cleanly if the browser window is closed
- Uses Selenium Manager, so ChromeDriver does not need to be installed manually

## Requirements

- Python 3.11+
- Google Chrome

Install the required package:

```bash
pip install -r requirements.txt
```

## Usage

Add ASINs to `asins.txt`, one per line:

```text
B08P16WZHT
B004YND1ZA
B08KS2TZ64
```

Run the scraper:

```bash
python main.py
```

## Example Output

```text
[1] B08P16WZHT
Title: Example Product
Price: €19.99
Delivery: FREE delivery August 25
------------------------------------------------------------
```

If a value cannot be retrieved:

```text
Price: Not available
```

## Project Structure

```text
Selenium/
├── main.py
├── asins.txt
├── requirements.txt
└── .gitignore
```

## Note

Amazon frequently changes its page structure. CSS selectors or element IDs may need to be updated if product information can no longer be retrieved.
