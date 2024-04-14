# encoding=utf-8

# 分页参考链接 https://www.cnblogs.com/wj-1314/p/10620178.html
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from exam_system.settings import REST_FRAMEWORK
from django.http import JsonResponse as JR
import re
def paginator(request, model_cls, order, attrs=[], filter={}):
    '''def test_paginator2(request):
    # return paginator(request, User, 'create_time',
    #                  attrs=['name', 'stu_id', 'tel', 'id_card', 'email', 'avatar', 'create_time', 'role', 'is_staff', 'is_active']
    #                  )
    return paginator(request, ExamQuestion, 'question_database',
                     attrs=['question_type', 'reference_answer', 'question_name', 'question_database', ],
                     filter={ 'question_type': "简答",
                              'reference_answer': "是由于服务器执行命令但是过滤不严谨，攻击场景可举例靶场环境中的 ping ip 的问题，网站本身希望留存探活功能，输入ip然后ping，但实际payload 诸如  ping 127.0.0.256 || ifconfig 可以绕过服务器的原本本意的ping命令，执行自己的ifconfig等自己的系统命令。"
                              },
                     )
    '''
    ret = dict()

    PAGE_SIZE = REST_FRAMEWORK['PAGE_SIZE']

    # input your model & queryset
    if filter=={}:
        queryset = model_cls.objects.all().order_by(order)
    else:
        queryset = model_cls.objects.filter(**filter).order_by(order)

    paginator = Paginator(queryset, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1) # 如果传入page参数不是整数，默认第一页
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    is_paginated = True if paginator.num_pages > 1 else False

    results = []
    for singleObj in page_obj.object_list:
        result = {}
        for attr in attrs:
            if hasattr(singleObj, attr):
                result[attr] = getattr(singleObj, attr)
        results.append(result)

    full_url = request.build_absolute_uri()

    # next
    if not page_obj.has_next():
        page_next = None
    else:
        # page_next = full_url + page.next_page_number()
        if type(page)==int:
            page_next = re.sub("(page=)(\d+)", r"\g<1>" + str(page_obj.next_page_number()), full_url)
        else:
            # 假设 full_url 是你的原始 URL，例如 http://example.com/api/test_paginator/?page=1
            # 解析 URL，提取出查询参数部分
            from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
            url_parts = urlparse(full_url)
            query_params = parse_qs(url_parts.query)
            # 设置新的查询参数
            query_params['page'] = page_obj.next_page_number()
            # 重新构建 URL
            new_query_string = urlencode(query_params, doseq=True)
            new_url_parts = url_parts._replace(query=new_query_string)
            page_next = urlunparse(new_url_parts)
    # previous
    if not page_obj.has_previous():
        page_previous = None
    else:
        page_previous = re.sub("(page=)(\d+)", r"\g<1>" + str(page_obj.previous_page_number()), full_url)

    # return columns
    # count next:null previous:null results:[]
    ret.update({
        'count': paginator.count,
        'next': page_next,
        'previous': page_previous,
        'results': results,
    })
    return JR(ret)
