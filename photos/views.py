from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Photo, Category
from .forms import CustomUserCreationForm



def registerPage(request):
    page = 'register'

    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])
            login(request, user)
            return redirect('gallery')

    context = {'page':page, 'form':form} 
    return render(request, 'photos/login_register.html', context)


def loginPage(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    context = {'page':page}
    return render(request, 'photos/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def gallery(request): 
    user = request.user

    category = request.GET.get('category')

    # print("Category :", category)

    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)

    context = {'categories':categories, 'photos':photos}
    return render(request, 'photos/gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo':photo}
    return render(request, 'photos/photo.html', context)


@login_required(login_url='login')
def addPhoto(request):
    user = request.user
    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.getlist('image')

        # print(data['category'])

        if data['category'] != 'none': 
            category = Category.objects.get(id=data['category'])

        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['new_category']
                )
        else:
            category = None
        
        Photo.objects.create(
            category = category,
            image = image,
            description = data['description'],
        )

        return redirect('gallery')
    
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

