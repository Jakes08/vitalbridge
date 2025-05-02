import logging, os, stripe
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@login_required
def payment(request):
    if request.method == 'POST':
        method = request.POST.get('payment_method')
        if method == 'credit_card':
            try:
                token = request.POST.get('stripeToken')
                charge = stripe.Charge.create(
                    amount=5000,  # Example: $50.00 in cents
                    currency='usd',
                    description='VitalBridge Consultation Payment - Credit Card',
                    source=token,
                )
                messages.success(request, "Credit card payment successful!")
                return redirect('dashboard')
            except stripe.error.CardError as e:
                logger.error("Stripe card error: %s", e)
                messages.error(request, "Credit card was declined.")
            except Exception as e:
                logger.error("Stripe error: %s", str(e))
                messages.error(request, f"Payment processing error: {str(e)}")
        elif method == 'mpesa':
            # Stub for MPesa integration (implement Safaricom API in production)
            messages.success(request, "MPesa payment processed successfully (stub)!")
            return redirect('dashboard')
        elif method == 'paypal':
            # Stub for PayPal integration (implement PayPal REST SDK in production)
            messages.success(request, "PayPal payment processed successfully (stub)!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid payment method selected.")
    return render(request, 'payments/payment.html', {
        'stripe_publishable_key': os.getenv('STRIPE_PUBLISHABLE_KEY')
    })
