
const STORAGE_KEY = 'todo';
let tasks = [];
const save = () => localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
const load = () => {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        const parsed = raw ? JSON.parse(raw) : [];
        if (Array.isArray(parsed)) return parsed;
    } catch (e) {}
    return [];
};

const uid = () => Math.random().toString(36);

const byOrder = (a, b) => a.order - b.order;

const normalize = (s) => (s || '').toLowerCase().trim()

const formatDate = (iso) => {
    if (!iso) return 'Без срока';
    const d = new Date(iso + 'T00:00:00');
    if (Number.isNaN(d.getTime())) return 'Дата не указана';
    return d.toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' });
};


function createEl(tag, { className, attrs, text } = {}, children = []) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    if (attrs) {
      for (const [k, v] of Object.entries(attrs)) {
        node.setAttribute(k, v);
      }
    }
    for (const child of children) node.appendChild(child);
    return node;
}

function removeChildren(node) {
    while (node.firstChild) node.removeChild(node.firstChild);
}

// header
const header = createEl('header');
document.body.prepend(header);

const container = createEl('div', { className: 'container'});
header.appendChild(container);

const h1 = createEl('h1', { text: 'To-Do List'});
container.appendChild(h1);

// main
const main = createEl('main');
const headerQ = document.querySelector('header');

headerQ.insertAdjacentElement('afterend', main);

const sectionControls = createEl('section', { className: 'controls'});
main.appendChild(sectionControls);

const containerControls = createEl('div', { className: 'container'});
sectionControls.appendChild(containerControls);

// form
const form = createEl('form', { className: 'controls__form'});
containerControls.appendChild(form);

const label = createEl('label', {className: "controls__formLabel", attrs: {for: "formInput"}});
form.appendChild(label);

const formDiv = createEl('div', { className: 'controls__formDiv'});
form.appendChild(formDiv);

const formInput = createEl('input', {className: "controls__formInput", attrs: {id: "formInput", type: "text", placeholder: "Введите задачу"}});
const formButton = createEl('button', {className: "controls__formButton", attrs: {type: "submit"}, text: "Добавить"});

form.appendChild(formInput);
form.appendChild(formButton);

const formDivData = createEl('div', { className: 'controls__formDivData'});
form.appendChild(formDivData);

const labelData = createEl('label', {className: "controls__formLabel", attrs: {for: "formInputData"}});
form.appendChild(label);

const formInputData = createEl('input', {className: "controls__formInput", attrs: {id: "formInputData", type: "date", placeholder: "Введите задачу"}});
form.appendChild(formInputData);

// filters
const filters = createEl('div', { className: "controls__filters"});
containerControls.appendChild(filters);

const filterDiv1 = createEl('div',  { className: "controls__filter"});
const filterDiv1Label = createEl('label', { className: "controls_filterLabel", attrs: {for: "filterDiv1"}, text: "Поиск по названию"});
const filterInput1 = createEl('input', { className: "controls__filterInput", attrs: {id: "filterDiv1", type: "search", placeholder: "Введите название"}} );
filterDiv1.appendChild(filterDiv1Label);
filterDiv1.appendChild(filterInput1);

const filterDiv2 = createEl('div',  { className: "controls__filter"});
const filterDiv2Label = createEl('label', { className: "controls_filterLabel", attrs: {for: "filterDiv2"}, text: "Фильтр по статусу"});
const filterSelect2 = createEl('select', { className: "controls__filterSelect", attrs: {id: "filterDiv2"}});
const optionAll = createEl('option', {attrs: {value: "all"}, text: "Все"});
const optionActive = createEl('option', {attrs: {value: "active"}, text: "Невыполненные"});
const optionCompleted = createEl('option', {attrs: {value: "completed"}, text: "Выполненные"});
filterSelect2.appendChild(optionAll);
filterSelect2.appendChild(optionActive);
filterSelect2.appendChild(optionCompleted);
filterDiv2.appendChild(filterDiv2Label);
filterDiv2.appendChild(filterSelect2);

