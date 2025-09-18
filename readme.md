
项目停止：由于本大型考务、视频教学系统已经部署在甲方单位系统，故于2024年初停止公开进行。

Readme写得很简单，如果有想基于本项目代码继续进行研究的同学可以参考[后端](https://github.com/SenRanja/es_backend)与[前端](https://github.com/SenRanja/es_front)，以及对应的**开发手册**与**用户手册**。

如果希望合作开发新的系统，可以通过提Issue联系我合作。


# TODO

- [ ] 13/09/2024 最新平台已放在服务器`/root/exam_system_2024_09_13`目录中。解决当日license不更新问题，由于license长时间未更新导致。检查了数据库，虽然`exam_question`表中的`subject_id`由于旧有数据库导入，依然是外联字段而非`char`字段，需要进行修正。但是由于model ExamQuestion的subject = models.CharField，因此实际上学科与题库脱钩。导入数据的学科格式不符合为NULL，因此没有报错问题。

# 部署方式

### step1 

    git clone https://gitee.com/bochen1993/es_deploy.git
    cd es_deploy
    git submodule update --init --recursive
    git submodule update --remote

git submodule update 的操作比较耗费时间，以gitee为例，俩子仓库都得输入密码，否则需要 rm -rf es_deploy 目录重新上述步骤部署。

### step2

此步修改前端的API访问地址。

此步需要本机安装nodejs的编译环境，参考`https://nodejs.org/en/download/prebuilt-installer`。开发者本人的环境如下， 如果安装nodejs及npm，建议安装贴近版本。

    C:\Users\ranja>node -v
    v16.13.2

    C:\Users\ranja>npm -v
    8.1.2

进入 es_front 项目，修改`.env.production`中的`VITE_MEDIA_PREFIX_PATH='http://192.227.167.113/'`的URL地址（如访问 `http://192.227.167.113/`），改为客户需要被访问的IP地址。

手动删除`exam_system\deploy\es_front\node_modules`目录，然后执行命令`npm install`重新生成`node_modules`目录。

注意不要直接`npm run build`，参考文章 `https://github.com/xdlumia/vue3-video-play/issues/139` 对`vue3-video-play`报错组件进行修正后，再执行下一步命令：

本地（非服务器）进入ES_FRONT项目的vite.config.js所在目录，执行命令
    
    npm run build

构建出的**dist**手动复制到服务器的 ~/es_deploy/es_front 目录。

### step3

    docker-compose build && docker-compose up -d

如果有报错，使用`docker-compose logs`查看报错

### 移除镜像(希望重新构建前必须操作步骤)

    docker-compose down

# 如果更新字段

数据库是现成的，数据库文件直接在git仓库中，因此数据库无需初始化。这样做避免docker构建过程中的一些麻烦，并可以确保稳定性。

但是如果要更改数据库字段，千万不要直接进数据库改字段。本项目使用django的model方式同步在数据库中，你只需要清空数据库exam_system下全部表即可。

然后重新 docker-compose build 然后dcoker-compose up -d 项目即可。

backend会自动执行如下语句，来初始化数据库字段。

```shell
python manage.py makemigrations user video notice question_manage exam_manage exam_score license subject_manage module system_manage system_monitor ftp testonly
python manage.py migrate
```

部分初始化数据库字段的代码见 `deploy/tools/`
