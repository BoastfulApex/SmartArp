import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from apps.checking.forms import *


@login_required(login_url="/login/")
def index(request):
    date = datetime.date.today()
    data = []
    prodjects = Project.objects.all()
    for project in prodjects:
        checked = []
        plans_today =ContentPlan.objects.filter(project__id=project.id, date=date)
        print(plans_today) 
        if not plans_today:
            continue
        else:
            project_name = project.project_name
            manager = project.manager
            t_plan_type = ""
            i_plan_type = ""
            f_plan_type = ""
            y_plan_type = ""
            t_plan_status = "success"
            i_plan_status = "success"
            f_plan_status = "success"
            y_plan_status = "success"
            t_post_type = ""
            i_post_type = ""
            f_post_type = ""
            y_post_type = ""
            day_success = False
            telegram = Sotsial.objects.filter(sotsial_name="Telegram").first()
            facebook = Sotsial.objects.filter(sotsial_name="Facebook").first()
            instagram = Sotsial.objects.filter(sotsial_name="Instagram").first()
            youTube = Sotsial.objects.filter(sotsial_name="YouTube").first()
            for plan_today in plans_today:
                if int(plan_today.sotsial.id) == int(telegram.id):
                    t_plan_type = plan_today.post_type.post_type
                elif int(plan_today.sotsial.id) == int(instagram.id):
                    i_plan_type = plan_today.post_type.post_type
                elif int(plan_today.sotsial.id) == int(facebook.id):
                    f_plan_type = plan_today.post_type.post_type
                elif int(plan_today.sotsial.id) == int(youTube.id):
                    y_plan_type = plan_today.post_type.post_type
            posts_today = PostCheck.objects.filter(project__id=project.id, date=date) 
            if not posts_today:
                day_success = False
            else:
                day_success = True
                for post_today in posts_today:
                    if int(post_today.sotsial.id) == int(telegram.id):
                        t_post_type = post_today.post_type.post_type
                    elif int(post_today.sotsial.id) == int(instagram.id):
                        i_post_type = post_today.post_type.post_type
                    elif int(post_today.sotsial.id) == int(facebook.id):
                        f_post_type = post_today.post_type.post_type
                    elif int(post_today.sotsial.id) == int(youTube.id):
                        y_post_type = post_today.post_type.post_type
            if t_plan_type != t_post_type:
                day_success = False
            if f_plan_type != f_post_type:
                day_success = False
            if i_plan_type != i_post_type:
                day_success = False
            if y_plan_type != y_post_type:
                day_success = False
            checked = {
                "project_name": project_name,
                "manager": manager,
                "day_success": day_success,
                "t_plan_type": t_plan_type,
                "i_plan_type": i_plan_type,
                "f_plan_type": f_plan_type,
                "y_plan_type": y_plan_type,
                "t_post_type": t_post_type,
                "i_post_type": i_post_type,
                "f_post_type": f_post_type,
                "y_post_type": y_post_type,
            }
        data.append(checked)    
        
    context = {
        "data": data
    }
    print(data)
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]
        print(request.path.split('/')[-1])

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


# def main(request):
#     content = {
        
#     }
#     return render(request, 'home/type_update.html', content)

def plan_create(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post_type = []
            print(form.data)
            sotsial = []
            history = False
            proekt = Project.objects.get(id=form.data["project"])
            if "i_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="Instagram").first()
                if form.data["i_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["i_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["i_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["i_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["i_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                if "i_history" in form.data:
                    history = True
                post = ContentPlan.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
                
            if "f_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="Facebook").first()
                if form.data["f_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["f_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["f_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["f_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["f_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                if "f_history" in form.data:
                    history = True
                post = ContentPlan.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
            if "y_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="YouTube").first()
                if form.data["y_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["y_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["y_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["y_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["y_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                if "y_history" in form.data:
                    history = True
                post = ContentPlan.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
            if "t_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="Telegram").first()
                if form.data["t_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["t_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["t_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["t_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["t_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                post = ContentPlan.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
                                
            return redirect('home')
    else:
        form = AddContentPlanForm()

    return render(request,
                'home/plan_add.html',
                {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post_type = []
            sotsial = []
            history = False
            proekt = Project.objects.get(id=form.data["project"])
            if "i_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="Instagram").first()
                if form.data["i_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["i_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["i_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["i_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["i_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                if "i_post_history" in form.data:
                    history = True
                post = PostCheck.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
                
            if "f_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="Facebook").first()
                if form.data["f_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["f_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["f_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["f_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["f_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                if "f_history" in form.data:
                    history = True
                post = PostCheck.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
            if "y_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="YouTube").first()
                if form.data["y_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["y_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["y_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["y_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["y_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                if "y_history" in form.data:
                    history = True
                post = PostCheck.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
            if "t_post_type" in form.data:
                sotsial = Sotsial.objects.filter(sotsial_name="Telegram").first()
                if form.data["t_post_type"] == "carusel":
                    post_type = PostType.objects.filter(post_type='Karusel').first()
                if form.data["t_post_type"] == "simple":
                    post_type = PostType.objects.filter(post_type='Simple').first()
                if form.data["t_post_type"] == "motion":
                    post_type = PostType.objects.filter(post_type='Motion').first()
                if form.data["t_post_type"] == "video":
                    post_type = PostType.objects.filter(post_type='Video').first()
                if form.data["t_post_type"] == "reels":
                    post_type = PostType.objects.filter(post_type='Reels').first()
                post = PostCheck.objects.create(
                    project=proekt,
                    post_type=post_type,
                    sotsial=sotsial,
                    date=form.data["date"],
                    history=history
                )
                post.save()
                                
            return redirect('home')
    else:
        form = AddPostForm()

    return render(request,
                'home/post_add.html',
                {'form': form})
