"""
Django自带模块:
    shortcuts - 快捷方式库
        render - 简化了渲染模板的操作，有了这个函数，就不用先创建Template对象再去调用render方法
    urls - 
        include - 函数将hrs应用中配置URL的文件包含到项目的URL配置中，并映射到hrs/路径下。
文件定义:
    project:
        manage.py - 一个让你可以管理Django项目的工具程序。
        settings.py - Django项目的配置文件。
        urls.py - Django项目的URL声明（URL映射），就像是你的网站的“目录”。
        wsgi.py - 项目运行在WSGI兼容Web服务器上的接口文件。
    app:
        __init__.py - 一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
        admin.py - 可以用来注册模型，用于在Django的管理界面管理模型。
        apps.py - 当前应用的配置文件
        migrations/ - 存放与模型有关的数据库迁移信息。
        models.py - 存放应用的数据模型，即实体类及其之间的关系（MVC/MTV中的M）。
        tests.py - 包含测试应用各项功能的测试类和测试函数。
        views.py - 处理请求并返回响应的函数（MVC中的C，MTV中的V）。

配置项:
    LANGUAGE_CODE - 设置语言代码
    TIME_ZONE - 设置时区

python manage.py 命令
    runserver - 启动Django自带服务器
    migrations - 生成数据库迁移文件
        可选项 - appName 只生成appName应用下迁移文件
    migrate - 执行迁移文件
    createsuperuser - 创建后台管理用户
    shell - 进入应用执行环境

model 定义模型
    class Meta 
        abstract - 设置为True时模型是抽象父类
        app_label - 如果定义模型的应用不在INSTALLED_APPS中可以用该属性指定
        db_tablespace - 模型使用的数据表空间
        db_table - 模型使用的数据表名称
        default_related_name - 关联对象回指这个模型时默认使用的名称，默认为<model_name>_set
        get_latest_by - 模型中可排序字段的名称。
        managed - 设置为True时，Django在迁移中创建数据表并在执行flush管理命令时把表移除
        order_with_respect_to - 标记对象为可排序的
        ordering - 对象的默认排序
        permissions - 创建对象时写入权限表的额外权限
        default_permissions - 默认为('add', 'change', 'delete')
        unique_together - 设定组合在一起时必须独一无二的字段名
        index_together - 设定一起建立索引的多个字段名
        verbose_name - 为对象设定人类可读的名称
        verbose_name_plural	- 设定对象的复数名称
    字段类型(字段名不能是Python的保留字，否则会导致语法错误,字段名不能有多个连续下划线，否则影响ORM查询操作)
        AutoField - 定义自增字段
        BigIntegerField - 64位有符号整数
        BinaryField - 存储二进制数据的字段，对应Python的bytes类型
        BooleanField - 存储True或False
        DateField - 存储日期，有auto_now和auto_now_add属性
        DateTimeField - 存储日期和日期，两个附加属性同上
        DecimalField - 存储固定精度小数，有max_digits（有效位数）和decimal_places（小数点后面）两个必要的参数
        DurationField - 存储时间跨度
        EmailField - 与CharField相同，可以用EmailValidator验证
        FileField - 文件上传字段
        FloatField - 存储浮点数
        ImageField - 其他同FileFiled，要验证上传的是不是有效图像
        IntegerField - 存储32位有符号整数。
        GenericIPAddressField - 存储IPv4或IPv6地址
        NullBooleanField - 存储True、False或null值
        PositiveIntegerField - 存储无符号整数（只能存储正数）
        SlugField - 存储slug（简短标注）
        SmallIntegerField - 存储16位有符号整数
        TextField - 存储数据量较大的文本
        TimeField - 存储时间
        URLField - 存储URL的CharField
        UUIDField - 存储全局唯一标识符
    字段属性
        null - 数据库中对应的字段是否允许为NULL，默认为False
        blank - 后台模型管理验证数据时，是否允许为NULL，默认为False
        choices - 设定字段的选项，各元组中的第一个值是设置在模型上的值，第二值是人类可读的值
        db_column - 字段对应到数据库表中的列名，未指定时直接使用字段的名称
        db_index - 设置为True时将在该字段创建索引
        db_tablespace - 为有索引的字段设置使用的表空间，默认为DEFAULT_INDEX_TABLESPACE
        default - 字段的默认值
        editable - 字段在后台模型管理或ModelForm中是否显示，默认为True
        error_messages - 设定字段抛出异常时的默认消息的字典，其中的键包括null、blank、invalid、invalid_choice、unique和unique_for_date
        help_text - 表单小组件旁边显示的额外的帮助文本。
        primary_key - 将字段指定为模型的主键，未指定时会自动添加AutoField用于主键，只读
        unique - 设置为True时，表中字段的值必须是唯一的
        verbose_name - 字段在后台模型管理显示的名称，未指定时使用字段的名称
        ForeignKey: 多对一
            limit_choices_to - 值是一个Q对象或返回一个Q对象，用于限制后台显示哪些对象。
            related_name - 用于获取关联对象的关联管理器对象（反向查询），如果不允许反向，该属性应该被设置为'+'，或者以'+'结尾。
            to_field - 指定关联的字段，默认关联对象的主键字段。
            db_constraint - 是否为外键创建约束，默认值为True。
            on_delete - 外键关联的对象被删除时对应的动作,可取的值包括django.db.models中定义的:
                CASCADE - 级联删除。
                PROTECT - 抛出ProtectedError异常，阻止删除引用的对象。
                SET_NULL - 把外键设置为null，当null属性被设置为True时才能这么做。
                SET_DEFAULT - 把外键设置为默认值，提供了默认值才能这么做。
        ManyToManyField: 多对多
            symmetrical - 是否建立对称的多对多关系。
            through - 指定维持多对多关系的中间表的Django模型。
            throughfields - 定义了中间模型时可以指定建立多对多关系的字段。
            db_table - 指定维持多对多关系的中间表的表名。
    
model 操作模型
    ModelName() - 定义一个新模型
    save() - 保存模型到数据表
    modelName_set - 根据外键反查
    all() - 查询模型所有数据
    get() - 查询单条数据
    delete() - 删除数据（返回删除数据）
    order_by('fieldName') - 根据fieldName排序（升序） '-fieldNmae'（倒序） 
    filter() - 根据条件查询模型
        fieldName = ?? - 查询模型fieldName等于??的数据
        fileName_contains = ?? - 查询fieldName中包含??的数据(模糊查询)
        fieldName__gt=10 - 查询fieldName大于10的数据
        fieldName__lt=20 - 查询fieldName小于20的数据
        fieldName_range=(10, 20) - 查询fieldName在10 - 20 范围内的数据
        pk=1 - 查询主键为1的数据
        exact / iexact：精确匹配/忽略大小写的精确匹配查询
        contains / icontains / startswith / istartswith / endswith / iendswith：基于like的模糊查询
        in：集合运算
        gt / gte / lt / lte：大于/大于等于/小于/小于等于关系运算
        range：指定范围查询（SQL中的between…and…）
        year / month / day / week_day / hour / minute / second：查询时间日期
        isnull：查询空值（True）或非空值（False）
        search：基于全文索引的全文检索
        regex / iregex：基于正则表达式的模糊匹配查询
        使用Q对象查询demo:
            from django.db.models import Q
            Emp.objects.filter(
                Q(name__startswith='张'),
                Q(sal__gte=5000) | Q(comm__gte=1000)
            ) # 查询名字以“张”开头且工资大于等于5000或补贴大于等于1000的员工


admin 管理后台
    register - 注册模型到admin管理
    模型管理类
        list_display - 显示字段
        ordering - 排序字段
        search_fields - 搜索字段



"""