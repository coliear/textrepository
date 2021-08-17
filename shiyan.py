from lxml import etree
import pymysql

for x in range(1, 3):
    html = etree.parse('./baogao/%s.html' % x, etree.HTMLParser())
    result1 = html.xpath('//table[@reporttype="EPOCH"]//tbody//tr//td[1]/p/text()')
    result2 = html.xpath('//table[@reporttype="EPOCH"]//tbody//tr//td[21]/p/text()')
    result_dict = dict(zip(result1, result2))
    # print(result_dict["2"])
    # 此处查询字典对应值的key要带引号,因为其(result_dict["1"])类型为<class 'lxml.etree._ElementUnicodeResult'>,常规列表类型为int则u需要加引号
    # print(type(result_dict))#为dict
    db = pymysql.connect(host="localhost", user="root", password='111111', database='mysql', port=3306,
                         charset='utf8')  # 注意:str(111111)
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS SHIYAN")
    sql = """CREATE TABLE SHIYAN%s (
             EPOCH  int(20) NOT NULL,
             STAGE  varchar(20)
             )""" % x
    cursor.execute(sql)
    for i in range(0, len(result1)):
        sql1 = '''INSERT INTO SHIYAN%s(EPOCH,STAGE)VALUES('%s', '%s')''' % (x,result1[i], result2[i])
        cursor.execute(sql1)
        db.commit()
