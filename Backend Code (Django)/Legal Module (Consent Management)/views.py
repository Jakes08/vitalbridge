from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # type: ignore
from django.utils.translation import gettext as _

@login_required
def consent_form(request):
    if request.method == 'POST':
        # Process consent (stub)
        messages.success(request, _("Consent form submitted successfully."))
        return redirect('dashboard')
    return render(request, 'legal/consent_form.html')
