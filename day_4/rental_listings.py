"""
This script automates the process of fetching rental listings from the RentCast API for a specific
zip code (98926) sorts by days on the market and sends a text message with the new listings. It also
updates a CSV file with the new rental listings data.

Functions:
- get_rentals(): Fetches rental listings from the RentCast API.
- filter_listings(df: pd.DataFrame) -> pd.DataFrame: Checks if new data contains new listings that are not currently in csv.
- send_text_message(phone_number: str, carrier: str, message: str) -> None: Sends a text message with the top rental listings information.
- main(): Orchestrates the script's workflow by calling the above functions in sequence.

Requires a configuration file (`config.py`) containing API_KEY, EMAIL, PASSWORD, CARRIERS, and NUMBER for functionality.
"""

import requests
import pandas as pd
import smtplib
from config import API_KEY, EMAIL, PASSWORD, CARRIERS, NUMBER
import os


def get_rentals() -> pd.DataFrame:

    url = "https://api.rentcast.io/v1/listings/rental/long-term?zipCode=98926&status=Active&limit=100"

    headers = {"accept": "application/json", "X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers)

    rental_listings_df = pd.DataFrame(response.json())

    return rental_listings_df


def filter_listings(df) -> pd.DataFrame:

    historic_listings = pd.read_csv("data/rental/cleaned/rental_listings.csv")

    historic_ids = set(historic_listings["id"].tolist())

    new_rental_listings_df = df.query("id not in @historic_ids")

    if not new_rental_listings_df.empty:

        # sort listings
        new_rental_listings_df = new_rental_listings_df.sort_values(by="lastSeenDate")

        df = pd.concat([new_rental_listings_df, historic_listings])

        df.to_csv("data/rental/cleaned/rental_listings.csv", index=False)

        return new_rental_listings_df

    else:
        return new_rental_listings_df


def send_text_message(phone_number, carrier, message) -> None:
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], recipient, message)
    return


def main():
    rental_listings_df = get_rentals()

    csv_path = "data/rental/cleaned/rental_listings.csv"

    if os.path.exists(csv_path):

        new_rental_listings_df = filter_listings(df=rental_listings_df)

        if not new_rental_listings_df.empty:
            top_listings_addresses = new_rental_listings_df["formattedAddress"].tolist()
            rental_prices = new_rental_listings_df["price"].tolist()
            days_on_market = new_rental_listings_df["daysOnMarket"].tolist()
            message = (
                f"Your top listings are- {top_listings_addresses} "
                f"and the rental price is {rental_prices} "
                f"they have been on the market for {days_on_market}"
            )
        else:
            message = "No new listings, will try again next Wednesday."

        send_text_message(phone_number=NUMBER, carrier="mint", message=message)

    else:
        rental_listings_df.to_csv(csv_path, index=False)


if __name__ == "__main__":
    main()
