import requests
from bs4 import BeautifulSoup

# the input file containing article links
input_file = "article_links.txt"

# the counter for the output file number
output_file_count = 81

# loop through all the article links in the input file
with open(input_file, "r", errors='ignore') as f:
    for article_url in f:
        # remove any whitespace characters such as newlines
        article_url = article_url.strip()
        print(output_file_count, article_url)
        # request the article content using the link
        response = requests.get(article_url)

        # extract the article content using beautifulsoup
        soup = BeautifulSoup(response.content, "html.parser")
        article_text = soup.get_text()

        # write the extracted article text to a new output file
        output_file_name = str(output_file_count) + ".txt"
        with open(output_file_name, "w", encoding='utf-8') as out_f:
            out_f.write(article_text)

        # increment the output file counter
        output_file_count += 1
