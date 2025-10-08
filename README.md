# 🍔 Bocatto – Sistema de Pedidos Online  

![Django](https://img.shields.io/badge/Django-v5.1-green) ![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Descripción  

**Bocatto** es un sistema de **pedidos online para comidas rápidas** desarrollado con **Django**.  
Permite a los clientes registrarse, navegar productos del menú, agregarlos al carrito, generar pedidos y elegir tipo de entrega (*retiro en local o delivery*) y forma de pago.  
El sistema también incluye una interfaz para empleados/administradores, quienes pueden gestionar los pedidos, actualizar estados y administrar los productos disponibles.

---

## ✨ Funcionalidades
### 🧑‍🍳 Cliente
- Registro y autenticación de usuarios (login/logout).  
- Exploración de productos del menú.  
- Gestión de carrito de compras:  
  - Agregar productos.  
  - Modificar cantidad.  
  - Eliminar productos.  
- Generación de pedidos a partir del carrito.  
- Selección de **tipo de entrega**: retiro en local o delivery.
- Selección de **tipo de entrega**: efectivo o transferencia.  
- Visualizacion del estado del pedido.
- Historial de pedidos con detalle de productos, subtotales y estado.
- Interfaz responsive con **Bootstrap 5**.    

---

### 🧾 Empleado / Administrador

El sistema cuenta con una interfaz administrativa donde los empleados pueden:

- Visualizar todos los pedidos generados por los clientes.
- Filtrar pedidos por estado.
- Actualizar el estado de cada pedido conforme avanza el proceso.
- Registrar el pago del pedido si se recibe en efectivo.
- Consultar detalles completos del pedido (cliente, productos, forma de entrega, método de pago, etc.).
- Gestionar el menú de productos:
    - Agregar nuevos productos.
    - Modificar precios, descripciones o imágenes.
    - Eliminar productos que ya no estén disponibles.

Esto permite un flujo de trabajo eficiente entre el cliente y el personal del local, garantizando una correcta gestión de pedidos y entregas.

---

## 🚀 Instalación  

1. Clonar el repositorio:  
    ```bash
    git clone https://github.com/tuusuario/Proyecto_Bocatto_django.git
    cd Proyecto_Bocatto_django
    ```

2. Crear y activar entorno virtual:  
    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```

3. Instalar dependencias:  
    ```bash
    pip install -r requirements.txt
    ```

4. Configurar variables de entorno (ej. `SECRET_KEY`, `DEBUG`, `DATABASE_URL`).  

5. Aplicar migraciones:  
    ```bash
    python manage.py migrate
    ```

6. Crear superusuario (opcional, para pruebas):  
    ```bash
    python manage.py createsuperuser
    ```

7. Ejecutar el servidor:  
    ```bash
    python manage.py runserver
    ```

8. Abrir en el navegador: [http://localhost:8000](http://localhost:8000)  

---

## 🖥️ Uso  

1. Registrarse o iniciar sesión.  
2. Explorar el menú de productos.  
3. Agregar productos al carrito.  
4. Seleccionar el tipo de entrega (*retiro en local o delivery*).  
5. Elegir medio de pago y confirmar la compra.  
6. Consultar estado del pedido. 
7. Revisar el historial de pedidos. 
8. Los empleados pueden gestionar los pedidos desde el panel administrativo. 

---

## 🛠️ Tecnologías  

- **Python 3.12**  
- **Django 5.x**  
- **Bootstrap 5**  
- **MySQL** 

---

## 👨‍💻 Autores

- **Lomello Baltasar** – [baltasarlomello@live.com](mailto:baltasarlomello@live.com)
- **Fumero Ignacio** – [fumero.ignacio@gmail.com](mailto:fumero.ignacio@gmail.com)
- **Dalmasso Elias** – [dalmassoelias.04@gmail.com](mailto:dalmassoelias.04@gmail.com)  

Sígueme en [GitHub](https://github.com/Balti2003)  

---

¡Gracias por visitar el proyecto Bocatto! 🚀🍟  
