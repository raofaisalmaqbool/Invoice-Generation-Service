# Invoice Generator & Email Sender (Django)

A small Django application that lets a user select a product, enter buyer details, automatically generate an invoice, and send it by email.

## Features

- List products with basic details and pricing
- Capture buyer information and quantity
- Generate a simple invoice view with seller and buyer details
- Email the invoice as an HTML email using SMTP
- Environment-based configuration via `.env`

## Technology Stack

- Python 3.x
- Django 3.0.7
- SQLite (default dev database)
- `python-dotenv` for environment variable management
- Bootstrap 5 for UI styles

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd invoice-generate-send-to-email
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root (same folder as `manage.py`) if it does not already exist. Use these keys:

   ```env
   # Django secret key for cryptographic signing (change this in production)
   SECRET_KEY=change-me-in-production

   # Django debug flag: use True for local dev, False in production
   DEBUG=True

   # Comma-separated list of allowed hosts
   ALLOWED_HOSTS=localhost,127.0.0.1

   # SMTP email credentials used to send invoices
   EMAIL_USER=your-email@example.com
   EMAIL_PASS=your-email-app-password
   ```

   - In production, set `DEBUG=False` and update `ALLOWED_HOSTS` accordingly.
   - For Gmail, you may need an **app password** instead of your normal account password.

5. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   The app will be available at `http://127.0.0.1:8000/` by default.

## Usage

1. Open the home page and review the list of products.
2. Click **Buy Product** for a product.
3. Fill in your name, address, phone, email, and desired quantity.
4. Submit the form to generate an invoice and send it by email.
5. The invoice details will also be shown in the browser.

## Email Configuration Notes

- Email settings are configured in `email_invoice/settings.py` and read from environment variables.
- The project uses the Django SMTP backend and assumes Gmail by default:
  - `EMAIL_HOST = 'smtp.gmail.com'`
  - `EMAIL_PORT = 587`
  - `EMAIL_USE_TLS = True`
- Update these values if you use a different provider.

## Project Structure (high level)

- `email_invoice/` – Django project configuration (settings, URLs, WSGI/ASGI)
- `app/` – main application logic (models, views, admin)
- `templates/` – Django templates for base layout, product listing, purchase form, and invoice detail
- `static/` – static assets such as CSS (`static/css/styles.css`)
- `media/` – uploaded media files (e.g., product images)

## Notes

- Do **not** commit real secrets (e.g., `SECRET_KEY`, email passwords) to version control.
- `.env`, `db.sqlite3`, and media/uploads are ignored via `.gitignore`.
