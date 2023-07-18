from selenium import webdriver
from bs4 import BeautifulSoup



if __name__ == "__main__":
    # 셀레니움 옵션
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--window-size=800,700")
    options.add_argument("--no-sandbox")
    # 첫번째 리모트 드라이버와 연결
    first_driver = webdriver.Remote("http://chrome1:4444/wd/hub", options=options)
    # 두번째 리모트 드라이버 연결
    second_driver = webdriver.Remote("http://chrome2:4444/wd/hub", options=options)
    # 드라이버를 이용하여 사이트 접속
    first_driver.get("https://www.amazon.com")    
    first_driver.implicitly_wait(5)
    second_driver.get("https://www.amazon.com")
    second_driver.implicitly_wait(5)
    
    
    
    # 드라이버를 이용하여 사이트 접속
    # 드라이버를 이용하여 사이트 소스코드를 불러옴
    first_soup = BeautifulSoup(first_driver.page_source, "html.parser")
    second_soup = BeautifulSoup(second_driver.page_source, "html.parser")
        
    # 불러온 소스코드를 파일로 저장
    open("amazon1.html", "w").write(first_soup.prettify())
    open("amazon2.html", "w").write(second_soup.prettify())
    # 드라이버 종료
    first_driver.quit()
    second_driver.quit()
    
    