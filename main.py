import MySQL_connector
import CSV_Reader

CSV_Reader.csv2json("demo.csv")
MySQL_connector.insert(
    1,"[{'product_id':'2','product_name':'王泉','qty':'11','description':'Wong330ml','weight':'330g'},{'product_id':'1','product_name':'玉泉','qty':'12','description':'CreamSoda330mL','weight':'330g'}]","cityu,kln","cityu,ac2,kln","2019-01-3111:06:03", 2 ,"{'customer_name':'玉王牌','contact':'59883943','description':'SoftDrinkCompany','address':'cityu,ac2,kln'}"
)