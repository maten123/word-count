#from django.http import HttpResponse
#from django.http import render   #递交客户发送的内容
from django.shortcuts import render


def home(request):
    #return HttpResponse('Hello World!,爱上你，我想让整个空气都变得新鲜！')
    return render(request, 'home.html')  #下一步创建html，放在templates文件夹中

def wordcount(request):
    user_text = request.GET['text'] #GET来获取
    total_count = len(user_text)

    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1 #没有就将它创建添加进去
        else:
            word_dict[word] += 1
    sorted_dict = \
        sorted(word_dict.items(),key= lambda x:x[1],reverse = True)

    return render(request,'wordcount.html',
                  {'count': total_count,'text': user_text,'wordict': word_dict,'sorted': sorted_dict})