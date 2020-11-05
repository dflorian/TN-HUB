from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Paper, Category
from .forms import PaperForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q, Count
from django.contrib import messages

	
def CategoryView(request, cats):
	cat_id = Category.objects.filter(lookup_name=cats)
	category_paper = Paper.objects.filter(category=cat_id[0])
	return render(request, 'categories.html', {'cats':cats, 'category_paper':category_paper})
	

def LikeView(request, pk):
	paper = get_object_or_404(Paper, id=request.POST.get('paper_id'))
	voted = False
	if paper.votes.filter(id=request.user.id).exists():
		paper.votes.remove(request.user)
		voted = False
	else:
		paper.votes.add(request.user)
		voted = True
	
	return HttpResponseRedirect(reverse('paper-detail', args=[str(pk)]))


class SearchResultsView(ListView):
    model = Paper
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Paper.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
            | Q(description__icontains=query)
            | Q(keywords__icontains=query)
        )
        return object_list


def MostVoted(request):
	object_list = Paper.objects.annotate(q_count=Count('votes')) \
                                 .order_by('-q_count')[:7]
	return render(request, 'popular.html', {'object_list':object_list})


def HomeView(request):
	object_list = Paper.objects.all().order_by('-publication_date')
	return render(request, 'home.html', {'object_list':object_list})


class PaperDetail(DetailView):
	model = Paper
	template_name = 'paper_detail.html'

	def get_context_date(self, *args, **kwargs):
		paper = get_object_or_404(Paper, id=request.POST.get('paper_id'))
		#l = get_object_or_404(Paper, id=self.kwargs['pk'])
		total_votes = paper.total_votes()

		voted = False
		if paper.votes.filter(id=self.request.user.id).exists():
			voted = True

		context['total_votes'] = total_votes
		context['voted'] = voted
		return context


class PaperSubmit(CreateView):
	model = Paper
	form_class = PaperForm
	template_name = 'submit_paper.html'
	#fields = ('title', 'author', 'body', 'link', 'backend')


class PaperDelete(DeleteView):
	model = Paper
	template_name = 'paper_delete.html'
	success_url = reverse_lazy('home')


class PaperEdit(UpdateView):
	model = Paper
	template_name = 'paper_edit.html'
	form_class = PaperForm
	#fields = ('title', 'author', 'description', 'keywords', 'link', 'backend')


def add_paper(request):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.owner = request.user
            paper.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PaperForm()
    return render(request, 'submit_paper.html', {
        'form': form
    })
