#-*-coding:utf-8-*-
#env/python3
#folw_chart : https://www.processon.com/view/link/58c522e6e4b0df53ed31350d

all_the_cities ={'一级菜单1':{'二级菜单11':['三级菜单111','三级菜单112','三级菜单113','三级菜单114','三级菜单115','三级菜单116'],'二级菜单12':['三级菜单121','三级菜单122','三级菜单123','三级菜单124']},
                 '一级菜单2':{'二级菜单21':['三级菜单211','三级菜单212','三级菜单213','三级菜单214','三级菜单215','三级菜单216'],'二级菜单22':['三级菜单221','三级菜单222','三级菜单223','三级菜单224']},
                '一级菜单3':{'二级菜单31':['三级菜单311','三级菜单312','三级菜单313','三级菜单314','三级菜单315','三级菜单316'],'二级菜单32':['三级菜单321','三级菜单322','三级菜单323','三级菜单324']},
                '一级菜单4':{'二级菜单41':['三级菜单411','三级菜单412','三级菜单413','三级菜单414','三级菜单415','三级菜单416'],'二级菜单42':['三级菜单421','三级菜单422','三级菜单423','三级菜单424']},
                '一级菜单5':{'二级菜单51':['三级菜单511','三级菜单512','三级菜单513','三级菜单514','三级菜单515','三级菜单516'],'二级菜单52':['三级菜单521','三级菜单522','三级菜单523','三级菜单524']},
                '一级菜单6':{'二级菜单61':['三级菜单611','三级菜单612','三级菜单613','三级菜单614','三级菜单615','三级菜单616'],'二级菜单62':['三级菜单621','三级菜单622','三级菜单623','三级菜单624']},
                '一级菜单7':{'二级菜单71':['三级菜单711','三级菜单712','三级菜单713','三级菜单714','三级菜单715','三级菜单716'],'二级菜单72':['三级菜单721','三级菜单722','三级菜单723','三级菜单724']},
                '一级菜单8':{'二级菜单81':['三级菜单811','三级菜单812','三级菜单813','三级菜单814','三级菜单815','三级菜单816'],'二级菜单82':['三级菜单821','三级菜单822','三级菜单823','三级菜单824']},
                '一级菜单9':{'二级菜单91':['三级菜单911','三级菜单912','三级菜单913','三级菜单914','三级菜单915','三级菜单916'],'二级菜单92':['三级菜单921','三级菜单922','三级菜单923','三级菜单924']},
                '一级菜单10':{'二级菜单101':['三级菜单1011','三级菜单1012','三级菜单1013','三级菜单1014','三级菜单1015','三级菜单1016'],'二级菜单102':['三级菜单1021','三级菜单1022','三级菜单1023','三级菜单1024']},
                '一级菜单11':{'二级菜单111':['三级菜单1111','三级菜单1112','三级菜单1113','三级菜单1114','三级菜单1115','三级菜单1116'],'二级菜单112':['三级菜单1121','三级菜单1122','三级菜单1123','三级菜单1124']},

                  }



def province_list_get():
    province_list = list(all_the_cities)
    for i in province_list:                                                #打印省级名称及序号
        print(province_list.index(i)+1,i)

def city_list_get(city_id):                                                     #打印市级名称及序号
    city_list = list(all_the_cities[list(all_the_cities)[int(city_id[:2].lstrip("0"))-1]])
    for i in city_list:
        print(city_list.index(i)+1,i)

def region_list_get(city_id):                                                   #打印区级名称及序号
    region_list = list(all_the_cities[list(all_the_cities)[int(city_id[:2].lstrip("0"))-1]].values())[int(city_id[-2:].lstrip("0"))-1]
    for i in region_list:
        print(region_list.index(i)+1,i)


def input_data_processing(city_id,input_data=None):                             #对输入的编码进行判断处理
    if input_data =="q":
        exit()
    elif input_data == "":
        return input_data
    elif input_data == "b":
        return city_id[:-2]
    elif input_data.isdigit() and len(city_id) < 4 and len(input_data) <= 2:
        return city_id + input_data.zfill(2)                                       #数字补0
    elif len(city_id) == 4:
        print("Is the last menu")
        return city_id
    else:
        print("""
        输入编码无法识别，请重新输入：
        帮助如下：
                q         ：   退出程序
                b         ：   返回上一级菜单
                number    ：   进入相应的级别菜单
        """)
        return ""



city_id = ""
input_data = ""
while 1:                                                                #程序内容
    city_id = input_data_processing(city_id,input_data)
    print(city_id)
    try:
        if len(city_id)==0:
            province_list_get()
        elif len(city_id)==2:
            city_list_get(city_id)
        elif len(city_id)==4:
            region_list_get(city_id)
    except IndexError:                                                    #如果没有该选项（即序列下标溢出），则重新输出本级菜单
        print('Where is this option')
        city_id = city_id[0:-2]                                            #列表下标溢出，则删除最后两个字符
        if len(city_id)==0:
            province_list_get()
        elif len(city_id)==2:
            city_list_get(city_id)
        elif len(city_id)==4:
            region_list_get(city_id)
    input_data = input('输入编号：')
