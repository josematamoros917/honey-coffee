from django.shortcuts import render, redirect, get_object_or_404
from .models import SocialMedia, Store, Category, Product, ContactMessage
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def home(request):
    # Obtén la tienda (o la única tienda en tu sistema)
    store = Store.objects.first()  # Asegúrate de que solo haya una tienda o usa el método adecuado
    
    # Obtén los íconos de redes sociales asociados a la tienda
    social_medias = SocialMedia.objects.filter(store=store)
    
    # Obtén todas las categorías
    categories = Category.objects.all()

    return render(request, 'core/home.html', {
        'social_medias': social_medias,
        'categories': categories,  # Añade las categorías al contexto
    })
    
    

def productos(request, category_id=None):
    # Obtén los íconos de redes sociales asociados a la tienda
    store = Store.objects.first()
    social_medias = SocialMedia.objects.filter(store=store)
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(categories=selected_category)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, 'core/productos.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category if category_id else None,
        'social_medias': social_medias,
    })
    
def about_us(request):
    store = Store.objects.first()  # Asegúrate de que solo haya una tienda o usa el método adecuado
    
    # Obtén los íconos de redes sociales asociados a la tienda
    social_medias = SocialMedia.objects.filter(store=store)
    
    # Obtén todas las categorías
    categories = Category.objects.all()

    return render(request, 'core/about_us.html', {
        'social_medias': social_medias,
        'categories': categories,  # Añade las categorías al contexto
    })
    
def contact_view(request):
    store = Store.objects.first()  # Asegúrate de que solo haya una tienda o usa el método adecuado
    
    # Obtén los íconos de redes sociales asociados a la tienda
    social_medias = SocialMedia.objects.filter(store=store)
    
    # Obtén todas las categorías
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            send_mail(
                f'Nuevo mensaje de {contact_message.name}',
                f'Nombre: {contact_message.name}\n'
                f'Email: {contact_message.email}\n'
                f'Mensaje:\n{contact_message.message}\n'
                f'Fecha y hora: {contact_message.timestamp}',
                'no-reply@example.com',  # Cambia esto por tu dirección de correo
                ['josematamoros917@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'social_medias': social_medias,
        'categories': categories,  # Añade las categorías al contexto
    })

def contact_success(request):
    store = Store.objects.first()  # Asegúrate de que solo haya una tienda o usa el método adecuado
    
    # Obtén los íconos de redes sociales asociados a la tienda
    social_medias = SocialMedia.objects.filter(store=store)
    
    # Obtén todas las categorías
    categories = Category.objects.all()

    return render(request, 'core/contact_success.html', {
        'social_medias': social_medias,
        'categories': categories,  # Añade las categorías al contexto
    })