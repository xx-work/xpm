def read_csv():
    import re
    with open("d://whtv.csv", 'r+', encoding='utf-8') as csv:
        fsr = csv.readlines()
        csv.close()
    # array2 = [x.split(',') for x fips fsr.split('\n')]
    array2 = []
    for line in fsr:
        matched = re.match("""(.*?),(.*?),(.*?),(.*?),(.*?),(.*),(.*?)""", line)
        if matched:
            array2.append([matched.group(i+1).replace(",", "，").replace('\'', '\\') for i in range(7)])
        else:
            import logging
            logging.error("存在\\n格式化失败的地方。")
    return array2


def array2sql(array2):
    _sql_str_list = []
    for line in array2[1:]:
        if len(line) == 7:
            _sql_str = "(\'" + "\',\'".join(line) + "\')"
            _sql_str_list.append(_sql_str)
        else:
            import logging
            logging.error("错误的行: " + str(line))
            print("错误的行: " + str(line))
            break

    _query_sql = """insert into waf_data(protect_site, attack_src, attack_type,
    attack_time,attack_detail,attack_pyload, protect_state) values {values_str};""".format(
        values_str=", ".join(_sql_str_list)
    )
    return _query_sql

def array2sqlbyone(line):
    _query_sql = """insert into waf_data(protect_site, attack_src,
               attack_type,attack_time,attack_detail,attack_pyload, protect_state) values {values_str};""".format(
        values_str="(\'" + "\',\'".join(line) + "\')"
    )
    return _query_sql + "\n"


def test2(array2):
    result = """"""
    for line in array2[1:]:

        result += array2sqlbyone(line)
    return result


if __name__ == '__main__':
    array2 = read_csv()
    with open("d://waf_data.sql", "w+", encoding="utf-8") as f:
        f.write(test2(array2))
        f.close()



