# encoding=utf-8


# test model
from paginator import paginator
from user.models import User
from question_manage.models import ExamQuestion


def test_paginator2(request):
    # return paginator(request, User, 'create_time',
    #                  attrs=['name', 'stu_id', 'tel', 'id_card', 'email', 'avatar', 'create_time', 'role', 'is_staff', 'is_active']
    #                  )
    return paginator(request, ExamQuestion, 'question_database',
                     attrs=['question_type', 'reference_answer', 'question_name', 'question_database', ],
                     filter={ 'question_type': "简答",
                              'reference_answer': "是由于服务器执行命令但是过滤不严谨，攻击场景可举例靶场环境中的 ping ip 的问题，网站本身希望留存探活功能，输入ip然后ping，但实际payload 诸如  ping 127.0.0.256 || ifconfig 可以绕过服务器的原本本意的ping命令，执行自己的ifconfig等自己的系统命令。"
                              },
                     )