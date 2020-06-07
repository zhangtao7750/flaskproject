def get_db_uri(dbinfo):
    engine=dbinfo.get("ENGINE") or "sqlite"
    driver=dbinfo.get("DRIVER") or "sqlite"
    user=dbinfo.get("USER") or ""
    password=dbinfo.get("PASSWORD") or ""
    host=dbinfo.get("HOST") or ""
    port=dbinfo.get("PORT") or ""
    name=dbinfo.get("NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name)
class Config:
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopConfig(Config):
    DEBUG=True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"Zt@647409",
        "HOST":"localhost",
        "PORT":"3306",
        "NAME":"myflask",
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class TestConfig(Config):
    DEBUG=True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"Zt@647409",
        "HOST":"localhost",
        "PORT":"3306",
        "NAME":"myflask",
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)


class StagingConfig(Config):
    DEBUG=True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"Zt@647409",
        "HOST":"localhost",
        "PORT":"3306",
        "NAME":"myflask",
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)


class ProductionConfig(Config):
    DEBUG=True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"Zt@647409",
        "HOST":"localhost",
        "PORT":"3306",
        "NAME":"myflask",
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)


envs={
    "develop":DevelopConfig,
    "testing":TestConfig,
    "staging":StagingConfig,
    "production":ProductionConfig,
    "default":DevelopConfig,
}