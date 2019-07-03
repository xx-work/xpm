
UrlMemuDicts = dict(

)

# xadmin 对应的APP的前缀， 后面的一个对应视图测试使用的前缀
XADMIN_URL_PREFIX = "/admin/"
MEMU_SUFFIX = 'hocked/'
XADMIN_VIEWD_URL_PREFIX = XADMIN_URL_PREFIX + MEMU_SUFFIX

POLICY_COMMON_URL = "mgsd/policyrule/?_p_policy_bench__type__exact="
CHK_COMMON_URL = "mgsd/changeaudit/?_p_change_type__exact="

common_list = [
    ['sys_policy', POLICY_COMMON_URL + "system"],
    ['sec_policy', POLICY_COMMON_URL + 'security'],
    ['aud_policy', POLICY_COMMON_URL + 'audit'],

    ['sys_chk', CHK_COMMON_URL + 'system'],
    ['sec_chk', CHK_COMMON_URL + 'security'],
    ['aud_chk', CHK_COMMON_URL + 'audit'],

]


def set_memu_dict(name, menu_url, origin_url):
    """
    创建memu名称
    :param name: 正则辨别的唯一str
    :param url:
    :param redirect_url:
    :return:
    """
    temp = {}
    temp.setdefault("name",  name)
    temp.setdefault("menu_url",  menu_url)
    temp.setdefault("origin_url",  origin_url)
    return temp


def get_memu_dicts():
    results = {}
    for x in common_list:
        results = dict(results, **{x[0]: set_memu_dict(x[0], XADMIN_VIEWD_URL_PREFIX + x[0], XADMIN_URL_PREFIX + x[1])})
    return results


MENU_DICTS = get_memu_dicts()
get_menu_url = lambda name: MENU_DICTS[name]["menu_url"]  ## 菜单视图使用
get_menu_origin_url = lambda name: MENU_DICTS[name]["origin_url"] ## 重定向视图使用