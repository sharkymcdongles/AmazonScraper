import bs4, requests, sys

def getAmazonPrice(productURL):


    if 'amazon.de' not in productURL: # check URL
        print("The Product URL must be from amazon.de") 
    else:
            
        res = requests.get(productURL) # get html
        res.raise_for_status() # check if error
        soup = bs4.BeautifulSoup(res.text, "html.parser") # parse html
        rawProductName = soup.select("#productTitle") # grab item name
        rawPrice = soup.select("#priceblock_ourprice") # grab block
        finalProductName = rawProductName[0].text.strip()
        finalPrice = rawPrice[0].text.strip("EUR ")+'€' # strip price

        print("The current price for: " + finalProductName + " is: " + finalPrice) # print price

sys.argv # get args

if len(sys.argv) > 1: # check args
    productURL = ' '.join(sys.argv[1:])
    
getAmazonPrice(productURL) # run program
