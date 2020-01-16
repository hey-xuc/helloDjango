from django.contrib import admin

# Register your models here.
from hrs.models import Dept, Emp    # 导入要管理的模型

class DeptAdmin(admin.ModelAdmin):
    """
    注册部门模型管理类
    """
    list_display = ('no', 'name', 'location')    # 显示字段
    ordering = ('no',)  # 排序字段

class EmpAdmin(admin.ModelAdmin):
    """
    员工模型管理类
    """
    list_display = ('no', 'name', 'job', 'mgr', 'sal', 'comm', 'dept')
    search_fields = ('name', 'job')   # 搜索字段

admin.site.register(Dept, DeptAdmin)
admin.site.register(Emp, EmpAdmin)   
