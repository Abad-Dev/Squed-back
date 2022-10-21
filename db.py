import pymysql


def connect():
    return pymysql.connect(
        host='67.225.161.252',
        user='limamenu_squed',
        password='Diego5147',
        db='limamenu_squed'
    )

