from django.shortcuts import render, redirect
from finanaly.models import user, pocket
from finanaly.form import UserForm, LoginForm
from finanaly import crawler, crawler_article
import pandas as pd


# 登入頁面-輸入帳號、密碼登入
def login(request):
    if request.method == 'POST':
        userform = LoginForm(request.POST)
        if userform.is_valid():
            email = userform.cleaned_data['useremail']
            password = userform.cleaned_data['userpassword']
            if user.objects.filter(useremail=email, userpassword=password) and request.session['name'] == "":
                request.session['name'] = user.objects.get(useremail=email).username
                request.session['status'] = True
                status = True
                return redirect('/index/')
            elif request.session['name'] != "":
                status = True
                return redirect('/index/')
            else:
                request.session['name'] = ""
                request.session['status'] = False
                message = '登入失敗，請重新輸入資料'
                status = False
        else:
            request.session['name'] = ""
            request.session['status'] = False
            message = '驗證失敗，請重新輸入資料'
            status = False
    else:
        request.session['name'] = ""
        request.session['status'] = False
        userform = LoginForm(request.POST)
        message = '請輸入暱名、電子郵件、密碼 !'
        status = False
    return render(request, "login.html", locals())


# 註冊頁面-輸入帳號、密碼、暱稱
def register(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            useremail = userform.cleaned_data['useremail']
            userpassword = userform.cleaned_data['userpassword']
            try:
                unit = user.objects.create(username=username, useremail=useremail, userpassword=userpassword)
                unit.save()
                return redirect('/login/')
            except:
                message = '此帳號或密碼或暱名已被註冊，請重新輸入資料'
        else:
            message = '驗證錯誤，請重新輸入資料'
    else:
        message = '請輸入暱名、電子郵件、密碼 !'
        userform = UserForm()
    return render(request, "register.html", locals())


# 首頁頁面-目前打算顯示出目前瀏覽器中最熱門之文章(關於書籍)
def index(request):
    # 判斷有無登入
    if request.session['status']:
        status = True
        name = request.session['name']
    else:
        status = False
    # 將網頁爬取文章彙集成一資料表，並傳回網頁
    articledf = crawler_article.okapi()

    # try:
    #    page = request.GET.get('page', 1)
    # except PageNotAnInteger:
    #    page = 1
    # p = Paginator(all_orgs, 5, request=request)
    # orgs = p.page(page)

    # 將瀏覽量進行排序
    articledf = articledf.sort_values(by="browse", ascending=False)
    return render(request, "index.html", locals())


# 搜尋後頁面-回傳搜尋商品在各電商平台價格表現
def search(request):
    # 判斷有無登入
    if request.session['status']:
        status = True
        name = request.session['name']
    else:
        status = False
    # 取得搜尋值
    target = request.GET.get('search', '')
    # 將各網頁爬取資料彙集成一資料表，並傳回網頁
    # goodsdf = pd.concat([crawler.books(target), crawler.tanlong(target), crawler.kingstone(target), crawler.eslite(target), crawler.tcsb(target)], ignore_index=True)
    goodsdf = pd.concat([crawler.books(target), crawler.tanlong(target)], ignore_index=True)
    goodsdf = goodsdf.dropna(subset=['商品價格'])
    goodsdf = goodsdf.sort_values(by="商品價格", ascending=True)
    return render(request, "search.html", locals())


# 我的收藏-顯示所有過去收藏的清單列表
def pocketlist(request):
    # 判斷有無登入
    if request.session['status']:
        status = True
        name = request.session['name']
        # 取得收藏連結
        if request.method == "POST":
            targeturl = request.POST['url']
            targetname = request.POST['name']
            name = request.session['name']
            try:
                unit = pocket.objects.create(username=request.session['name'], url=targeturl, name=targetname)
                unit.save()
            except:
                error = "您已收藏過此文章或商品了！"
        try:
            query = pocket.objects.filter(username=request.session['name'])
        except:
            error = "您還未收藏任何商品或文章哦！"
    else:
        status = False
        return redirect('/login/')

    return render(request, "pocketlist.html", locals())


# 商品詳細頁面-回傳商品在各電商平台詳細表現--本次報告未做出，以後努力
def goods(request):
    return render(request, "goods.html", locals())
