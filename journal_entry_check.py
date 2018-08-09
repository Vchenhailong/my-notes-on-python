#! /usr/bin/python
# coding=utf-8
# cx_Oracle 需要安装环境
# 颜色输出格式为：开头部分：\033[显示方式;前景色;背景色m + 结尾部分：\033[0m
# 颜色输出格式可参考 https://www.cnblogs.com/hellojesson/p/5961570.html
# 显式游标的使用顺序可以明确的分成声明游标、打开游标、读取数据和关闭游标4个步骤
# 解决 cx_Oracle 的中文显示'？'的问题 https://blog.csdn.net/liluotuo/article/details/46535669

import cx_Oracle as Oracle
import time
from datetime import date, timedelta
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

"""
工具类：日终总账加工
"""


class JournalEntryCheck(Exception):
    # 格式：用户名/密码 @服务IP:PORT / SERVICE_NAME
    user = "acct"
    password = "acct_2018"
    db_ip = "192.168.7.50"
    port = 1521
    service_name = "sitpay1"
    ordb = Oracle.connect("{0}/{1}@{2}:{3}/{4}".format(user, password, db_ip, str(port), service_name),
                          encoding='UTF-8')
    print("数据库信息:%s" % ordb)

    def __init__(self):
        self.date = time.strftime("%Y%m%d")
        print("系统日期为：{date}".format(date=self.date))

        # TODO: 了解 time, timedate 模块
        # 在 oracle 中以数据库的日期，按业务查询会计日则是：" SELECT TO_CHAR(SYSDATE-1,'YYYYmmdd') FROM DUAL; "
        # 按业务的技术定义，做对应的日期格式化
        # 另外，获取会计日期的最保险方式，应是查询日切服务表中会计日作为结果
        self.account_date = date.today() - timedelta(days=1)  # 此时类型非字符串

        print("\033[1;32;0m 会计日期为：{account_date} \033[0m".format(account_date=self.account_date.strftime("%Y%m%d")))

    @staticmethod
    def is_blank(rowcount):
        if isinstance(rowcount, int):
            if rowcount == 0:
                raise EOFError("数据库查询的结果集为空")
            else:
                return False
        else:
            raise ValueError("非数字类型")

    # Step1：将日间发生的动账明细，汇总至日总账明细临时表
    def detail_total_numb_check(self):
        print("==================== Step1 明细汇总检查 ====================")
        # 创建游标，获取到 cursor 对象
        # TODO:http://cx-oracle.readthedocs.io/en/latest/cursor.html
        cr = self.ordb.cursor()
        # 执行 SQL
        cr.execute("SELECT 1 FROM ACCT.CORE_ACT_DETAIL WHERE ACCOUNT_DATE = {account_date}".format(
            account_date=self.account_date.strftime("%Y%m%d")))
        # fetchall() 返回一个元组组成的列表
        cr.fetchall()
        # 读取游标操作后的条目数
        m_total = cr.rowcount

        # self.is_blank(m_total)

        print("====> Log:当日的主账明细统计条目数为：%s" % m_total)

        cr.execute("SELECT 1 FROM ACCT.CORE_ACT_INTERIOR_DETAIL WHERE ACCOUNT_DATE = {account_date}".format(
            account_date=self.account_date.strftime("%Y%m%d")))
        cr.fetchall()
        i_total = cr.rowcount

        # self.is_blank(i_total)

        print("====> Log:当日的内部账明细统计条目数为：%s" % i_total)

        cr.execute("SELECT 1 FROM ACCT.CORE_TOTAL_DETAIL_TEMP WHERE ACCOUNT_DATE = {account_date}".format(
            account_date=self.account_date.strftime("%Y%m%d")))
        cr.fetchall()
        t_total = cr.rowcount
        print("====> Log:当日的总账明细统计条目数为：%s" % t_total)

        if t_total == m_total + i_total:
            print("\033[1;34;0m Step1:备份成功! 备份的条目数总共为{num} \033[0m".format(num=str(t_total)))
            if t_total == 0:
                print("====>Log:Step1 今日明细备份表中发现根本没有交易数据, 还是人工检查一波吧")
        else:
            print("\033[1;31;0m Error:检查备份结果失败 \033[0m")
        cr.close()

    # Step2：业务类型的完成有效性检查
    def effective_complete_entry_check(self):
        print("==================== Step2 业务类型的完成有效性检查 ====================")
        cr = self.ordb.cursor()

        print("===== Step2.1  有效性检查之[业务编码] =====")
        cr.execute("SELECT 1 FROM (SELECT VOUCHER_LIST_TYPE_CODE \
                                      FROM CORE_TOTAL_DETAIL_TEMP WHERE ACCOUNT_DATE={account_date} AND \
                                      VOUCHER_LIST_TYPE_CODE NOT IN (SELECT VOUCHER_LIST_TYPE_CODE FROM \
                                      CORE_ACT_VCHLIST_INFO)) ".format(
            account_date=self.account_date.strftime("%Y%m%d")))
        cr.fetchall()
        invalid_voucher_type_num = cr.rowcount
        print("====> Log: +业务编码无效数为：%d" % invalid_voucher_type_num)
        if invalid_voucher_type_num != 0:
            print("\033[1;31;0m Error:存在不匹配的[业务编码]——voucher_list_type_code！条目数为 %s \033[0m" % invalid_voucher_type_num)
        assert invalid_voucher_type_num == 0
        print("\033[1;34;0m 有效性检查之[业务编码] 通过 \033[0m")

        print("===== Step2.1 +有效性检查之[分录编码] =====")
        cr.execute("SELECT 1 FROM (SELECT VOUCHER_TYPE_CODE \
                                        FROM CORE_TOTAL_DETAIL_TEMP WHERE ACCOUNT_DATE={account_date} AND VOUCHER_TYPE_CODE \
                                        NOT IN (SELECT VOUCHER_TYPE_CODE FROM CORE_ACT_VCHCHILD_INFO)) \
                                        ".format(account_date=self.account_date.strftime("%Y%m%d")))
        cr.fetchall()
        invalid_voucher_type_code_num = cr.rowcount
        print("====> Log:分录编码无效数为：%d" % invalid_voucher_type_code_num)
        if invalid_voucher_type_code_num != 0:
            print("\033[1;31;0m Error: 存在不匹配的[分录编码]——voucher_type_code！条目数为 %s \033[0m" % invalid_voucher_type_code_num)
        assert invalid_voucher_type_code_num == 0
        print("\033[1;34;0m +有效性检查之[分录编码] 通过 \033[0m")

        print("===== Step2.2  完整性检查之[分录完整] =====")
        # 获取定义的会计分录表的元数据表 metadata
        cr.execute("SELECT * FROM ACCT.CORE_ACT_VOUCHER_INFO ORDER BY VOUCHER_LIST_TYPE_CODE")
        result = cr.fetchall()
        __map = {'VOUCHER_LIST_TYPE_CODE': '', 'VOUCHER_ORDER': ''}
        __lst = list()
        for i in range(len(result) - 1):
            __map.update(VOUCHER_LIST_TYPE_CODE=result[i][1], VOUCHER_ORDER=result[i][2])
            __lst.append(__map)
        print("====> Log:分录规则为 %s" % __lst)
        # 根据会计日，按账传票套流水号检索明细表的数据
        cr.execute("SELECT VOUCHER_LIST_TYPE_CODE, VOUCHER_ORDER, VOUCHER_LIST_SERIAL_NO FROM ACCT.CORE_TOTAL_DETAIL_TEMP WHERE \
                        ACCOUNT_DATE={account_date}  ORDER BY VOUCHER_LIST_SERIAL_NO".format(
            account_date=self.account_date.strftime("%Y%m%d")))
        detail_result = cr.fetchall()
        print("====> Log:在会计日当天，明细表的结果集为 %s" % detail_result)

        row_num = cr.rowcount
        if row_num == 0:
            raise EOFError("====> Log:在会计日当天，明细表的结果为空")
        else:
            for i in range(row_num - 1):
                # 判断结果集中的传票套流水号的相等性，即为同一笔交易的相关分录信息
                if detail_result[i][2] == detail_result[i + 1][2]:
                    if detail_result[i][0] == "ACCOUNT_CONSUME_BALACNE":
                        print("====> Log:消费场景的分录完整性检查")
                        __temp = list()
                        __temp.append(detail_result[i][1])
                        # TODO:可优化（变量__lst并未再此用到）
                        assert __temp.count('1') == __temp.count('2') == __temp.count('3') == 1, "消费场景分录是完整的"

                    if detail_result[i][0] == "MERCH_SETTLE_PAY_ABABANK":
                        print("====> Log:商户结算内部账户ABA的分录完整性检查")
                        __temp = list()
                        __temp.append(detail_result[i][1])
                        # TODO:可优化（变量__lst并未再此用到）
                        assert __temp.count('1') == 1, "商户结算内部账户 ABA 的分录是完整的"

                    if detail_result[i][0] == "MERCH_SETTLE_PAY_CIMBBANK":
                        print("====> Log:商户结算内部账户 CIMM 的分录完整性检查")
                        __temp = list()
                        __temp.append(detail_result[i][1])
                        # TODO:可优化（变量__lst并未再此用到）
                        assert __temp.count('1') == 1, "商户结算内部账户 CIMM 的分录是完整的"

                    if detail_result[i][0] == "MERCH_SETTLE_APPLY":
                        print("====> Log:商户结算主账户的分录完整性检查")
                        __temp = list()
                        __temp.append(detail_result[i][1])
                        # TODO:可优化（变量__lst并未再此用到）
                        assert __temp.count('1') == 1, "商户结算主账户的分录是完整的"

                    if detail_result[i][0] == "USER_TRANSFER_BALACNE":
                        print("====> Log:转账场景的分录完整性检查")
                        __temp = list()
                        __temp.append(detail_result[i][1])
                        # TODO:可优化（变量__lst并未再此用到）
                        assert __temp.count('1') == 1 and __temp.count('2') == 1, "转账场景的分录是完整的"
                    continue
        print("\033[1;34;0m +分录完整性检查 通过 \033[0m")

        print("===== Step2.3  异常数据检查，正常情况下应为零条数据 =====")
        cr.execute("SELECT 1 FROM core_total_vchlist_err WHERE ACCOUNT_DATE={account_date}".format(
            account_date=self.account_date.strftime("%Y%m%d")))
        cr.fetchall()
        err_num = cr.rowcount
        print("====> Log:完整有效性的异常数为：%d" % err_num)
        if err_num == 0:
            assert err_num == 0, "业务类型的完整有效性检查通过"
            print("\033[1;34;0m Step2:业务类型的完整有效性检查通过 \033[0m")
        else:
            raise (FileExistsError, "\033[1;31;0m Error: 存在异常数据！请自检 \033[0m")
        cr.close()

    # Step3：借贷平衡检查
    def debit_credit_check(self):
        print("==================== Step3 借贷平衡检查 ====================")
        cr = self.ordb.cursor()

        cr.execute("SELECT VOUCHER_SERIAL_NO, CURRENCY, DEBIT_AMOUNT, CREDIT_AMOUNT FROM ACCT.CORE_TOTAL_DETAIL_TEMP \
              WHERE ACCOUNT_DATE={account_date}".format(account_date=self.account_date.strftime("%Y%m%d")))

        data = cr.fetchall()
        row_num = cr.rowcount
        if row_num == 0:
            print("====> Log: Step3 今日明细备份表中发现根本没有交易数据, 还是人工检查一波吧")
            pass
        for i in range(row_num - 1):
            if data[i][2] == data[i][3]:
                print("\033[1;34;0m Step3:借贷平衡检查通过 \033[0m")
            else:
                raise ValueError("\033[1;31;0m 借贷平衡检查异常 \033[0m")
        cr.close()

    # Step4：内部户余额加工
    def inner_account_blc_check(self):
        print("==================== Step4 内部户余额检查 ====================")
        print("===== Step4.1 内部户日账表数据备份 =====")
        cr = self.ordb.cursor()

        cr.execute(
            "SELECT 1 FROM ACCT.CORE_ACT_INTERIOR_BILLBAK WHERE \
            ACCOUNT_DATE=(SELECT TO_CHAR(SYSDATE-1, 'YYYYmmdd') FROM DUAL)")
        cr.fetchall()
        back_no = cr.rowcount

        cr.execute(
            "SELECT 1 FROM ACCT.CORE_ACT_INTERIOR_BILL WHERE \
            ACCOUNT_DATE=(SELECT TO_CHAR(SYSDATE-1, 'YYYYmmdd') FROM DUAL)")
        origin_no = cr.rowcount

        if back_no == origin_no:
            print("====> Log:内部户日账表数据备份正常。备份条目数：%s" % back_no)
        else:
            assert ValueError, "备份失败"

        print("===== Step4.2 内部户日账表的上日借方余额和上日贷方余额核查 =====")
        cr.execute('SELECT DEBIT_BALANCE "当日借方余额", CREDIT_BALANCE "当日贷方余额" \
                    FROM ACCT.CORE_ACT_INTERIOR_BILLBAK \
                    WHERE ACCOUNT_DATE=(SELECT TO_CHAR(SYSDATE-1, \'YYYYmmdd\') FROM DUAL)')
        inner_data_bak = cr.fetchall()
        cr.rowcount

        cr.execute('SELECT LAST_DEBIT_BALANCE "上日借方余额", LAST_CREDIT_BALANCE "上日贷方余额" \
                   FROM ACCT.CORE_ACT_INTERIOR_BILL \
                   WHERE ACCOUNT_DATE=(SELECT TO_CHAR(SYSDATE-1, \'YYYYmmdd\') FROM DUAL)')
        inner_data = cr.fetchall()
        if len(inner_data) != 0 and len(inner_data) != 0:
            if inner_data_bak[0][0] == inner_data[0] and inner_data[1] == inner_data_bak[0][1]:
                print("内部户日账表的上日借方、贷方余额更新为：%s, %s" % (inner_data[0], inner_data[1]))
                print("====> Log:内部户日账表数据的上日借贷余额无异常")
        else:
            raise ValueError("会计日日终处理的内部户日账借贷余额的值处理错误了")

        print("===== Step4.3 内部户日账表的“当日借方累计发生额”和“当日贷方累计发生额”核查 =====")
        cr.execute("SELECT SUM_DEBIT_AMOUNT \"内部户借方累计发生额\", LAST_CREDIT_BALANCE \"内部户贷方累计发生额\" \
                    FROM ACCT.CORE_ACT_INTERIOR_BILL \
                    WHERE ACCOUNT_DATE=(SELECT TO_CHAR(SYSDATE-1, 'YYYYmmdd') FROM DUAL)")
        cr.fetchall()

        # Step5：总账加工的检查
        # Step6：总分核对的检查(目前只实现主账户的总账科目和对应分账户的核对）


if __name__ == '__main__':
    t = JournalEntryCheck()
    t.detail_total_numb_check()
    t.effective_complete_entry_check()
    t.debit_credit_check()
    t.inner_account_blc_check()
