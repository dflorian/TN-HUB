from django.urls import path
#from . import views
from.views import HomeView, PaperDetail, PaperSubmit, CategoryView, LikeView, \
				SearchResultsView, add_paper, MostVoted, PaperEdit, PaperDelete

urlpatterns = [
    path('', HomeView, name='home'),
    path('mostvoted', MostVoted, name='popular'),
    path('paper/<int:pk>', PaperDetail.as_view(), name='paper-detail'),
    path('edit/<int:pk>', PaperEdit.as_view(), name='paper-edit'),
    path('delete/<int:pk>', PaperDelete.as_view(), name='paper-delete'),
    path('submit_paper', add_paper, name='paper-submit'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_paper'),
    path('search/', SearchResultsView.as_view(), name='search_result'),
]
