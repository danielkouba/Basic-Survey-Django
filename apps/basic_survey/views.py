from django.shortcuts import render, redirect


# Create your views here.
def index(request):
	return render(request, 'basic_survey/index.html')

def submit(request):
	if request.method == 'POST':
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		return redirect('/success')
	return redirect('/')

def success(request):
	return render(request, 'basic_survey/success.html')

