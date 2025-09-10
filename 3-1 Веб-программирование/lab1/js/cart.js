const tpl = document.getElementById('cart__itemTmpl');
const container = document.querySelector('section.products .container');

let list = container.querySelector('.cart__list');
list = document.createElement('div');
list.className = "cart__list";
tpl.after(list);
renderCart();

list.addEventListener('click', (e) => {
    const row = e.target.closest('.cart__item');
    const id = row.dataset.id;

    if (e.target.classList.contains('cart__inc')) {
        changeCount(id, +1);
    } else if (e.target.classList.contains('cart__dec')) {
        changeCount(id, -1);
    } else if (e.target.classList.contains('cart__remove')) {
        removeItem(id);
    }
});

function renderCart() {
    const cart = getCart();
    const items = Object.values(cart);

    list.innerHTML = '';

    if (!items.length) {
        list.innerHTML = '<p class="cart__empty">Корзина пуста</p>';
        return;
    }

    const frag = document.createDocumentFragment();

    items.forEach(item => {
        const node = tpl.content.cloneNode(true);

        node.querySelector('.cart__item').dataset.id = item.id;
        node.querySelector('.cart__img').src = item.img;
        node.querySelector('.cart__img').alt = item.title;
        node.querySelector('.cart__title').textContent = item.title;
        node.querySelector('.cart__price').textContent = item.price + "₽" + " / шт.";
        node.querySelector('.cart__count').textContent = item.count;
        node.querySelector('.cart__itemSum').textContent = (item.price * item.count) + "₽";

        frag.appendChild(node);
    });

    list.appendChild(frag);
    updateTotal();
}

function changeCount(id, delta) {
    const cart = getCart();
    const next = Math.max(0, (cart[id].count || 0) + delta);
    if (next === 0) {
        delete cart[id];
    } else {
        cart[id].count = next;
    }
    setCart(cart);
    renderCart();
    updateTotal();
}

function removeItem(id) {
    const cart = getCart();
    if (cart[id]) {
        delete cart[id];
        setCart(cart);
        renderCart();
    }
    updateTotal();
}

function getCart() {
    console.log(localStorage.getItem("cart"));
    return JSON.parse(localStorage.getItem("cart")) || {};
}

function setCart(cart) {
    localStorage.setItem("cart", JSON.stringify(cart));
}

function updateTotal() {
    const cart = getCart();
    const total = Object.values(cart).reduce((sum, item) => {
        const price = Number(item.price) || 0;
        const count = Number(item.count) || 0;
        return sum + price * count;
    }, 0);
    localStorage.setItem("total", String(total));
    const htmlTotal = document.querySelector(".cart__total");
    htmlTotal.textContent = "Итоговая стоимость: " + total;
    return total;
}


const form = document.querySelector(".order__form");
form.addEventListener("submit", () => {
    setCart({});                      
    renderCart();                     
    updateTotal();                    
    alert("Заказ успешно создан.");

})


const toggleBtn = document.querySelector('.cart__toggleOrder');
const accordion = document.querySelector('.order__accordion');

if (toggleBtn && accordion) {
  toggleBtn.addEventListener('click', () => {
    accordion.classList.toggle('is-open');
    if (accordion.classList.contains('is-open')) {
      accordion.hidden = false;
    } else {
      setTimeout(() => { accordion.hidden = true; }, 300);
    }
  });
}