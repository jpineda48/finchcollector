from django.shortcuts import render
from .models import Finch



# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

# Add new view
def finches_index(request):
  # We pass data to a template very much like we did in Express!
 finches = Finch.objects.all()
 print(finches)
 return render(request, 'finches/index.html', 
               {
                 'finches': finches
               })


def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/details.html', { 'finch':finch })
