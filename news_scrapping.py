import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components

def scrape_news(query):
    url = f"https://news.google.com/rss/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    news_items = soup.find_all('item')
    articles = []
    for item in news_items:
        title = item.title.text
        description = item.description.text
        link = item.link.text
        articles.append({'title': title, 'link': description})
    return articles

# Main function
def main():
    st.title("News Scraper")
    
    # Get the URL from the user
    url = st.text_input("Enter The News Query") + " News in India"
    
    if st.button("Scrape"):
        # Scrape the news data
        df = scrape_news(url)
        
        # Display the scraped data
    
        def display_link_with_icon(link):
            st.markdown(f'{link}', unsafe_allow_html=True)

        # Display the scraped data
        for article in df:
            title = article['title']
            link = article['link']
            display_link_with_icon(link)

        # Save the data to a CSV file
        df.to_csv('news_data.csv', index=False)
        st.success("Data scraped and saved to news_data.csv")

# Run the main function
if __name__ == '__main__':
    main()