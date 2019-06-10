import os

from website.settings import PROJECT_DIR, CONFIG, DOCKERD

MYSQL_DB_BACKUPD_DIR = os.path.join(PROJECT_DIR, "backupd", "mysqldb" )
MYSQL_BIN_PREFIX = "docker exec -t mysql-server " if DOCKERD else ""

if not os.path.exists(MYSQL_DB_BACKUPD_DIR):
    os.makedirs(MYSQL_DB_BACKUPD_DIR)
MYSQL_DB_BACKUPD_PATH = lambda uid : os.path.join(MYSQL_DB_BACKUPD_DIR, str(uid) + ".sql")


def get_backup_recover_cmd(uid, Backup=True):
    if Backup:
        return "{MYSQL_BIN_PREFIX} mysqldump -h{DB_HOST} -P{DB_PORT} -u{DB_USER} -p{DB_PASSWORD} {DB_NAME} > {path}".format(
            MYSQL_BIN_PREFIX=MYSQL_BIN_PREFIX,
            DB_HOST=CONFIG.DB_HOST,
            DB_PORT=CONFIG.DB_PORT,
            DB_USER=CONFIG.DB_USER,
            DB_PASSWORD=CONFIG.DB_PASSWORD,
            DB_NAME=CONFIG.DB_NAME,
            path=MYSQL_DB_BACKUPD_PATH(uid),
        )

    return "{MYSQL_BIN_PREFIX} mysql -h{DB_HOST} -P{DB_PORT} -u{DB_USER} -p{DB_PASSWORD} {DB_NAME} < {path}".format(
        MYSQL_BIN_PREFIX=MYSQL_BIN_PREFIX,
        DB_HOST=CONFIG.DB_HOST,
        DB_PORT=CONFIG.DB_PORT,
        DB_USER=CONFIG.DB_USER,
        DB_PASSWORD=CONFIG.DB_PASSWORD,
        DB_NAME=CONFIG.DB_NAME,
        path=MYSQL_DB_BACKUPD_PATH(uid),
    )

