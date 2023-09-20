from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toy
from .forms import MigrationsForm, FeedingForm




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

 return render(request, 'finches/index.html', 
               {
                 'finches': finches
               })


def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  #get all toys finch has
  id_list = finch.toys.all().values_list('id')
  #query for toys not in the list
  toys_cat_doesnt_have = Toy.objects.exclude(id__in=id_list)
  migrations_form = MigrationsForm()
  feeding_form = FeedingForm()
  return render(request, 'finches/details.html', 
        { 'finch':finch, 'migrations_form':migrations_form,'feeding_form': feeding_form, 'toys': toys_cat_doesnt_have
 })

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'region', 'description', 'diet']

class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

def add_migrations(request, finch_id):
  form = MigrationsForm(request.POST)

  if form.is_valid():
    new_migrations = form.save(commit=False)
    new_migrations.finch_id = finch_id
    new_migrations.save()
  return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id = finch_id)

def assoc_toy(request, finch_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)


  



