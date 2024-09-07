import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
from urls import urls


def get_article_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    headline = soup.find("h1").get_text()

    pane_content = soup.find("div", class_="pb-20 clearfix")
    paragraphs = pane_content.find_all("p")

    body_text = " ".join([paragraph.get_text() for paragraph in paragraphs])

    print("Headline:", headline)

    return headline, body_text


def main():
    with open("articles_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["headline", "body"])  # Write the header

        # Loop through each URL and extract content
        for url in tqdm(urls, desc="Processing URLs"):
            headline, body_text = get_article_text(url)
            writer.writerow([headline, body_text])  # Save the data
            print("\n")

        print("Data saved to articles_data.csv")


if __name__ == "__main__":
    main()
