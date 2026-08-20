# Amazon Selenium Automation

A lightweight Python automation project that uses Selenium to read Amazon ASINs from a text file and retrieve available product information from Amazon.de.

## Features

- Reads ASINs from `asins.txt`
- Opens Amazon.de in English
- Sets the delivery country to the United States
- Retrieves available product title, price, and delivery information
- Prints `Not available` when a field cannot be found
- Stops cleanly if the browser window is closed
- Uses Selenium Manager, so ChromeDriver does not need to be installed manually

## Requirements

- Python 3.11+ (tested)
- Google Chrome

Install the dependency:

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

Run the automation:

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

If a field cannot be retrieved, the script keeps the remaining data:

```text
Price: Not available
```

## Project Structure

```text
Amazon-Selenium-Automation/
├── main.py
├── asins.txt
├── requirements.txt
└── .gitignore
```

## Notes

Amazon pages and selectors can change over time, so element IDs or CSS selectors may occasionally need to be updated. Product price and delivery information can also vary by product, seller, and selected delivery country.
