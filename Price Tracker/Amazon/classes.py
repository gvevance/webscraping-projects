# class definitions

main_url = "http://www.amazon.in"

from bs4 import BeautifulSoup

class search_result :


    def __init__(self,link) :
        self.link = link


    def get_soup(self,session):
        res = session.get(main_url+self.link).text
        soup = BeautifulSoup(res,'lxml')
        return soup


    def extract_title(self,soup):
        return soup.find("span",id="productTitle").text.strip()


    def extract_rating(self,soup):
        
        try :
            rating = soup.find("span",{"data-hook":"rating-out-of-text"}).text
        
        except AttributeError:
            return "Rating not found."
        
        except :
            return "Unknown error in extracting product rating."
        
        return rating


    def extract_price(self,soup):
        
        try :
            price = soup.find("span", class_="a-price a-text-price a-size-medium apexPriceToPay").find("span",class_="a-offscreen").text

        except AttributeError:
            
            try :
                price = soup.find("span", class_="a-price aok-align-center priceToPay").find("span",class_="a-offscreen").text

            except AttributeError :
                return "Price not found."

            except :
                "Unknown error in extracting product price."

        except :
            return "Unknown error in extracting product price."

        return price

    def extract_review_count(self,soup):
        pass


    def extract_deliver_by(self,soup):
        pass


    def extract_product_details(self,soup):
        pass