const filterDiv3 = createEl('div',  { className: "controls__filter"});
const filterDiv3Label = createEl('label', { className: "controls_filterLabel", attrs: {for: "filterDiv3"}, text: "Сортировка"});
const filterSelect3 = createEl('select', { className: "controls__filterSelect", attrs: {id: "filterDiv3"}});
const optionOrderAsc = createEl('option', {attrs: {value: "order-asc"}, text: "По порядку"});
const optionDateAsc = createEl('option', {attrs: {value: "date-asc"}, text: "По дате ↑"});
const optionDateDesc = createEl('option', {attrs: {value: "date-desc"}, text: "По дате ↓"});
const optionTitleAsc = createEl('option', {attrs: {value: "title-asc"}, text: "По названию A→Z"});
const optionTitleDesc = createEl('option', {attrs: {value: "title-desc"}, text: "По названию Z→A"});
filterSelect3.appendChild(optionOrderAsc);
filterSelect3.appendChild(optionDateAsc);
filterSelect3.appendChild(optionDateDesc);
filterSelect3.appendChild(optionTitleAsc);
filterSelect3.appendChild(optionTitleDesc);
filterDiv3.appendChild(filterDiv3Label);
filterDiv3.appendChild(filterSelect3);

filters.appendChild(filterDiv1);
filters.appendChild(filterDiv2);
filters.appendChild(filterDiv3);

// list
const listSection = createEl('section', { className: "list"});
main.appendChild(listSection);

const containerList = createEl('div', { className: 'container'});
listSection.appendChild(containerList);

const list = createEl('ul', { className: "list__ul"});
containerList.appendChild(list);

function render() {
    const search = normalize(document.querySelector('#filterDiv1').value);
    const status = document.querySelector('#filterDiv2').value;
    const sort = document.querySelector('#filterDiv3').value;

    const filtered = tasks.filter(t => {
        const matchesSearch = !search || normalize(t.title).includes(search);
        const matchesStatus =
            status === 'all' ||
            (status === 'active' && !t.completed) ||
            (status === 'completed' && t.completed);
        return matchesSearch && matchesStatus;
    });

    const sorted = [...filtered].sort((a, b) => {
      switch (sort) {
        case 'date-asc': {
          const ad = a.due || '';
          const bd = b.due || '';
          if (ad === bd) return a.order - b.order;
          return ad.localeCompare(bd);
        }
        case 'date-desc': {
          const ad = a.due || '';
          const bd = b.due || '';
          if (ad === bd) return a.order - b.order;
          return bd.localeCompare(ad);
        }
        case 'title-asc': return normalize(a.title).localeCompare(normalize(b.title));
        case 'title-desc': return normalize(b.title).localeCompare(normalize(a.title));
        case 'order-asc':
        default: return a.order - b.order;
      }
    });

    let list = document.querySelector('.list__ul')

    removeChildren(list);
    for (const t of sorted) {
        list.appendChild(renderItem(t));
    }
  }

function renderItem(task) {
    const li = createEl('li', { className: 'card' + (task.completed ? ' card--completed' : '') }, []);
    li.draggable = true;
    li.dataset.id = task.id;

    const drag = createEl('div', { className: 'card__drag', attrs: { role: 'button' }, text: '⋮⋮' });

    const checkbox = createEl('input', { className: 'checkbox', attrs: { type: 'checkbox' } });
    checkbox.checked = task.completed;

    const main = createEl('div', { className: 'card__main' });
    const title = createEl('div', { className: 'card__title', text: task.title });
    const meta = createEl('div', { className: 'card__meta', text: formatDate(task.due) });
    main.append(title, meta);

    const actions = createEl('div', { className: 'card__actions' });
    const editBtn = createEl('button', { className: 'btn', text: 'Редакт.' });
    const delBtn = createEl('button', { className: 'btn', text: 'Удалить' });
    actions.append(editBtn, delBtn);

    const leftWrap = createEl('div');
    leftWrap.style.display = 'flex';
    leftWrap.style.alignItems = 'center';
    leftWrap.style.gap = '10px';
    leftWrap.append(drag, checkbox);

    li.append(leftWrap, main, actions);

    // Events
    checkbox.addEventListener('change', () => {
        task.completed = checkbox.checked;
        save();
        render();
    });

    delBtn.addEventListener('click', () => {
        tasks = tasks.filter(t => t.id !== task.id);
        renumberOrders();
        save();
        render();
    });

    editBtn.addEventListener('click', () => enterEditMode(li, task));

    return li;
}

function enterEditMode(li, task) {
    removeChildren(li);
    li.classList.remove('card--completed');

    const form = createEl('form');

    const titleInput = createEl('input', { className: 'input', attrs: { type: 'text', required: '' } });
    titleInput.value = task.title;

    const dateInput = createEl('input', { className: 'input', attrs: { type: 'date' } });
    dateInput.value = task.due || '';

    const saveBtn = createEl('button', { className: 'btn btn--primary', attrs: { type: 'submit' }, text: 'Сохранить' });
    const cancelBtn = createEl('button', { className: 'btn', attrs: { type: 'button' }, text: 'Отмена' });

    form.append(titleInput, dateInput, saveBtn, cancelBtn);
    li.append(form);

    cancelBtn.addEventListener('click', () => render());

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const newTitle = titleInput.value.trim();
        if (!newTitle) return;
        task.title = newTitle;
        task.due = dateInput.value ? dateInput.value : null;
        save();
        render();
    });
}

