import requests
import smtplib

def main():
	code = get_html() #get html from page
	
	exchange = find_between(code, "<a href='/graph/?from=USD&amp;to=EUR'>", "</a>" )
	
	print(exchange.encode('utf-8')) #print
	
def get_html():
	url = 'http://www.x-rates.com/table/?from=USD&amount=1'
	response = requests.get(url)
	return response.text
		
def find_between( s, first, last ):
		try:
			start = s.index( first ) + len( first )
			end = s.index( last, start )
			return s[start:end]
		except ValueError:
			return ""

if __name__ == '__main__':
    main()