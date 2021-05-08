# -*- coding: utf-8 -*- 
import requests
import hashlib
import json
import random

def md5_key(arg):
    hash = hashlib.md5()
    hash.update(arg.encode(encoding='utf-8'))
    return hash.hexdigest()

def mypost():
	serialNumber = random.randrange(1111,200000,1)
	print serialNumber

	data = {"bidAddress":u"四川成都","bidBeginDate":"2021-02-02 12:00:00","bidFileEndDate":"2021-08-01 12:00:00","bidName":u"标段名称1","bidNo":"biaoduanbianhao222","bidValidity":"2021-10-03 12:00:00","bidWebsite":"http://www.1688.com","bond":"600000","fileNo":"wennjianbianhao111","holder":u"金惠家科技局","holderPaperNo":"91510100743648211G","insured":u"被保人1","insuredPaperNo":"beibaoren67890","projectAmt":"400000","projectName":u"项目名称","projectType":"1","serialNumber":serialNumber,"url":"http://www.baidu.com"}
	data3 = {"bidAddress":"四川成都","bidBeginDate":"2021-02-02 12:00:00","bidFileEndDate":"2021-08-01 12:00:00","bidName":"标段名称1","bidNo":"biaoduanbianhao222","bidValidity":"2021-10-03 12:00:00","bidWebsite":"http://www.1688.com","bond":"600000","fileNo":"wennjianbianhao111","holder":"金惠家科技局","holderPaperNo":"91510100743648211G","insured":"被保人1","insuredPaperNo":"beibaoren67890","projectAmt":"400000","projectName":"项目名称","projectType":"1","serialNumber":serialNumber,"url":"http://www.baidu.com"}
	# data11 = sorted(data.keys())
	# print data11
	str2 = json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',', ':'))
	str1 = "InoNKJI131JII" + str2
	print str1
	final_code = md5_key(str1)
	print final_code
	payload = {"channel":"chic","sign":final_code}
	
	url = "http://uat-cbaoxian.jhjhome.com/jhj-hyb-consumer-web/chic/insure"
	res = requests.post(url,params=payload,data = json.dumps(data3,sort_keys=True,separators=(',', ':')),headers={'Content-Type':'application/json'})
	# print(res.url)
	# print(res.headers)
	print(res.text)
if __name__ == '__main__':

	# str2 = json.dumps({"bankAccount":"6225881285263546","bankName":u"招商银行","claimAmount":"300000","damageAreaCode":"0","damageDate":"2021-05-08:00:00:00"," linkerMobile":"17775462598","linkerName":u"李丽","orderNo":"Y0027221121000002689","payName":u"马锈南","policyCode":"60027221121000001797","processDesc":u"长残了","registName":u"马的","reportDate":"2021-05-08:08:08:00","reportMobile":"13885462598","serialNumber":"1871119"},encoding="utf-8",ensure_ascii=False)
# 	# print str2
# 	str1 = "InoNKJI131JII" + str2
# 	# print str1
# 	final_code = md5_key(str1)

	mypost()
