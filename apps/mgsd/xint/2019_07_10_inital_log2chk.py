


if __name__ == '__main__':
    from src import django_setup

    django_setup()

    from mgsd.xtool.log2chk import get_category_of_models_by_modelname, get_chk_recode_by_log

    get_chk_recode_by_log()