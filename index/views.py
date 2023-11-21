from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ToDoForm
from .models import ToDoModel

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def __init__(self):
        self.params = {
            'form': ToDoForm(),
            'message': "please input to_do_list",
            'object_list': ToDoModel.objects.all(),
        }

    def get(self, request):
        return render(request, self.template_name, self.params)

    def post(self, request):

        print(request.POST)
        if 'add' in request.POST:
            self.params['form'] = ToDoForm(request.POST)
            if self.params['form'].is_valid():
                self.params['form'].save(commit=True)
                self.params['message'] = "complete addition"
                return render(request, self.template_name, self.params)
            else:
                self.params['message'] = "form is not valid"
                return render(request, self.template_name, self.params)
        elif 'del' in request.POST:
            todo = ToDoModel.objects.filter(id=request.POST['id'])
            todo.delete()
            self.params['message'] = "complete delete"
            return render(request, self.template_name, self.params)






