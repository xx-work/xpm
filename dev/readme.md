# 开发部署说明文档



## Docker 
- `docker` Web平台部署概要 [老版本](./docker)
  - [Nginx容器和配置文件](./docker/nginx-container)
  - [Web容器docker-compose](./docker/docker-compose.yml)
  - [Docker安装脚本](./docker/install_docker.sh)
  - [宿主机安装python脚本](./docker/install_python36.sh)
- `sueprvisord` 宿主机部署服务管控配置 [Supervisord](./supervisord)
  - [gunicorn](./supervisord/supervisord.d/gunicorn.ini)
  - [celery](./supervisord/supervisord.d/celery.ini)
  - [celery-beat](./supervisord/supervisord.d/beat.ini)
  - [flower](./supervisord/supervisord.d/flower.ini)
- `docker-all` 完全版本的 `docker-compose` 设置

## Docker 架构修改
- django-beat 失效，异步任务使用 apscheduler 控制 djcelery 
