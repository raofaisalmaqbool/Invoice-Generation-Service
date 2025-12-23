from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import buyer, producat, seller


# Display list of available products on the home page
def index(request):
    products = producat.objects.all()
    sellers = seller.objects.all()
    return render(request, 'index.html', {'products': products, 'seller': sellers})


# Handle purchase form submission and send invoice email
def buy(request, pk):
    product = get_object_or_404(producat, pk=pk)

    if request.method == "POST":
        # Read and normalize form data from POST request
        name = request.POST.get('name', '').strip()
        address = request.POST.get('address', '').strip()
        phone = request.POST.get('phone', '').strip()
        recipient_email = request.POST.get('email', '').strip()
        quantity_raw = request.POST.get('quantity', '1').strip()

        # Validate quantity as a positive integer
        try:
            quantity = int(quantity_raw)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            error_message = "Quantity must be a positive whole number."
            return render(request, 'buy.html', {'product': product, 'error_message': error_message})

        # Ensure required fields are provided
        if not all([name, address, phone, recipient_email]):
            error_message = "Please fill in all required fields before submitting."
            return render(request, 'buy.html', {'product': product, 'error_message': error_message})

        # Create buyer record for this purchase
        purchase = buyer.objects.create(
            name=name,
            address=address,
            phone=phone,
            email=recipient_email,
        )

        # Prepare invoice data for template rendering
        amount = float(product.price)
        product_name = product.name
        product_description = product.dis
        price_per_unit = amount
        total_quantity = quantity
        grand_total = amount * quantity
        sellers = seller.objects.all()

        data = {
            'id': purchase.pk,
            'purchase_date': purchase.purchase_date,
            'p_name': product_name,
            'p_price': price_per_unit,
            'email': recipient_email,
            'b_name': name,
            'b_address': address,
            'b_phone': phone,
            'p_dis': product_description,
            'p_quantity': total_quantity,
            'p_total': grand_total,
        }

        # Render HTML invoice content for email and on-screen display
        html_content = render_to_string("detail.html", {'data': data, 'seller': sellers})
        text_content = strip_tags(html_content)

        # Attempt to send invoice email to the buyer
        try:
            email_message = EmailMultiAlternatives(
                subject='Product Invoice',
                from_email=settings.EMAIL_HOST_USER,
                to=[recipient_email],
                body=text_content,
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()
            msg = "Invoice sent successfully."
        except Exception:
            msg = "Invoice saved but email could not be sent. Please try again later."

        return render(request, 'detail.html', {'data': data, 'seller': sellers, 'msg': msg})

    # Render empty purchase form for GET requests
    return render(request, 'buy.html', {'product': product})


