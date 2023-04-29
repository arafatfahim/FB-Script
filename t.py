from facebook_page_scraper import Facebook_scraper


page_list = ['DailyProthomAlo', 
             'bdnews24', 
             'bd24live', 
             'banglanews24com', 
             'somoynews.tv', 
             'RTVOnline', 
             'Channel24BD', 
             'jamunatv.bd', 
             'ntvbd', 
             'MohonaTV', 
             'Independent24tv', 
             'DhakaTribune', 
             'TheDailyStarBangladesh', 
             'TheDailyIttefaq', 
             'KalerKantho', 
             'SamakalOnline', 
             'Jugantor', 
             'ManabZaminBD', 
             'BangladeshPratidin', 
             'AmaderShomoy.Com', 
             'BonikBarta', 
             'BhorerKagoj', 
             'DailyInqilab', 
             'DailyJanakantha', 
             'DailyNayaDiganta', 
             'DailySangram', 
             'DainikAmadershomoy.Com', 
             'DainikDestiny', 
             'DainikJugantor', 
             'DainikJanata', 
             'DainikManobkantha', 
             'DainikMathabhanga',]


proxy_port = 10001

posts_count = 2
browser = "firefox"

timeout = 600 #600 seconds
headless = False

directory = r"C:\Users\arafat\Documents\GitHub\FB Script\output"

for page in page_list:
    #our proxy for this scrape
    # proxy = f'username:password@us.smartproxy.com:{proxy_port}'
    #initializing a scraper
    scraper = Facebook_scraper(page, posts_count, browser,  timeout=timeout, headless=headless)
    
    filename = page
    scraper.scrap_to_csv(filename, directory)
    
    # Rotating our proxy to the next port so we could get a new IP and avoid blocks
    # proxy_port += 1