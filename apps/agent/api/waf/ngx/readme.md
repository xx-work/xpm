# Nginx 辅助工具

## 安装
```shell 
yum -y install epel-release 
yum -y install nginx certbot vim curl wget git
sudo certbot certonly --webroot -w /usr/share/nginx/html/ -d tj.actanble.com
```

```bash
echo "*/20 * * * * root /usr/bin/python3.6 /root/replace_cookie.py" >> /etc/crontab 
```
