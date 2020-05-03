#!/bin/python
### import module for access database
# encoding: utf-8
from datetime import datetime
import pymysql


def get_query_result():
    print("start")
    cnx = pymysql.connect(user='dbadmin', password='1qaz!QAZ', host='rm-2ze4n76u4c13ckb97.mysql.rds.aliyuncs.com', database='data_check')
    print("connect success")
    mycursor = cnx.cursor()
    mycursor1 = cnx.cursor()
    mycursor3 = cnx.cursor()
    mycursor4 = cnx.cursor()
    mycursor5 = cnx.cursor()

     
    ###
    
    # query = "select * from bd_region1 "
    query = r"""
	select * from 
    test_big_bud_af
	order by CsmBUILDINGID1,pm_Building_ID1; 
    """

    #query1 = "truncate table test_tmp121;"
# test_tmp121    query2 = "select count(*) from test_big_af1"
#     mycursor.execute(query2)
#     max = mycursor.fetchall()
#     print(max[0])
    mycursor3.execute(query)
    # print(query)
    data = mycursor3.fetchmany(500)
    print("start fetch")
    i = 0
    j = 0
    k = 0

    while not(data is None):
        j = j + 1
        query51 = ""
        for item in data:

            # print(item)
            item_trim = str(item).replace("(", "").replace(")", "")
            # print(item_trim)
            item1 = str(item_trim).split(',')
            # print(str(item_trim).split(','))
            # print(len(item1))

            query4 = " select * from test_bud126 where "
            flag1 = 0
            whers = ""

            if item1[0].strip() == 'None':
                if item[3].strip() != 'None':
                    query4 = query4 + " CsmBUILDINGID= %s " % (item1[3])
                    whers = "  CsmBUILDINGID1 = %s  " % (item1[3])
                    flag1 = 1
            else:
                query4 = query4 + " CsmBUILDINGID= %s " % (item1[0])
                whers = "  CsmBUILDINGID1 = %s  " % (item1[0])
                flag1 = 1
            if item1[4].strip() != 'None':
                if flag1 == 1:
                    query4 = query4 + " or pm_Building_ID= %s " % (item1[4])
                else:
                    query4 = query4 + " pm_Building_ID= %s " % (item1[4])
                flag1 = 1
            # print(query4)

            if flag1 == 1:
                query4 = query4 + ";"
                # print(query4)
                mycursor4.execute(query4)

                data4 = mycursor4.fetchone()
                # print(data4)
                data41 = str(data4).replace("(", "").replace(")", "")
                if len(data41) > 0 and not(data4 is None):
                    #print("data %s" % data41)

                    # print(len(data4))
                    # print(data4)
                    item_trim4 = str(data4).replace("(", "").replace(")", "")
                    # print(item_trim4)
                    item4 = str(item_trim4).split(',')
                    # print(str(item_trim).split(','))
                    # print(len(item4))
                    fis1 = 0

                    query5 = " update test_big_bud_af set "
                    if item4[0].strip() != 'None':
                        query5 = query5 + "CsmBuildingID2 = %s " % (item4[0])
                        fis1 = 1
                    if item4[1].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "pm_Building_ID2 = %s " % (item4[1])
                    if item4[2].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "Buildingcode2 = %s " % (item4[2])
                    if item4[3].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "Building_ID2 = %s " % (item4[3])
                    if item4[4] .strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "regionsnum2 = %s " % (item4[4])
                    if item4[5].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "regioncode2 = %s" % (item4[5])
                    if item4[6].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "project_ID2 = %s" % (item4[6])
                    if item4[7].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "project_name2 = %s" % (item4[7])
                    if item4[8].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "is_public2 = %s" % (item4[8])
                    if item4[9].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "vitual2 = %s" % (item4[9])

                    if item4[10].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "unitsnum2 = %s" % (item4[10])
                    if item4[11].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "floorsnum2 = %s" % (item4[11])
                    if item4[12].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "is_del2 = %s" % (item4[12])
                    if item4[13].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "plan_id2 = %s" % (item4[13])
                    if item4[14].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "plan_name2 = %s" % (item4[14])
                    if item4[15].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "commid2 = %s" % (item4[15])
                    if item4[16].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "regionname2 = %s" % (item4[16])
                    if item4[17].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "building_type2 = %s" % (item4[17])
                    if item4[18].strip() != 'None':
                        if fis1 == 1:
                            query5 = query5 + ", "
                        else:
                            fis1 = 1
                        query5 = query5 + "budname2 = %s" % (item4[18])

                    #print(query5)
                    query5 = query5 + " where " + whers + ";"
                    print(query5)
                    mycursor5.execute(query5)
                    query51 = query51 + query5
                    i = i + 1
                    k = k + 1

        #mycursor5.execute(query51)
        cnx.commit()

        print("commit %i " % i)
        print("total %i " % k)

        i = 1
        query51 = ""
        data = mycursor3.fetchmany(500)

        print("loop %i " % i)
        item_trim = str(data).replace("(", "").replace(")", "")
        if item_trim.strip() == "":
            print("end")
            exit()
        # print(data)
    ###
def sql_main():
    try:
     cnx.commit()

    except e:
        print("err")
        mycursor.close()
        mycursor1.close()
        mycursor3.close()
        cnx.close()
    	# raise()
    else:
        print("not exit")
        cnx.commit()
        pass
    finally:
    	pass

    cnx.commit()
    mycursor.close()
    mycursor1.close()
    mycursor3.close()
    cnx.close()
    
def inst():
	pass 


def print_time_stamp():
    print('In schedule plan, This time is: %s' % datetime.now())


if __name__ == '__main__':
    get_query_result()
