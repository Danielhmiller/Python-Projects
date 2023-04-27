from django.shortcuts import render


# This function will render the Homepage when requested
def home(request):
    return render(request, 'Checkbook/CheckbookTemplates/checkbook/index.html')
#This function will render the Create New Account page when requested
def create_account(request):
    return render(request, 'Checkbook/CheckbookTemplates/checkbook/CreateNewAccount.html')
#This function will render the Balance page when requested
def balance(request):
    return render(request, 'Checkbook/CheckbookTemplates/checkbook/BalanceSheet.html')
#This function will render the transaction page when requested
def transaction(request):
    return render(request, 'Checkbook/CheckbookTemplates/checkbook/AddTransaction.html')



