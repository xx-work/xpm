# 辅助 xadmin 管理




## Xadmin 自定制
- [Xadmin页面自定制](https://www.cnblogs.com/pgxpython/p/10242748.html)


## 教程


### ModelView 参数
```
list_display=[] #要显示的字段
search_fields=[] #搜索的字段
list_filter = [] #过滤器
date_hierarchy =['publication_date']  #添加过滤（这里是过滤日期）
ordering = ['-publication_date',]   #排序（这里以日期排序，加‘-’表示降序）
filter_horizontal = ('authors',) #filter_horizontal 从‘多选框’的形式改变为‘过滤器’的方式，水平排列过滤器，必须是一个 ManyToManyField类型，且不能用于 ForeignKey字段，默认地，管理工具使用`` 下拉框`` 来展现`` 外键`` 字段
filter_vertical = ['authors',]#同上filter_horizontal，垂直排列过滤器
raw_id_fields = ['publisher',] #将ForeignKey字段从‘下拉框’改变为‘文本框’显示
list_editable = ['csdevice'] #在列表页可直接编辑的字段
model_icon = 'fa fa-user-secret'  #图标样式
style_fields = {'csdevice': 'm2m_transfer','csservice': 'ueditor',} #字段显示样式
refresh_times = [10, 60] #自动刷新时间
show_detail_fields=['ttdsn'] #在指定的字段后添加一个显示数据详情的一个按钮
relfield_style = 'fk-ajax' #涉及到外键下拉的时候使用ajax搜索的方式而不是全部列出的方式，比如在分类下拉很多的情况下，这个功能就很好用
free_query_filter=['字段1','字段2',......]#默认为 True , 指定是否可以自由搜索. 如果开启自由搜索, 用户可以通过 url 参数来进行特定的搜索
exclude=['字段1','字段2',......]#隐藏字段
aggregate_fields = {"expire": "max"}#  列聚合，在list表格下面会增加一行统计的数据，可用的值："count","min","max","avg",  "sum"
# 添加数据时候，一步一步提供数据，分块显示
wizard_form_list = [
        ("基础信息", ("name", "contact", "telphone", "address")),
        ("其它信息", ("customer_id", "expire", "description")),
    ]
grid_layouts = ("table", "thumbnails") #列表的布局方式，是以表格一行一条的方式还是类似于缩略图的方式展示的
list_per_page = 50 # 每页显示数据的条数
list_max_show_all = 200 #每页最大显示数据的条数

```