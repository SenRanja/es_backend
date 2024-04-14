# 后端

### TODO

* 考试的models已做完，就剩主观题评分的功能view未做 + 多选策略（少选是否得分）
* 功能模块 module的app 的功能怎么关联到前端，参考前端的 ruleNames 和 菜单栏
* video模块

```
模块管理

1. 一级菜单模块
如 首页、用户管理、学科管理

字段
name descrption

2. 二级菜单模块
如 用户管理 下有 导入用户、用户更改 栏

字段
表1外键 name descrption
表1外键 name descrption

3. 鉴权
方法： 根据guardian，对group、user可assign_perm权限，对象级权限或应用级权限


乱序序列 按照 自定义序列 排序方法
custom_order = ['校长', '副校长', '教授', '副教授', '教职工', '学生']
unordered_list = ['学生', '教职工', '校长']
sorted_list = sorted(unordered_list, key=lambda x: custom_order.index(x))



------

一场考试 对应 多个学生的试卷和答题

考试管理：
考试命名：
考试类型：考试 or 模拟
开始考试时间：
结束考试时间：
考试时长：自动计算分钟
考试管理创建时间：
考试管理最后一次修改时间：
满分值设置
考试管理封存（考试完了，永不可动）：flag

对谁可见状态：考试前 or 考试中 or 考试结束
对谁可见： 用户 or group  （谁来参加考试，谁可见），权限操作


题库选择
根据 题目类型、难易程度、题目数量 来存储单条，如：
考试管理id  --  题库id  --  单选  -- 简单 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  单选  -- 中等 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  单选  -- 难 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  多选  -- 简单 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  多选  -- 中等 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  多选  -- 难 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  论述  -- 简单 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  论述  -- 中等 -- 题目数量 -- 单个题目分值设置
考试管理id  --  题库id  --  论述  -- 难 -- 题目数量 -- 单个题目分值设置

成绩管理（app）
1. 判分系统
    客观成绩评分（待商议，多选题 选错 少选是否得分），直接入库
    主观成绩评分（暂不做）
2. 学生主观题答卷存储
    因为主观题不自动算分，因此需要存入db，让老师看系统判分

题库（app）[done]
试题model

学科管理（app）
学科名字（unique=True）
相关教师组（即group）
创建时间
描述




视频管理
上传视频俩接口：
1. video 存储视频名字
2. 单独的文件上传，系统自行重新命名

```


### 部署

```shell
makemigrations user video notice question_manage exam_manage exam_score license subject_manage module system_manage system_monitor ftp testonly
migrate
```

### 技术架构

django
DRF

需求：姓名、性别、学号、手机号、身份证、邮箱、密码、所属组

### 用户操作

##### 用户模型操作

`http://127.0.0.1:8000/api/user/`

DRF的rest api

##### 注册普通用户

`http://127.0.0.1:8000/api/register/`

```json
{
  "password": "password123",
  "name": "Jane Smith",
  "stu_id": "123456789",
  "tel": "9876543210",
  "id_card": "987654321012345678",
  "email": "jane.smith@example.com"
}
```

##### 注册超级用户

`http://127.0.0.1:8000/api/register/`

```json
{
  "password": "admin",
  "name": "申晏键",
  "stu_id": "001",
  "tel": "18536864913",
  "id_card": "141181199904230017",
  "email": "shenyanjian@gmail.com",
  "super": true
}
```

### video DRF操作model

DELETE方法，**不要忘记api的pk后面需要带斜杠**：

```DELETE /api/video/14/ HTTP/1.1
Host: 127.0.0.1:8000
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html; q=1.0, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://127.0.0.1:8000/api/video/
Content-Type: application/json
X-CSRFTOKEN: 5C5YQ5f14fJ7UO0QSnSqet01i2mKiIqh2DJtsryA1Z3juT2LR7Fy2cuOCwrsJ9nn
X-Requested-With: XMLHttpRequest
Content-Length: 0
Origin: http://127.0.0.1:8000
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

```

### 菜单管理

参考飞书文档

### 防止源码泄露

使用pyarmor进行源码加密，再部署。

### 容器部署

python:3.7  903MB
后需要改为更小的ubuntu来部署

### license

使用license生成器生成1-719天的license（超过此范围天数，license无效）

系统可运行时间是多license累计天数，超过提交过的license累计天数，系统过期。系统若过期，仅允许管理员用户登录，管理员需要提交新的license运行系统。

系统部署后，如果由于使用者逆向、停机等原因，导致系统license失效（即可能系统检测自己有36小时未运行），此时管理员需要提交一个新的license来重新激活系统（此情况建议给一两天的license即可）

### 定时任务脚本

每小时运行`/scripts/time_add.py`










