from django.urls import path
from .views import SearchResultList, trigger_scraper

urlpatterns = [
    path('api/search_results/', SearchResultList.as_view(), name='search-result-list'), #endpoint for scrape results 
    path('api/trigger_scraper/', trigger_scraper, name='trigger-scraper'), #endpoint for trigerring scraper
]

