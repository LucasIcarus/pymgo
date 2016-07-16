用tornado简单搭了一个WEB框架，大概下面四个部分，填东西找到对应的位置就好了，没有的话自己加上。

Models ,实体类，类似User这样的类放在这边

Views，视图，后端的数据处理部分，所有跟前端有交互的模块放在这个部分，可以开二级文件夹扩展。

Static，静态文件，有几个部分，JS、CSS、FONTS、IMG根据字面意思放对应的文件，template放HTML文件（前端这边我不是特别懂，有什么遗漏的可以自己开文件夹扩展）

Common,一些公用的服务，目前只有创建数据库连接在这里。不涉及具体业务，但是又要在不同模块使用的，一般放在这边。

另外在根目录下有一些文件，解释一下。

.gitignore git用的

Config.py 主要是一些静态变量

Gruntfile.js 前端管理工具，基于Node.js

Package.json 上面那个文件的依赖环境

Index.py 服务主程序，运行这段代码就可以开启服务

Requirement.txts python依赖，可以通过  pip install -r requirements.txt一键安装所有环境，添加了新环境的话，务必在这个文件中加入相应字段。

Session.py 一个简单的session实现，基于redis。

Urls.py  路由配对和requests.setting的配置。




Tornado框架下的基本开发步骤。

    ⒈新建一个handler类，继承tornado.web.RequestHandler类，这个类封装了HTTP协议，Socket等。

    2.在这个类中定义一个Get或Post函数。

    3.写业务逻辑，从已经加载到handler父类中的setting配置读取数据库。

    4.使用self.write()方法将结果返回（除非确保正确，否则不要重写这个方法）。

    5.在urls.py中将这个Handler配对到对应的静态文件中（可以参考示例）。

    6.前端接收到结果，做处理···,呈现到页面上。