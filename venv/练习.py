# _*_ coding: utf-8 _*_
import random
# from 随机三要素 import *
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack,file_data
import re
from selenium.common.exceptions import NoSuchElementException
from itertools import product
import pymysql
import requests
import xlrd,xlutils,xlwt



# a = (80.5/(1.75)**2)

# if a >32:
#     print ('严重肥胖')
# elif 28< a <= 32:
#     print ('肥胖')
# elif 25< a <=28:
#     print ('过重')
# elif 18.5< a <= 25:
#     print ('过轻')
#
# l=[1,2,3,4,5,[1,2,3],5]
# print (l[5][2])
#
#
# l= [['Apple','Google','Microsoft'],
#     ['Java','Python','Ruby','PHP'],
#     ['Adam','Bart','Lisa']
# ]
# s=['Adam','Bart','Lisa']
# print (l[0][0])
# print (l[1][1])
# print (s[2])

# c="http://www.baidu.com,自动化测试数据"
# d=',自动化测试数据'
#
# j=0
# for i in range(0,300):
#     j=i+1
#     a = c + str(j) + d + str(j)
#     print(a)

# try:
# print(self.driver.find_element_by_xpath('//li[@class="ant-pagination-total-text"][contains(text(),"共")]').text)
# except NoSuchElementException:
#      file_data("no_such_element.png")
#      self.driver.save_screenshot('no_such_element.png')
#      self.driver.get_screenshot_as_file('no_such_element.png')
#    raise

# a=1
# print("a:",a)
# b=2
# print("b:", b)

# def sanyaosu():
#     def phone():
#         prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
#                  "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
#                 "186", "187", "188", "189"]
#         phone_num = random.choice(prelist) + "".join(random.choice("0123456789")for i in range(8))
#         return phone_num
#
#     def name():
#         last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
#                       '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
#                       '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
#                       '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
#                       '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
#                       '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
#                       '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
#         first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
#                        '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
#                        '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
#                        '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
#                        '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
#                        '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
#                        '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
#                        '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
#                        '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
#                        '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
#                        '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
#                        '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
#                        '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
#                        '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
#                        '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
#                        '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
#                        '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
#                        '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
#                        '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
#                        '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
#                        '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
#                        '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
#                        '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
#                        '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
#                        '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
#                        '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
#                        '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
#                        '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
#                        '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
#                        '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
#                        '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
#                        '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
#                        '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
#                        '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
#                        '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
#                        '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
#                        '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
#                        '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
#                        '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
#                        '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
#                        '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
#                        '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
#                        '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
#                        '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
#                        '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
#                        '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
#                        '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
#                        '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
#                        '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
#                        '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
#                        '乾', '坤']
#         xing = random.choice(last_names)
#         ming = random.sample(first_names,2)
#         name = xing + "".join(ming)
#         # print(xing,ming)
#         return name
#
#
#     def id_card():
#         list = [320282, 320681, 350624, 352230, 360104, 362329, 410724, 420322, 420922, 430122, 430221, 431129, 440229,
#                     440507, 440582, 440981, 445281, 450324, 450326, 450881, 452501, 510182, 510230, 532901, 612429, 630102]
#
#         code = str(random.choice(list))
#
#         # start, end = "1960-01-01", "2000-12-30"
#         # days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
#         # birth_days = datetime.datetime.strftime(
#         #     datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days)), "%Y%m%d")
#
#         year = random.randint(1900,2019)
#         month = random.randint(1,12)
#
#         if month in [1,3,5,7,8,10,12]:
#             day = random.randint(1, 31)
#         else:
#             day = random.randint(1, 30)
#
#         if day <= 9:
#             day = "0" + str(day)
#
#         if month <= 9:
#             month = "0" + str(month)
#
#         birth_days = str(year) + str(month) + str(day)
#
#         # 顺序码(2位数)
#         order = str(random.randint(10, 99))
#         # 性别码(1位数)sex = 0表示女性，sex = 1表示男性
#         sex = str(random.randint(0, 1))
#
#         # 校验码(1位数)
#         number = code + birth_days + order + sex
#         # print(number)
#         n = ((int(number[0])) * 7) + ((int(number[1]) * 9)) + ((int(number[2])) * 10) + ((int(number[3])) * 5) + ( \
#                     (int(number[4])) * 8) + ((int(number[5])) * 4) + ((int(number[6])) * 2) + ((int(number[7])) * 1) + ( \
#                         (int(number[8])) * 6) + ((int(number[9])) * 3) + ((int(number[10])) * 7) + ( \
#                         (int(number[11])) * 9) + ((int(number[12])) * 10) + ((int(number[13])) * 5) + ( \
#                         (int(number[14])) * 8) + ((int(number[15])) * 4) + ((int(number[16])) * 2)
#
#         if n % 11 == 0:
#             code_number = 1
#         elif n % 11 == 1:
#             code_number = 0
#         elif n % 11 == 2:
#             code_number = 'X'
#         elif n % 11 == 3:
#             code_number = 9
#         elif n % 11 == 4:
#             code_number = 8
#         elif n % 11 == 5:
#             code_number = 7
#         elif n % 11 == 6:
#             code_number = 6
#         elif n % 11 == 7:
#             code_number = 5
#         elif n % 11 == 8:
#             code_number = 4
#         elif n % 11 == 9:
#             code_number = 3
#         elif n % 11 == 10:
#             code_number = 2
#         else:
#             print("异常请检查")
#
#         id_card = number+str(code_number)
#         # print(id_card)
#         return id_card

