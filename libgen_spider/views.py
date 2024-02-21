from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Book, Author, SearchedKeyword, Results

# Create your views here.
def scrape_website(request):
    if request.method == 'POST':
        # Get the search query from the form
        searched_query = request.POST.get('req', '')
        # https://libgen.is/search.php?req=art
        # URL to scrape with the search query
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }
        bookList = list()
        for page in range(1, 6):
            url = f'https://libgen.is/search.php?req={searched_query}'

            # Make a GET request to the URL
            response = requests.get(url, headers=headers)

            # Check if request was successful
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.content, 'html.parser')
                # Extracting the intended data
                table = soup.find('table')
                books = table.find_all('tr')
                if len(books) < 2:
                    return render(request, 'libgen_spider/error.html', {'message': 'No data found'})
        
            else:
                return render(request, 'libgen_spider/error.html')
        # # Pass the data to the template
    else:
        return render(request, 'libgen_spider/search.html')
