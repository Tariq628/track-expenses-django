from django.urls import path
from . import views

urlpatterns = [
    # ... your other URL patterns
    path('expenses-dashboard', views.dashboard, name='expenses_dashboard'),
    path('add-expense', views.expense_form, name='add_expense'),
]
