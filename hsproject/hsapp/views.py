from django.shortcuts import render
import requests
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import time

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")




def market(request):

    ticker = "NIFTY_50"

    url = f"https://www.google.com/finance/quote/{ticker}:INDEXNSE"

    # ✅ Add headers (VERY IMPORTANT)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    # ✅ Check response
    print(response.status_code)   # should be 200
    print(response.text[:500])    # preview HTML

    # ✅ Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Try to find price
    price = soup.find("div", class_="YMlKec fxKbKc")
    change = soup.find("div", class_="JwB6zf")

    print("Price:", price.text if price else "Not found")
    print("Change:", change.text if change else "Not found")
    return render(request, "market.html", 
        {"price_": price,
        "change": change})

def abc(request):
    all="chetan"
    print(all)
    return render(request,"abc.html",{"data":all})

