# 普通服务器的审计记录

# aureport 命令
```
# 登录日志
aureport --failed    #针对失败的event的统计，如果统计成功的用aureport --success
aureport -if myfile           #aureport 没带任何参数，仅用-if指定一个audit log文件， 统计出它的总体的log报告， 如何不指定文件，显示当前audit的统计。
aureport -l -ts 14:00 -te 15:00 -if myfile    #对于myfile的log文件，统计出从14：00到15：00的用户登录信息。

aureport -s   #system call的报告
aureport -x   #从可执行的角度去查看audit log
aureport -u     #对于用户在系统运行命令的生成的报告
aureport -l -i    #用户登录事件生成的报告
aureport -t   #查看audit log文件包含日志的起止时间
aureport -e -i --summary   #分类统计事件数量
```


# ausearch命令
```bash
ausearch -m    #按消息类型查找
ausearch -ul   #按登陆ID查找
ausearch -ua   #按uid和euid查找
ausearch -ui   #按uid查找
ausearch -ue   #按euid查找
ausearch -ga   #按gid和egid查找
ausearch -gi   #按gid查找
ausearch -ge   #按egid查找
ausearch -c    #按cmd查找
ausearch -x    #按exe查找
ausearch -sc   #按syscall查找
ausearch -p    #按pid查找
ausearch -sv   #按syscall的返回值查找（yes/no）
ausearch -f    #按文件名查找
ausearch -tm   #按连接终端查找(term/ssh/tty)
ausearch -hn   #按主机名查找
ausearch -k    #按特定的key值查找
ausearch -w    #按在audit rule设定的字符串查找
```


