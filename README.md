# Amazon Scraper

A Python/Django web scraper to scrape sponsored search results from Amazon.co.uk, store the results in a database, and expose the data through an Django-rest API.

## Requirements

- Python 3.7 or higher
- Django 3.2 or higher
- Django Rest Framework 3.12 or higher
- BeautifulSoup4 4.9 or higher
- Requests 2.25 or higher

## Installation

1. Clone the repository:
```
git clone https://github.com/ritik2209/amazon_scraper_project.git
cd amazon_scraper_project
```

2. Create a virtual environment and install the requirements:

``` 
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Apply the database migrations:
```
python manage.py makemigrations
python manage.py migrate`
```

4. Create a superuser to access the Django Admin:
```python manage.py createsuperuser```

5. Run the development server:
```python manage.py runserver ```



## Usage
### Django Admin

Access the Django Admin at http://127.0.0.1:8000/admin/ to add or remove keywords for the scraper.

### API

The project provides the following API endpoints:

    List/Search Search Results:
        URL: /api/search_results/
        Method: GET
        Query Parameters:
            keyword (optional): Filter search results by keyword.
            date (optional): Filter search results by date (format: YYYY-MM-DD).

    Trigger Scraper:
        URL: /api/trigger_scraper/
        Method: GET