# dir = {"phone":phone3(),"name":name3(),"id_card":id_card3()}
# print("第一次：",dir["phone"])
# print("第二次：",dir["phone"])


# @ddt
# class test1(unittest.TestCase):
#     list1 = [1,2,4]
#     @data(*list1)
#     def test_001(self,param):
#         print(param)
#
#
#
# if __name__ == '__main__':
#     unittest.main()

# def phone():
#
#     phone_head = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
#                  "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
#                 "186", "187", "188", "189"]
#
#     phone = product(phone_head,product(["0123456789"],repeat=8))
#     return phone
#
# print(phone)


# 迭代器
# for repeat in range(1,9):
#     a = product("qwertyuiopasdfghjklzxcvbnm!@#$%^&*_+\|<>,.:;'{}01234-=`~56789",repeat=repeat)
#     for i in a:
#         i = ''.join(i)
#         print(i)
#     if i == "shazi666":
#         break


# a = ["1","2","3"]
# b = "".join(a)
# print(b)



# li = ['A','B','C']
# print(len(li))
# for list in range(0,3):
#     print(li[list])

# a = random.randint(0000,5555)
# # print(a)


# sum = 0
# i=1
# while i < 100:
#     if i % 2 ==1:
#         sum += -1
#     i += 1
# print(sum)

# zhanghao = 'MJ'
# mima = 123456
#
# total_count = 3
# while total_count > 0:
#     zhang = input('请输入账号')
#     mi = input('请输入密码')
#     if zhang==zhanghao and int(mi)==mima:
#         print('登陆成功')
#         break
#     else:
#         total_count -= 1
#         print(f'账户或密码错误,你还有{total_count}次机会')
#         if total_count == 0:
#             print('你的机会已用光,请明日再试')

# total_count = 3
# age = random.randint(1,100)
# print(age)
# run = True
# status = ''
# cai = ''
# while run:
#     while total_count > 0:
#         if status == 'admin123':
#             break
#         cai = int(input('年龄是？'))
#         print(type(cai))
#         if int(cai) == age:
#             print('恭喜你猜中了！！！')
#             break
#         #
#         # elif type(cai)!=int:
#         #     input('请输入正确格式')
#         #     cai = ''
#         else:
#             total_count -= 1
#             print(f'很可惜,没猜中哦！你还有{total_count}次机会')
#             while total_count == 0:
#                 print('你的机会用完了,是否继续游戏？回复Y或者y继续游戏；回复N或者n退出游戏')
#                 end = input('是否继续游戏？')
#                 if end == 'Y' or end == 'y':
#                     run = True
#                     total_count = 3
#                 elif end == 'N' or end == 'n':
#                     print('游戏结束')
#                     total_count = 0
#                     run = False
#                     break
#                 else:
#                     run = True
#                     total_count =
#                     status = 'admin123'
#     if status == 'admin123':
#         end = input('请输入正确胡格式 Y OR N,是否继续游戏？')
#         if end == 'Y' or end == 'y':
#             run = True
#         elif end == 'N' or end == 'n':
#             print('游戏结束')
#             total_count = 0
#             run = False
#         else:
#             run = True
#             total_count = 1
#             status = 'admin123'


# for i in range(1,20,2):
#     print(f'{i*"*":^20}')

# def get_salesman_info(job,job2):
#
#     conn_jmgj_crm = pymysql.connect(host="120.25.193.33", user="root", password="123456", database="jmgj_crm",   #dev
#                                     charset="utf8", port=3306)
#     cursor_jmgj_crm = conn_jmgj_crm.cursor()
#     if job == 1:
#         sql_name = f"select AES_DECRYPT(from_base64(real_name),'jmgj_aes') from crm_salesman where id = '{job2}'"
#         cursor_jmgj_crm.execute(sql_name)
#         result = cursor_jmgj_crm.fetchall()
#         cursor_jmgj_crm.close()
#         conn_jmgj_crm.close()
#         return print(result, job2)
#     elif job == 2:
#         sql_id = f"select id from crm_salesman where (select AES_DECRYPT(from_base64(real_name),'jmgj_aes')) = '{job2}'"
#         cursor_jmgj_crm.execute(sql_id)
#         result = cursor_jmgj_crm.fetchone()
#         cursor_jmgj_crm.close()
#         conn_jmgj_crm.close()
#         return print(result[0], job2)
#     else:
#         print('请正确填入数据')

# def delete_crm_wechat():
#     print()
#
# def get_sqlconn():
#     conn_jmgj_crm = pymysql.connect(host="120.25.193.33",user="root",password="123456",database="jmgj_crm",charset="utf8",port=3306)
#     conn_member_center = pymysql.connect(host="120.25.193.33",user="root",password="123456",database="",charset="utf8",port=3306)
#     cursor_jmgj_crm = conn_jmgj_crm.cursor()
#     cursor_member_center = conn_member_center.cursor()


    # sql_create = "create table MJtest2 (id int auto_increment primary key,name char(10) not null unique,age tinyint not null)engine = innodb"
    # print(cursor.execute(sql))
    # cursor.close()

get_salesman_info(2,'郭一')