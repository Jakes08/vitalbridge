# VitalBridge

VitalBridge is a comprehensive telemedicine platform that connects doctors and patients securely with real-time video consultations, appointment booking, secure messaging, and more.

## Features

- **User Authentication & Role Management** (Custom Django model & Firebase Auth)
- **Appointment Booking** with a real-time calendar
- **Video Consultations** (Twilio integration)
- **EHR Integration** (FHIR API stub)
- **Multi-Payment Options:** MPesa (stub), Credit Card via Stripe, and PayPal (stub)
- **Real-Time Messaging** (via Django Channels)
- **Hydration Reminders** (Celery tasks)
- **Analytics Dashboard** & Admin Panel
- **Multilingual Support** (English and Swahili)
- **Mobile Responsive UI** (TailwindCSS)
- **Captivating UI/UX:** Custom fonts, animations, and branding

## Monetization Strategy

- **Subscriptions:** Premium memberships with advanced features.
- **Per-Consultation Fees:** Charge per telemedicine session.
- **White-Label Licensing:** Offer the platform to hospitals and healthcare organizations.
- **In-App Advertising & Additional Services:** E-prescriptions, pharmacy integrations, etc.

## Setup

### Backend (Django)

1. Create a `.env` file in the root directory with the following variables:

DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_API_KEY=your_twilio_api_key
TWILIO_API_SECRET=your_twilio_api_secret
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_public_key
EHR_API_URL=<https://api.exampleehr.com/patientrecords>
EMAIL_USER=<your_email@example.com>
EMAIL_PASSWORD=your_email_password
SENTRY_DSN=your_sentry_dsn
