import redis


class RedisCli():

    def __init__(self, host='192.168.2.227', port=6379, password='xxscan'):
        self.host = host
        self.port = port
        self.password=password

    def redis_agent(self):
        return redis.Redis(host=self.host, port=self.port, password=self.password)