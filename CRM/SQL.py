import pymysql


def conn():
    Environmental_Science = 'dev'
    if Environmental_Science == 'dev':
        host = "120.25.193.33"
    elif Environmental_Science == 'test':
        host = "47.106.249.160"

    conn_jmgj_crm = pymysql.connect(host=f"{host}", user="root", password="123456", database="jmgj_crm",
                                    charset="utf8", port=3306)

    conn_jmgj_marketing = pymysql.connect(host=f"{host}", user="root", password="123456", database="jmgj_marketing",
                                    charset="utf8", port=3306)

    conn_member_center = pymysql.connect(host=f"{host}", user="root", password="123456", database="member_center",
                                    charset="utf8", port=3306)

    return conn_jmgj_crm,conn_jmgj_marketing,conn_member_center

def get_salesman_id_name(job,job2):   # 1.输入id查姓名 2.输入姓名查id

    cursor_jmgj_crm = conn()[3].cursor()
    if job == 1:
        sql_name = f"select AES_DECRYPT(from_base64(real_name),'jmgj_aes') from crm_salesman where id = '{job2}'"
        cursor_jmgj_crm.execute(sql_name)
        result = cursor_jmgj_crm.fetchall()
        cursor_jmgj_crm.close()
        conn()[3].close()
        return print(result[0], job2)
    elif job == 2:
        sql_id = f"select id from crm_salesman where (select AES_DECRYPT(from_base64(real_name),'jmgj_aes')) = '{job2}'"
        cursor_jmgj_crm.execute(sql_id)
        result = cursor_jmgj_crm.fetchone()
        cursor_jmgj_crm.close()
        conn()[3].close()
        return print(result[0], job2)
    else:
        print('请正确填入数据')

def get_sumit_products():
