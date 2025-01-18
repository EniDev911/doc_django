---
date: 2024-05-14
categories:
  - Django
  - Formularios
---

{% raw %}

En Django, un formulario es una clase que representa un formulario HTML en una aplicación web. Los formularios se suelen utilizar para recolectar datos del usuario y validar la entrada antes de procesarla. Django proporciona un marco robusto para trabajar con formularios, simplificando la creación, validación y procesamiento de datos.

<!-- more -->


## Formas de crear formularios en Django

Django facilita la creación de formularios mediante dos métodos principales:

- formularios de Django (para propósito general)
- formularios de modelo (basados en un modelo de la aplicación)

Ambos métodos permiten definir y manejar formularios, pero tienen diferencias en su enfoque y propósito.

### Formularios de Django (`forms.Form`)

Este enfoque como se mencionaba es de propósito general y se suele utilizar cuando necesitas un formulario que no esté directamente relacionado con un modelo de la base de datos. Veamos un ejemplo de formulario de contacto.

#### Definir un formulario de contacto

En un archivo `forms.py` en la aplicación Django definimos el siguiente formulario:

```py
from django import forms

class ContactForm(forms.Form):

	name = forms.CharField(label='Nombre', max_length=100) #(1)!
	email = forms.EmailField(label='Correo electrónico') #(2)!
	message = forms.CharField(label='Mensaje', widget=forms.Textarea) #(3)!
```

1. Aquí `CharField` es un campo básico que corresponde a una entrada de texto.
2. Aquí `EmailField` es un campo básico que corresponde a una entrada de texto para emails.
3. Aquí `CharField` con el argumento `widget=forms.Textarea` hará que se renderice un área de texto en lugar de un campo de entrada de una sola línea.

#### Usar el formulario en la vista

Ahora en el archivo `views.py` de la aplicación Django, creamos la instancia del formulario y se pasa al contexto del template:


```py title="views.py"
from .forms import ContactForm

def contact_view(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			# Aquí se procesan los datos
			print(form.cleaned_data)
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form':form})
```

#### Crear la plantilla para el formulario

En un archivo `contact.html` en la subcarpeta **templates** de la aplicación Django mostramos el formulario:

```html title="templates/contact.html"
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}<!-- (1)! -->
    <button type="submit">Enviar</button>
</form>
```

1. `{{ form.as_p }}` renderiza el formulario con cada campo envuelto en un párrafo HTML

### Formularios de Modelo (`forms.ModelForm`)

Este enfoque se utiliza cuando deseas un formulario basado en un modelo de Django. Simplifica la creación de formularios para agregar o editar instancias de un modelo.

#### Definir un formulario para un modelo comentario

```py title="forms.py"
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	model = Comment
	fields = ['content']
```

{% endraw %}