function renumberOrders() {
    tasks.forEach((t, i) => (t.order = i));
}

  
function bindTopControls() {
    const form = document.querySelector('.controls__form')
    form.addEventListener('submit', (e) => {
        const title = document.querySelector('#formInput').value.trim();
        if (!title) return;
        const due = document.querySelector('#formInputData').value ? document.querySelector('#formInputData').value : null;
        const order = tasks.length ? Math.max(...tasks.map(t => t.order)) + 1 : 0;
        const task = { id: uid(), title, due, completed: false, order };
        tasks.push(task);
        save();
        render();
    });

    ['input', 'change'].forEach(ev => {
        document.querySelector('#filterDiv1').addEventListener(ev, render);
        document.querySelector('#filterDiv2').addEventListener(ev, render);
        document.querySelector('#filterDiv3').addEventListener(ev, render);
    });
}


(function simpleDnD() {
    const listEl = document.querySelector('.list__ul');
    if (!listEl) return;

    listEl.addEventListener('dragstart', function(e) {
        var li = e.target.closest('li.card');
        if (!li) return;
        var id = li.dataset.id;
        e.dataTransfer.setData('text/plain', id);
        e.dataTransfer.effectAllowed = 'move';
        li.classList.add('dragging');
    });

    listEl.addEventListener('dragend', function(e) {
        var li = e.target.closest('li.card');
        if (li) li.classList.remove('dragging');
        var over = listEl.querySelectorAll('.card--dragover');
        for (var i = 0; i < over.length; i++) over[i].classList.remove('card--dragover');
    });

    listEl.addEventListener('dragover', function(e) {
        e.preventDefault();
        var under = document.elementFromPoint(e.clientX, e.clientY);
        var li = under && under.closest ? under.closest('li.card') : null;
        var over = listEl.querySelectorAll('.card--dragover');
        for (var i = 0; i < over.length; i++) over[i].classList.remove('card--dragover');
        if (li) li.classList.add('card--dragover');
    }, false);

    listEl.addEventListener('drop', function(e) {
        e.preventDefault();
        var over = listEl.querySelectorAll('.card--dragover');
        for (var i = 0; i < over.length; i++) over[i].classList.remove('card--dragover');

        var draggingId = e.dataTransfer.getData('text/plain') || null;
        if (!draggingId) {
            var draggingEl = listEl.querySelector('.dragging');
            if (draggingEl) draggingId = draggingEl.dataset.id;
        }
        if (!draggingId) return;

        var movingEl = listEl.querySelector('li.card[data-id="' + draggingId + '"]');
        if (!movingEl) return;

        var under = document.elementFromPoint(e.clientX, e.clientY);
        var targetEl = under && under.closest ? under.closest('li.card') : null;

        if (!targetEl || targetEl === movingEl) {
            listEl.appendChild(movingEl);
        } else {
            var rect = targetEl.getBoundingClientRect();
            var isAfter = e.clientY > rect.top + rect.height / 2;
            if (isAfter) listEl.insertBefore(movingEl, targetEl.nextElementSibling);
            else listEl.insertBefore(movingEl, targetEl);
        }

        var children = listEl.children;
        var ids = [];
        for (var j = 0; j < children.length; j++) ids.push(children[j].dataset.id);

        var idToTask = {};
        for (var k = 0; k < tasks.length; k++) idToTask[tasks[k].id] = tasks[k];

        var newTasks = [];
        for (var m = 0; m < ids.length; m++) {
            var id = ids[m];
            if (idToTask[id]) newTasks.push(idToTask[id]);
            else newTasks.push({ id: id, title: 'Без названия', due: null, completed: false, order: 0 });
        }
        tasks = newTasks;

        renumberOrders();
        save();
        render();
    });
})();



function init() {
    tasks = load()
        .map((x, i) => ({
            id: typeof x.id === 'string' ? x.id : uid(),
            title: x.title,
            due: x.due || null,
            completed: !!x.completed,
            order: Number.isFinite(x.order) ? x.order : i
        }));
    renumberOrders();
    bindTopControls();
    render();
}

document.addEventListener('DOMContentLoaded', init);
