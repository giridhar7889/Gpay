from django.shortcuts import render

def auth(request):

    if request.method == 'POST':
        phone_num = request.POST['phonenumber']
        print(phone_num)

        return render(request, "index.html")

    return render(request, "index.html")
