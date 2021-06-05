from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views import View

from .models import questionModel, dataType
from taggit.models import Tag
# Create your views here.

class home(View):
    def get(self, request):
        datatype = dataType.objects.all()

        context = {
            "title":"Programmerly",
            "dataTypes": datatype,
            }
        return render(request, "codingquestions/mainpage.html", context)


class content(View):
    def get(self, request):
        data = questionModel.objects.all() 
        context = {"questions":data}
        return render(request, "codingquestions/content-page.html", context)

class blog(View):
    def get(self, request):
        data = questionModel.objects.all()
        context = {"posts":data}
        return render(request, "codingquestions/blog.html", context)

class blogView(View):
    def get(self, request, slug):
        data = questionModel.objects.get(slug=slug)
        context = {
            'question':data,
        }
        return render(request, "codingquestions/blogView.html", context)


class content1(View):
    def get(self, request,slug):
        data = dataType.objects.get(pk=slug)
        title = data.heading
        body = data.description
        questions = questionModel.objects.all()
        context = {}
        context["type"] = title
        context["heading"] = title
        context["body"] = body 
        context["flag"] = True
        context["questions"]=questions
        return render(request, "codingquestions/content.html",context)
    
class contentquestion(View):
    def get(self, request,slug):
        questions = questionModel.objects.all() 
        data = questionModel.objects.get(slug=slug)
        title = data.problemstmt
        body = data.description
        context = {}
        context["type"] = data.datastructure
        context["heading"] = title
        context["body"] = body 
        context["questions"]=questions
        return render(request, "codingquestions/content.html",context)
    
class all_questions(View):
    def get(self, request):
        questions = questionModel.objects.all()
        tags = Tag.objects.all()
        
        context = {
            "questions" : questions,
            "tags" : tags
        }
        return render(request, "codingquestions/questions_list.html", context)

class tagQuestionView(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        questions = questionModel.objects.filter(tags = tag)
        tags = Tag.objects.all()
        context = {
            "questions" : questions,
            "tags" : tags
        }
        return render(request, "codingquestions/questions_list.html", context)
    
class questionView(View):
    def get(self, request, slug):
        data = questionModel.objects.get(slug=slug)
        context = {
            'question':data,
        }
        return render(request, "codingquestions/blogView.html", context)





    
