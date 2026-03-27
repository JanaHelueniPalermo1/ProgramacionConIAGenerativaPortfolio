const menuButtons = document.querySelectorAll('.menu-btn');
const panels = document.querySelectorAll('.panel');
const form = document.getElementById('product-form');
const message = document.getElementById('form-message');
const tableBody = document.getElementById('products-body');
const refreshButton = document.getElementById('refresh-btn');

const API_BASE = '/api/productos';

menuButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const target = button.dataset.target;

        menuButtons.forEach((btn) => btn.classList.remove('active'));
        panels.forEach((panel) => panel.classList.remove('active'));

        button.classList.add('active');
        document.getElementById(target).classList.add('active');

        if (target === 'listar') {
            loadProducts();
        }
    });
});

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    clearMessage();

    const payload = {
        nombre: form.nombre.value.trim(),
        codigo: form.codigo.value,
        precio: form.precio.value,
        stock: form.stock.value,
    };

    try {
        const response = await fetch(API_BASE, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        const data = await response.json();

        if (!response.ok) {
            showMessage(data.error || 'No se pudo guardar el producto.', true);
            return;
        }

        showMessage('Producto guardado correctamente.', false);
        form.reset();
        await loadProducts();
    } catch (error) {
        showMessage('Error de conexion con la API.', true);
    }
});

refreshButton.addEventListener('click', async () => {
    await loadProducts();
});

async function loadProducts() {
    try {
        const response = await fetch(API_BASE);
        const products = await response.json();

        if (!response.ok) {
            tableBody.innerHTML = '<tr><td colspan="4" class="empty">No se pudo cargar el listado.</td></tr>';
            return;
        }

        if (!products.length) {
            tableBody.innerHTML = '<tr><td colspan="4" class="empty">Aun no hay productos cargados.</td></tr>';
            return;
        }

        tableBody.innerHTML = products
            .map(
                (item) => `
                <tr>
                    <td>${escapeHtml(item.nombre)}</td>
                    <td>${item.codigo}</td>
                    <td>${Number(item.precio).toFixed(2)}</td>
                    <td>${item.stock}</td>
                </tr>
            `
            )
            .join('');
    } catch (error) {
        tableBody.innerHTML = '<tr><td colspan="4" class="empty">Error de conexion con la API.</td></tr>';
    }
}

function showMessage(text, isError) {
    message.textContent = text;
    message.classList.remove('ok', 'error');
    message.classList.add(isError ? 'error' : 'ok');
}

function clearMessage() {
    message.textContent = '';
    message.classList.remove('ok', 'error');
}

function escapeHtml(value) {
    return String(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');
}

loadProducts();
