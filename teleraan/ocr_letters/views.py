from django.shortcuts import render
from django.http.response import JsonResponse
from PIL import Image
import pytesseract
import json
from ocr_letters.models import ImageModel
# Create your views here.

#定义主函数
def main(request):
    return render(request,'main.html')

#定义返回视图
def result(request):
    #接收前端上传图片
    ocr_image = request.FILES.get('img')
    #处理图片与OCR识别
    ph=Image.open(ocr_image)
    s = pytesseract.image_to_string(ph,lang='eng')
    print(s)
    #返回识别数据
    data = {'content':[i for i in s if i.isalpha()]}#列表生成器 只留字母
    dic = {'image_bat':ocr_image.read(),'ocr_letter':data}
    ImageModel.objects.create(**dic)#与数据库交互
    return JsonResponse (data)#返回JSON数据

