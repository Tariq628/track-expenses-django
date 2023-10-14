from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm


def expense_form(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("expenses_dashboard")
    else:
        form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {"form": form})


def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "expenses/dashboard.html", {"expenses": expenses})
