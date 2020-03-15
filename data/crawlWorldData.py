import requests
import re
from bs4 import BeautifulSoup
import json

print("#####################################")
print("############ 세계 데이터 #############")
print("######## worldData.js #########")

html = requests.get("https://www.worldometers.info/coronavirus/").text
# print(html) 작동확인 1
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select('#main_table_countries > tbody > tr')
# print(datas) 작동확인 2
기존데이터 = [{
    "Name": "이란",
    "Name_en": "Iran",
    "Name_ch": "伊朗",
    "lat": 35.6970118,
    "lng": 51.2097373,
    "확진자수": 4747,
    "사망자수": 124,
    "완치자수": 913,
    "추가날짜": "2/21"
  }, {
    "Name": "이집트",
    "Name_en": "Egypt",
    "Name_ch": "埃及",
    "lat": 30.0594838,
    "lng": 31.2234448,
    "확진자수": 15,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "2/16"
  }, {
    "Name": "루마니아",
    "Name_en": "Romania",
    "Name_ch": "尼亚",
    "lat": 44.430481,
    "lng": 26.12298,
    "확진자수": 11,
    "사망자수": 0,
    "완치자수": 5,
    "추가날짜": "3/6"
  }, {
    "Name": "벨기에",
    "Name_en": "Belgium",
    "Name_ch": "比利时",
    "lat": 50.8550625,
    "lng": 4.3053503,
    "확진자수": 169,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "2/5"
  }, {
    "Name": "벨라루스",
    "Name_en": "Belarus",
    "Name_ch": "白俄罗斯",
    "lat": 53,
    "lng": 28,
    "확진자수": 6,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "3/6"
  }, {
    "Name": "스페인",
    "Name_en": "Spain",
    "Name_ch": "西班牙",
    "lat": 40.4378698,
    "lng": -3.8196189,
    "확진자수": 401,
    "사망자수": 8,
    "완치자수": 245,
    "추가날짜": "2/2"
  }, {
    "Name": "스웨덴",
    "Name_en": "Sweden",
    "Name_ch": "瑞典语",
    "lat": 59.3260668,
    "lng": 17.8419725,
    "확진자수": 161,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "2/2"
  }, {
    "Name": "덴마크",
    "Name_en": "Denmark",
    "Name_ch": "丹麦",
    "lat": 56.26392,
    "lng": 9.501785,
    "확진자수": 27,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "2/2"
  }, {
    "Name": "노르웨이",
    "Name_en": "Norway",
    "Name_ch": "挪威",
    "lat": 59.9138204,
    "lng": 10.7387413,
    "확진자수": 127,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "3/6"
  }, {
    "Name": "이탈리아",
    "Name_en": "Italy",
    "Name_ch": "义大利",
    "lat": 41.902782,
    "lng": 12.496366,
    "확진자수": 4636,
    "사망자수": 197,
    "완치자수": 913,
    "추가날짜": "2/1"
  },{
    "Name": "아제르바이잔",
    "Name_en": "Azerbaijan",
    "Name_ch": "阿塞拜疆",
    "lat": 40.3,
    "lng": 47.3,
    "확진자수": 9,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "3/6"
  }, {
    "Name": "러시아",
    "Name_en": "Russia",
    "Name_ch": "俄罗斯",
    "lat": 55.751244,
    "lng": 37.618423,
    "확진자수": 13,
    "사망자수": 0,
    "완치자수": 2,
    "추가날짜": "2/1"
  },{
    "Name": "파키스탄",
    "Name_en": "Pakistan",
    "Name_ch": "巴基斯坦",
    "lat": 30.37,
    "lng": 69.34,
    "확진자수": 6,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "3/6"
  }, {
    "Name": "캐나다",
    "Name_en": "Canada",
    "Name_ch": "加拿大",
    "lat": 54.7235693,
    "lng": -113.7164202,
    "확진자수": 54,
    "사망자수": 0,
    "완치자수": 8
  }, {
    "Name": "미국",
    "Name_en": "USA",
    "Name_ch": "美国",
    "lat": 37.2757368,
    "lng": -104.6549972,
    "확진자수": 321,
    "사망자수": 15,
    "완치자수": 15
  }, {
    "Name": "핀란드",
    "Name_en": "Finland",
    "Name_ch": "芬兰",
    "lat": 60.1102086,
    "lng": 24.7378224,
    "확진자수": 15,
    "사망자수": 0,
    "완치자수": 1
  },{
    "Name": "체코",
    "Name_en": "Czechia",
    "Name_ch": "捷克",
    "lat": 50.083,
    "lng": 14.417,
    "확진자수": 19,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜" : "3/6"
  }, {
    "Name": "프랑스",
    "Name_en": "France",
    "Name_ch": "法国",
    "lat": 46.1390503,
    "lng": -2.4346589,
    "확진자수": 716,
    "사망자수": 11,
    "완치자수": 12
  }, {
    "Name": "영국",
    "Name_en": "UK",
    "Name_ch": "英国",
    "lat": 51.509865,
    "lng": -0.118092,
    "확진자수": 206,
    "사망자수": 2,
    "완치자수": 18,
    "추가날짜": "2/1"
  }, {
    "Name": "네덜란드",
    "Name_en": "Netherlands",
    "Name_ch": "荷兰",
    "lat": 52.132633,
    "lng": 5.291266,
    "확진자수": 188,
    "사망자수": 1,
    "완치자수": 0,
    "추가날짜": "3/6"
  }, {
    "Name": "네팔",
    "Name_en": "Nepal",
    "Name_ch": "尼泊尔",
    "lat": 28.3838445,
    "lng": 81.8867804,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 1
  },{
    "Name": "팔레스타인",
    "Name_en": "Palestine",
    "Name_ch": "巴勒斯坦",
    "lat": 31.89,
    "lng": 34.9,
    "확진자수": 16,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  }, {
    "Name": "마카오",
    "Name_en": "Macao",
    "Name_ch": "澳门",
    "lat": 22.1619078,
    "lng": 113.5351333,
    "확진자수": 10,
    "사망자수": 0,
    "완치자수": 9
  }, {
    "Name": "홍콩",
    "Name_en": "Hong Kong",
    "Name_ch": "香港",
    "lat": 22.3529808,
    "lng": 113.9876162,
    "확진자수": 107,
    "사망자수": 2,
    "완치자수": 51
  }, {
    "Name": "태국",
    "Name_en": "Thailand",
    "Name_ch": "泰国",
    "lat": 13.0110763,
    "lng": 96.9952628,
    "확진자수": 48,
    "사망자수": 1,
    "완치자수": 31
  }, {
    "Name": "호주",
    "Name_en": "Australia",
    "Name_ch": "澳大利亚",
    "lat": -24.9936027,
    "lng": 115.2351577,
    "확진자수": 64,
    "사망자수": 2,
    "완치자수": 22
  }, {
    "Name": "싱가포르",
    "Name_en": "Singapore",
    "Name_ch": "新加坡",
    "lat": 1.3143394,
    "lng": 103.7041659,
    "확진자수": 138,
    "사망자수": 0,
    "완치자수": 90
  },{
    "Name": "포르투갈",
    "Name_en": "Portugal",
    "Name_ch": "葡萄牙",
    "lat": 39.399872,
    "lng": -8.224454,
    "확진자수": 13,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜" : "3/6"
  },{
    "Name": "조지아",
    "Name_en": "Georgia",
    "Name_ch": "格鲁吉亚",
    "lat": 41.7109,
    "lng": 44.7919,
    "확진자수": 9,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜" : "3/6"
  }, {
    "Name": "레바논",
    "Name_en": "Lebanon",
    "Name_ch": "黎巴嫩",
    "lat": 33.8869444,
    "lng": 35.5130556,
    "확진자수": 22,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "2/23"
  }, {
    "Name": "이스라엘",
    "Name_en": "Israel",
    "Name_ch": "以色列",
    "lat": 31.4117257,
    "lng": 35.0818155,
    "확진자수": 21,
    "사망자수": 0,
    "완치자수": 2,
    "추가날짜": "2/23"
  }, {
    "Name": "에스토니아",
    "Name_en": "Estonia",
    "Name_ch": "爱沙尼亚",
    "lat": 59,
    "lng": 26,
    "확진자수": 9,
    "사망자수": 0,
    "완치자수": 5,
    "추가날짜": "3/6"
  }, {
    "Name": "말레이시아",
    "Name_en": "Malaysia",
    "Name_ch": "马来西亚",
    "lat": 4.1389178,
    "lng": 105.1226078,
    "확진자수": 83,
    "사망자수": 0,
    "완치자수": 23
  }, {
    "Name": "캄보디아",
    "Name_en": "Cambodia",
    "Name_ch": "柬埔寨",
    "lat": 12.1458696,
    "lng": 103.8594161,
    "확진자수": 2,
    "사망자수": 0,
    "완치자수": 1
  }, {
    "Name": "베트남",
    "Name_en": "Vietnam",
    "Name_ch": "越南",
    "lat": 15.7583637,
    "lng": 101.4157502,
    "확진자수": 20,
    "사망자수": 0,
    "완치자수": 16
  }, {
    "Name": "필리핀",
    "Name_en": "Philippines",
    "Name_ch": "菲律宾",
    "lat": 14.5965787,
    "lng": 120.9444545,
    "확진자수": 5,
    "사망자수": 1,
    "완치자수": 2
  }, {
    "Name": "대만",
    "Name_en": "Taiwan",
    "Name_ch": "台湾",
    "lat": 25.0174719,
    "lng": 121.3662943,
    "확진자수": 45,
    "사망자수": 1,
    "완치자수": 12
  }, {
    "Name": "스리랑카",
    "Name_en": "Sri Lanka",
    "Name_ch": "斯里兰卡",
    "lat": 7.8589214,
    "lng": 79.5850432,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 1
  },{
    "Name": "카타르",
    "Name_en": "Qatar",
    "Name_ch": "卡塔尔",
    "lat": 25.35,
    "lng": 51.18,
    "확진자수": 11,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "사우디아라비아",
    "Name_en": "Saudi Arabia",
    "Name_ch": "沙特阿拉伯",
    "lat": 23.89,
    "lng": 45.08,
    "확진자수": 7,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜":"3/6"
  },{
    "Name": "버진아일랜드",
    "Name_en": "Virgin Islands",
    "Name_ch": "维尔京群岛",
    "lat": 18.2,
    "lng": -64.5,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/7"
  },{
    "Name": "인도네시아",
    "Name_en": "Indonesia",
    "Name_ch": "印度尼西亚",
    "lat": -6.211544,
    "lng": 106.845172,
    "확진자수": 4,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "뉴질랜드",
    "Name_en": "NewZealand",
    "Name_ch": "新西兰",
    "lat": -41.28648,
    "lng": 174.776217,
    "확진자수": 5,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "아르헨티나",
    "Name_en": "Argentine",
    "Name_ch": "阿根廷",
    "lat": -34,
    "lng": -64,
    "확진자수": 8,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "보스니아 헤르체고비나",
    "Name_en": "Bosnia and Herzegovina",
    "Name_ch": "波斯尼亚和黑塞哥维那",
    "lat": 43.915886,
    "lng": 17.679076,
    "확진자수": 3,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "마케도니아",
    "Name_en": "Macedonia",
    "Name_ch": "马其顿",
    "lat": 41.9617,
    "lng": 21.6214,
    "확진자수": 3,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "나이지리아",
    "Name_en": "Nigeria",
    "Name_ch": "尼日利亚",
    "lat": 9.05735,
    "lng": 7.48976,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "리투아니아",
    "Name_en": "Lithania",
    "Name_ch": "立陶宛",
    "lat": 55.17,
    "lng": 23.88,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "룩셈부르크",
    "Name_en": "Luxembourg",
    "Name_ch": "卢森堡",
    "lat": 47.162494,
    "lng": 19.503304,
    "확진자수": 3,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "모로코",
    "Name_en": "Morocco",
    "Name_ch": "摩洛哥",
    "lat": -7.09262,
    "lng": 31.791702,
    "확진자수": 2,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "모나코",
    "Name_en": "Monaco",
    "Name_ch": "摩纳哥",
    "lat": 43.750298,
    "lng": 7.412841,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "아르메니아",
    "Name_en": "Armenia",
    "Name_ch": "亚美尼亚",
    "lat": 40.07,
    "lng": 45.04,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "도미니카 공화국",
    "Name_en": "Dominican Republic",
    "Name_ch": "多明尼加共和国",
    "lat": 	18.74,
    "lng":  -70.16,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "카메룬",
    "Name_en": "Cameroon",
    "Name_ch": "喀麦隆",
    "lat": 	7.369722,
    "lng":  12.354722,
    "확진자수": 2,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/7"
  },{
    "Name": "토고",
    "Name_en": "Togo",
    "Name_ch": "多哥",
    "lat": 	8.4,
    "lng":  1.460,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/7"
  },{
    "Name": "콜롬비아",
    "Name_en": "Colombia",
    "Name_ch": "哥伦比亚",
    "lat": 	4.6,
    "lng": -74.0833,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/7"
  },{
    "Name": "바티칸 시국",
    "Name_en": "Vatican City State",
    "Name_ch": "梵蒂冈市国",
    "lat": 	41.54,
    "lng":  12.27,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/7"
  },{
    "Name": "페루",
    "Name_en": "Peru",
    "Name_ch": "秘鲁",
    "lat": 	-9.189967,
    "lng":  -75.015152,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/7"
  },{
    "Name": "요르단",
    "Name_en": "Jordan",
    "Name_ch": "约旦",
    "lat": 	31,
    "lng":  36,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "라트비아",
    "Name_en": "Latvia",
    "Name_ch": "约旦",
    "lat": 56.946,
    "lng": 24.10589,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜":"3/6"
  },{
    "Name": "안도라",
    "Name_en": "Andorra",
    "Name_ch": "安道尔",
    "lat": 42.33,
    "lng": 1.34,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "튀니지",
    "Name_en": "Tunisie",
    "Name_ch": "突尼斯",
    "lat": 34,
    "lng": 9,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "우크라이나",
    "Name_en": "Ukraina",
    "Name_ch": "乌克兰",
    "lat": 48.379433,
    "lng": 31.16558,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "리히텐슈타인",
    "Name_en": "Liechtenstein",
    "Name_ch": "列支敦士登",
    "lat": 47.16,
    "lng": 9.32,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "폴란드",
    "Name_en": "Poland",
    "Name_ch": "波兰",
    "lat": 52,
    "lng": 20,
    "확진자수": 6,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "페로 제도",
    "Name_en": "Faroe Islands",
    "Name_ch": "法罗群岛",
    "lat": 62,
    "lng": -7,
    "확진자수": 2,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "남아프리카 공화국",
    "Name_en": "South Africa",
    "Name_ch": "南非共和国",
    "lat": 29,
    "lng": 24,
    "확진자수": 2,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "코스타리카",
    "Name_en": "Costa Rica",
    "Name_ch": "哥斯达黎加",
    "lat": 9.75,
    "lng": -83.75,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "지브롤터",
    "Name_en": "Gibraltar",
    "Name_ch": "直布罗陀",
    "lat": 36.8,
    "lng": -5.21,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "부탄",
    "Name_en": "Bhutan",
    "Name_ch": "不丹",
    "lat": 27.3,
    "lng": 90.3,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "세르비아",
    "Name_en": "Serbia",
    "Name_ch": "塞尔维亚",
    "lat": 43.57,
    "lng": 21.41,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "세네갈",
    "Name_en": "Senegal",
    "Name_ch": "塞内加尔",
    "lat": 14.497401,
    "lng": -14.452362,
    "확진자수": 4,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜":"3/6"
  },{
    "Name": "칠레",
    "Name_en": "Chile",
    "Name_ch": "智利",
    "lat": -33.45,
    "lng": -70.6667,
    "확진자수": 5,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  },{
    "Name": "헝가리",
    "Name_en": "Hungary",
    "Name_ch": "匈牙利",
    "lat": 47.162494,
    "lng": 19.503304,
    "확진자수": 4,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜":"3/6"
  }, {
    "Name": "독일",
    "Name_en": "Germany",
    "Name_ch": "德国",
    "lat": 51.0968735,
    "lng": 5.9694438,
    "확진자수": 670,
    "사망자수": 0,
    "완치자수": 18
  }, {
    "Name": "인도",
    "Name_en": "India",
    "Name_ch": "印度",
    "lat": 28.5274228,
    "lng": 77.1387735,
    "확진자수": 34,
    "사망자수": 0,
    "완치자수": 3
  }, {
    "Name": "아랍에미리트",
    "Name_en": "UAE",
    "Name_ch": "阿拉伯联合酋长国",
    "lat": 24.3870789,
    "lng": 54.4185368,
    "확진자수": 45,
    "사망자수": 0,
    "완치자수": 23
  }, {
    "Name": "중국",
    "Name_en": "China",
    "Name_ch": "中国",
    "lat": 39.9385466,
    "lng": 116.117281,
    "확진자수": 80652,
    "사망자수": 3070,
    "완치자수": 55521
  }, {
    "Name": "일본",
    "Name_en": "Japan",
    "Name_ch": "日本",
    "lat": 34.6777642,
    "lng": 135.4160247,
    "확진자수": 420,
    "사망자수": 6,
    "완치자수": 76
  }, {
    "Name": "일본크루즈",
    "Name_en": "Diamond Princess",
    "Name_ch": "日本 邮轮",
    "lat": 34.6777642,
    "lng": 135.4160247,
    "확진자수": 705,
    "사망자수": 7,
    "완치자수": 245
  },
  {
    "Name": "쿠웨이트",
    "Name_en": "Kuwait",
    "Name_ch": "科威特",
    "lat": 29.376150,
    "lng": 47.977308,
    "확진자수": 58,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "2/25"
  },
  {
    "Name": "이라크",
    "Name_en": "Iraq",
    "Name_ch": "伊拉克",
    "lat": 33.294967,
    "lng": 44.364783,
    "확진자수": 48,
    "사망자수": 4,
    "완치자수": 1,
    "추가날짜": "2/25"
  },
  {
    "Name": "바레인",
    "Name_en": "Bahrain",
    "Name_ch": "巴林",
    "lat": 34.561213,
    "lng": 69.210980,
    "확진자수": 66,
    "사망자수": 0,
    "완치자수": 4,
    "추가날짜": "2/25"
  },
  {
    "Name": "오만",
    "Name_en": "Oman",
    "Name_ch": "阿曼",
    "lat": 23.577151,
    "lng": 58.371409,
    "확진자수": 16,
    "사망자수": 0,
    "완치자수": 2,
    "추가날짜": "2/25"
  },
  {
    "Name": "오스트리아",
    "Name_en": "Austria",
    "Name_ch": "奥地利",
    "lat": 48.220599,
    "lng": 16.239634,
    "확진자수": 66,
    "사망자수": 0,
    "완치자수": 2,
    "추가날짜": "2/26"
  },
  {
    "Name": "아이슬란드",
    "Name_en": "Ireland",
    "Name_ch": "爱尔兰",
    "lat": 53.3331,
    "lng": -6.2489,
    "확진자수": 18,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "3/7"
  },
  {
    "Name": "아일랜드",
    "Name_en": "Ireland",
    "Name_ch": "冰岛",
    "lat": 64.963051,
    "lng": -19.020835,
    "확진자수": 45,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "3/6"
  },
  {
    "Name": "슬로베니아",
    "Name_en": "Slovenia",
    "Name_ch": "斯洛文尼亚",
    "lat": 64.963051,
    "lng": -19.020835,
    "확진자수": 12,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "3/6"
  },
  {
    "Name": "슬로바키아",
    "Name_en": "Slovakia",
    "Name_ch": "斯洛伐克",
    "lat": 48.4,
    "lng": 19.3,
    "확진자수": 1,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "3/6"
  },
  {
    "Name": "그리스",
    "Name_en": "Greece",
    "Name_ch": "希腊",
    "lat": 37.97945,
    "lng": 23.71622,
    "확진자수": 45,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "3/6"
  },
  {
    "Name": "아프가니스탄",
    "Name_en": "Afghanistan",
    "Name_ch": "阿富汗",
    "lat": 26.225355,
    "lng": 50.580098,
    "확진자수": 3,
    "사망자수": 1,
    "완치자수": 2,
    "추가날짜": "2/25"
  },
  {
    "Name": "알제리",
    "Name_en": "Algeria",
    "Name_ch": "阿尔及利亚",
    "lat": 36.722930,
    "lng": 3.0595322,
    "확진자수": 17,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "2/26"
  },
  {
    "Name": "크로아티아",
    "Name_en": "Croatia",
    "Name_ch": "克罗地亚",
    "lat": 45.809237,
    "lng": 15.817735,
    "확진자수": 11,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "2/26"
  },
  {
    "Name": "스위스",
    "Name_en": "Switzerland",
    "Name_ch": "瑞士",
    "lat": 46.945735,
    "lng": 7.3077371,
    "확진자수": 268,
    "사망자수": 1,
    "완치자수": 3,
    "추가날짜": "2/26"
  },
  {
    "Name": "브라질",
    "Name_en": "Brazil",
    "Name_ch": "巴西",
    "lat": -15.775082,
    "lng": -48.077963,
    "확진자수": 13,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "2/26"
  },
  {
    "Name": "산마리노",
    "Name_en": "San Marino",
    "Name_ch": "圣马力诺",
    "lat": 43.9810089,
    "lng": 12.4896372,
    "확진자수": 23,
    "사망자수": 1,
    "완치자수": 0,
    "추가날짜": "3/6"
  },
  {
    "Name": "에콰도르",
    "Name_en": "Ecuador",
    "Name_ch": "厄瓜多尔",
    "lat": -1.831239,
    "lng": -78.183406,
    "확진자수": 13,
    "사망자수": 0,
    "완치자수": 0,
    "추가날짜": "3/6"
  },
  {
    "Name": "멕시코",
    "Name_en": "Mexico",
    "Name_ch": "墨西哥",
    "lat": 19.4978,
    "lng": -99.1269,
    "확진자수": 6,
    "사망자수": 0,
    "완치자수": 1,
    "추가날짜": "3/6"
  },
  {
    "Name": "한국",
    "Name_en": "Korea, Republic of",
    "Name_ch": "韩国",
    "lat": 37.5456299,
    "lng": 126.9540667,
    "확진자수": 7134,
    "사망자수": 50,
    "격리자수": 6605,
    "완치자수": 118,
    "검사진행": 19620
  },
  {
    "Name": "제주",
    "Name_en": "Jeju",
    "Name_ch": "濟州",
    "lat": 33.50972,
    "lng": 126.52194,
    "확진자수": 4,
    "사망자수": 0,
    "격리자수": 0,
    "완치자수": 0,
    "검사진행": 60
  }
]
세계확진자 = []

