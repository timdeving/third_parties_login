# third_parties_login
Simple login system via third parties (Yandex & Tg)

Yandex integration - https://oauth.yandex.com (Get ClientID and Client secret). For Redirect URI for web services - set to http://127.0.0.1:8000/accounts/yandex/login/callback/; 
Tg integration - https://core.telegram.org/widgets/login (Create own bot via Gotfather and and with coommand "/setdomain" set your domain for the bot http://127.0.0.1:8000).

Used django-allauth package, simply overrode login and logout templates (for simplification purposes) (Docs https://docs.allauth.org/en/latest/)

In settings.py set your keys for SOCIALACCOUNT_PROVIDERS

pip install django-allauth
pip install "django-allauth[socialaccount]"

<img width="419" height="173" alt="Screenshot 2025-07-25 at 5 05 55 PM" src="https://github.com/user-attachments/assets/f82b3a02-8a51-4d79-962e-adaf16158a23" />
