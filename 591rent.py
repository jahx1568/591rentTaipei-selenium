import requests
from selenium import webdriver
import time

def ChooseNum(text, num):
    while(True):
        try:
            chose = int(input("輸入對應的{s}:".format(s= text))) - 1
    
            if chose not in range(num):
                print("請重新輸入\n")
            else:
                break
        except:
            print("請重新輸入\n")
            pass
    return chose
def ChooseMultiple(num):
    Area=[]
    while(True):
        try:
            A = int(input("輸入對應的區域數字(可複選,不選時輸入數字0):"))
            
            if A not in range(num):
                continue
            elif A == 0:
                break
        except:
            print("請重新輸入\n")
            pass
                
        Area.append(A-1)
    return Area

print("1:北部, 2:中部, 3:南部, 4:東部")
print("EX:要東部輸入4")

position = ChooseNum(text = "方位", num = 4)
    
    
if position == 0:
    print("\n1:台北市, 2:新北市, 3:桃園市, 4:新竹市, 5:新竹縣, 6:基隆市, 7:宜蘭縣")
    city = ChooseNum(text = "城市數字", num = 7)
    if city == 0:
        print("\n1:中山區, 2:大安區, 3:信義區, 4:士林區, 5:內湖區, 6:中正區, 7:松山區, 8:萬華區")
        print("9:萬華區, 10:大同區, 11:文山區, 12:北投區, 13:南港區")
        print("可複選,不選時輸入數字0")
        Area = ChooseMultiple(14)
    elif city == 1:
        print("\n1:板橋區, 2:三重區, 3:淡水區, 4:中和區, 5:新莊區, 6:永和區, 7:新店區, 8:汐止區")
        print("9:蘆洲區, 10:林口區, 11:三峽區, 12:土城區, 13:樹林區, 14:泰山區, 15:五股區, 16:鶯歌區")
        print("17:深坑區, 18:八里區")
        print("可複選,不選時輸入數字0")
        Area = ChooseMultiple(18)
    elif city == 2:
        print("\n1:桃園區, 2:中壢區, 3:蘆竹區, 4:龜山區, 5:八德區, 6:平鎮區, 7:大園區, 8:楊梅區")
        print("9:龍潭區, 10:觀音區, 11:大溪區, 12:新屋區, 13:復興區")
        print("可複選,不選時輸入數字0")
        Area = ChooseMultiple(13)
    elif city == 3:
        print("\n1:東區, 2:北區, 3:香山區")
        print("可複選,不選時輸入數字0")
        Area = ChooseMultiple(3)
    elif city == 4:
        print("\n1:竹北市, 2:湖口鄉, 3:新豐鄉, 4:竹東鎮, 5:寶山鄉, 6:新埔鎮, 7:芎林鄉, 8:關西鎮")
        print("9:北埔鄉, 10:橫山鄉, 11:五峰鄉, 12:尖石鄉, 13:峨嵋鄉")
        print("可複選,不選時輸入數字0")
        Area = ChooseMultiple(13)
    elif city == 5:
        print("\n1:中正區, 2:仁愛區, 3:安樂區, 4:信義區, 5:中山區, 6:七堵區, 7:暖暖區")
        print("可複選,不選時輸入數字0")
        Area = ChooseMultiple(7)
    elif city == 6:
        print("\n1:宜蘭市, 2:羅東鎮, 3:礁溪鄉, 4:頭城鎮, 5:蘇澳鎮, 6:冬山鄉, 7:五結鄉, 8:三星鄉")
        print("9:狀元鄉, 10:員山鄉, 11:大同鄉, 12:南澳鄉")
        print("可複選,不選時輸入數字0")
        Area = ChooseMultiple(12)
        
elif position == 1:
    print("\n1:台中市, 2:彰化縣, 3:苗栗縣, 4:雲林縣, 5:南投縣")
    city = ChooseNum(text = "城市數字", num = 5)
            
elif position == 2:
    print("\n1:高雄市, 2:台南市, 3:嘉義市, 4:屏東縣, 5:嘉義縣")
    city = ChooseNum(text = "城市數字", num = 5)
            
elif position == 3:
    print("\n1:花蓮縣, 2:台東縣, 3:金門縣, 4:澎湖縣, 5:連江縣")
    city = ChooseNum(text = "城市數字", num = 5)


print("\n1:不限, 2:整層住家, 3:獨立套房, 4:分租套房, 5:雅房, 6:車位")
Hometype = ChooseNum(text="類型", num=6)

try:
    PriceMin = int(input("輸入您期望的最低金額:"))
except:
    print("請重新輸入\n")
    pass

try:
    PriceMax = int(input("輸入您期望的最高金額:"))
except:
    print("請重新輸入\n")
    pass

print("\n1:一房, 2:二房, 3:三房, 4:四房, 5:五房以上")
Pattern = ChooseNum(text="房型", num=5)
try:
    PlainMin = int(input("輸入您期望的最小坪數:"))
except:
    print("請重新輸入\n")
    pass

try:
    PlainMax = int(input("輸入您期望的最大坪數:"))
except:
    print("請重新輸入\n")
    pass


driver = webdriver.Chrome()

driver.get("https://rent.591.com.tw/?kind=0&region=1")
try:
    click_close = driver.find_element_by_id("area-box-close")
    click_close.click()
except:
    pass

ChooseLoaction = driver.find_element_by_xpath("//div[@id='search-location']/span[contains(@data-index,'1')]")
ChooseLoaction.click()

ChooseCity = driver.find_element_by_id("optionBox").find_elements_by_tag_name('dl')
ChooseCity[position].find_elements_by_tag_name('li')[city].click()

time.sleep(1)

ChooseArea = driver.find_element_by_id("optionBox").find_elements_by_tag_name('li')
for i in Area:
    ChooseArea[i].click() #板橋

HomeType = driver.find_element_by_id("search-kind").find_element_by_css_selector("[data-index='{index}']".format(index=
                                                                                                                 Hometype))
HomeType.click()

driver.find_element_by_id("rentPrice-min").send_keys('{minn}'.format(minn=PriceMin))
driver.find_element_by_id("rentPrice-max").send_keys('{maxx}'.format(maxx=PriceMax))


driver.find_element_by_id("search-pattern").find_element_by_css_selector("[data-index='{index}']".format(index=Pattern)).click()

driver.find_element_by_id("plain-min").send_keys('{Min}'.format(Min=PlainMin))
driver.find_element_by_id("plain-max").send_keys('{Max}'.format(Max=PlainMax))

time.sleep(3)
for num in driver.find_element_by_class_name("listBox").find_elements_by_class_name("j-house"):
    title = num.find_element_by_class_name("infoContent")
    price = num.find_element_by_class_name("price")
    url_house = title.find_element_by_tag_name("a").get_attribute("href")
    print("標題:{title}, 價格:{price}, 網址:{url}\n".format(title=title.text, price=price.text, url=url_house))
