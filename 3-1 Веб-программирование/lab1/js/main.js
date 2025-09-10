const buttons = document.querySelectorAll('.products__itemBottom');

const cart = JSON.parse(localStorage.getItem('cart')) || {};

buttons.forEach(btn => {
    const id = btn.dataset.id;
    const count = cart[id]?.count || 0;
    btn.dataset.count = String(count);

    if (count > 0) {
        btn.classList.add('is-active');
        renderCounter(btn, count);
    }

    btn.addEventListener('click', () => {
        increment(btn, cart);
    });
});

function increment(btn, cart) {
    const card = btn.closest('.products__item');
    const id = btn.dataset.id;
    const title = card.dataset.title;
    const price = card.dataset.price;
    const img = card.dataset.img;

    if (!btn.classList.contains('is-active')) {
        btn.classList.add('is-active');
    }

    let count = parseInt(btn.dataset.count || '0', 10) + 1;
    btn.dataset.count = String(count);

    cart[id] = { id, title, price, img, count };

    localStorage.setItem('cart', JSON.stringify(cart));

    renderCounter(btn, count);
    }

function renderCounter(btn, count) {
    let counter = btn.querySelector('.products__itemBottomCount');
    if (!counter) {
        counter = document.createElement('span');
        counter.className = 'products__itemBottomCount';
        const textP = btn.querySelector('p');
        btn.insertBefore(counter, textP);
    }
    counter.textContent = count;
}