for d in datas:
    국가이름 = d.find_all('td')[0].text
    if 국가이름.strip() == 'S. Korea':
        continue
    확진자 = d.find_all('td')[1].text
    사망자 = d.find_all('td')[3].text
    완치자 = d.find_all('td')[5].text
    # print(f'국가이름 : {국가이름}')
    # print(f'확진자 : {확진자}')
    # print(f'사망자 : {사망자}')
    # print(f'완치자 : {완치자}')

    한국어이름 = ''
    name_ch = ''

    for value in 기존데이터:
        if value['Name_en'] == 국가이름.strip():
            한국어이름 = value['Name']
            name_ch = value['Name_ch']

    #지도 SVG 이름 동기화(아래 USA는 크롤링된 영어이름)
    if 국가이름.strip() == 'USA':
        #여기에 SVG파일에 있는 국가명으로 변경
        국가이름 = 'United States'

    #잘못된 영어이름 수정
    if 국가이름.strip() == 'USA':
        #여기에 SVG파일에 있는 국가명으로 변경
        국가이름 = 'United States'

    if 국가이름.strip() == 'Total:':
      print("Skipping total")
      continue


    #한국어 이름이 필드에 없을 경우 영어이름 삽입
    if 한국어이름 == '':
        한국어이름 = 국가이름.strip()

    세계확진자.append({
        'Name' : 한국어이름,
        'Name_ch' : name_ch,
        'Name_en' : 국가이름.strip(),
        '확진자수' : int(0 if 확진자.strip().replace(',', '') == "" else 확진자.strip().replace(',', '')),
        '사망자수' : int(0 if 사망자.strip().replace(',', '') == "" else 사망자.strip().replace(',', '')),
        '완치자수' : int(0 if 완치자.strip().replace(',', '') == "" else 완치자.strip().replace(',', '')),
    })

with open("./data/worldData.js", "w", encoding='UTF-8-sig') as json_file:
    json.dump(세계확진자, json_file, ensure_ascii=False, indent=4)
    # file.write(json.dumps(dict, ensure_ascii=False))

data = ''
with open("./data/worldData.js", "r", encoding='UTF-8-sig') as f:
    while True:
        line = f.readline()
        if not line: break
        data += line
data = '//Auto-generated by crawlWorldData.py\nvar marker = ' + data + ';'

with open("./data/worldData.js", "w", encoding='UTF-8-sig') as f_write:
    f_write.write(data)

print("############### 완료!! ###############")
print("#####################################")
