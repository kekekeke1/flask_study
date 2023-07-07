from flask import escape, request, url_for
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


"""
上面就是flask的最小应用了
启动服务的方法：
1.先导入环境变量： $env:FLASK_APP = "hello.py"
2.启动服务： flask run --host=0.0.0.0
"""


@app.route('/hello')
def hello():
    return 'Hello, World1123'


"""
url上传递参数 <var> 就行
收参数的时候，可以加个 escape
escape()的作用
用户输入的数据会包含恶意代码，所以不能直接作为响应返回，需要使用 Flask提供的 escape()函数对 name 变量进行转义处理，比如把< 转换成 &lt;。这样在返回响应时浏览器就不会把它们当做代码执行
"""


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


"""
url_for的作用
url_for() 函数用于构建指定函数的 URL。它把函数名称作为第一个 参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量 将添加到 URL 中作为查询参数
"""


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


with app.test_request_context():
    # print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

""""
处理http的请求
"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    pass


def show_the_login_form():
    pass


""""
flaskr的启动命令：
在flaskr的上级目录下：
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV="development"
flask run --host=0.0.0.0

开启debug模式
$env:FLASK_DEBUG="True"
完事儿

再初始化数据库
flask init-db # 这个命令跟 db.py中的 click.command('init-db') 保持一致
"""

from functools import partial

def concat_args(param1, param2, param3, *args):
    param1 = str(param1)
    param2 = str(param2)
    param3 = str(param3)
    args = [str(arg) for arg in args]

    concat = {
        'a': partial(lambda args: f'"{param1} {param2} {param3} {" ".join(args)}"' if len(args) == 2 else AssertionError('参数数量错误！'), args),
        'b': partial(lambda args: f'"{param1} {param2} {param3} {" ".join(args)}"' if len(args) == 1 else AssertionError('参数数量错误！'), args),
        'c': partial(lambda args: f'"{param1} {param2} {param3} {" ".join(args)}"' if len(args) == 3 else AssertionError('参数数量错误！'), args),
    }.get(param1, partial(lambda args: AssertionError('无效的第一个参数！'), args))(args)

    another_function(concat)  # 将拼接后的字符串传递给另一个函数

# 示例用法
def another_function(value):
    print(f"传递给另一个函数的值：{value}")

concat_args('a', 1, 2, 3, 4)         # 输出: 传递给另一个函数的值："a 1 2 3 4"
concat_args('b', 5, 6, 7)            # 输出: 传递给另一个函数的值："b 5 6 7"
concat_args('c', 8, 9, 10, 11, 12)   # 输出: 传递给另一个函数的值："c 8 9 10 11 12"
concat_args('a', 13, 14, 15)         # 输出: AssertionError: 参数数量错误！
concat_args('b', 16, 17, 18, 19)     # 输出: AssertionError: 参数数量错误！
concat_args('d', 20, 21, 22)         # 输出: AssertionError: 无效的第一个参数！
