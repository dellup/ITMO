let locations = [];
let activeId = null;
let lastSuggest = [];
let geoDeniedShown = false;

const KEY_LOCATIONS = 'locations';
const KEY_ACTIVE = 'active';
const KEY_GEO_INIT = 'geo_init';

function createEl(tag, { className, text, attrs } = {}, children = []) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text != null) node.textContent = text;
  if (attrs) {
    for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, v);
  }
  for (const c of children) node.appendChild(c);
  return node;
}

function removeChildren(node) {
  while (node.firstChild) node.removeChild(node.firstChild);
}

function saveState() {
  localStorage.setItem(KEY_LOCATIONS, JSON.stringify(locations));
  localStorage.setItem(KEY_ACTIVE, activeId ? String(activeId) : '');
}

function loadState() {
  const a = localStorage.getItem(KEY_ACTIVE);
  const data = localStorage.getItem(KEY_LOCATIONS);
  if (data) {
    try {
      const parsed = JSON.parse(data);
      if (Array.isArray(parsed)) locations = parsed;
    } catch (e) {}
  }
  if (a) activeId = a;
  if (locations.length > 0 && !activeId) activeId = locations[0].id;
}

function uid() {
  return String(Date.now()) + '_' + String(Math.floor(Math.random() * 100000));
}

function showOverlayDenied() {
  const overlay = document.querySelector('.overlay');
  overlay.classList.remove('overlay-hidden');
}

function hideOverlayDenied() {
  const overlay = document.querySelector('.overlay');
  overlay.classList.add('overlay-hidden');
}

function normalizeName(item) {
  let s = item.name || '';
  if (item.admin1) s += ', ' + item.admin1;
  if (item.country) s += ', ' + item.country;
  return s;
}

function fetchSuggest(q) {
  return fetch('https://geocoding-api.open-meteo.com/v1/search?name=' + encodeURIComponent(q) + '&count=7&language=ru&format=json')
    .then(function (r) { return r.json(); });
}

function fetchForecast(lat, lon) {
  const url =
    'https://api.open-meteo.com/v1/forecast?latitude=' + encodeURIComponent(lat) +
    '&longitude=' + encodeURIComponent(lon) +
    '&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode' +
    '&forecast_days=3&timezone=auto';
  return fetch(url).then(function (r) { return r.json(); });
}

function weatherText(code) {
  const c = Number(code);
  if (c === 0) return 'Ясно';
  if (c === 1 || c === 2) return 'Облачно';
  if (c === 3) return 'Пасмурно';
  if (c === 45 || c === 48) return 'Туман';
  if (c === 51 || c === 53 || c === 55) return 'Морось';
  if (c === 61 || c === 63 || c === 65) return 'Дождь';
  if (c === 71 || c === 73 || c === 75) return 'Снег';
  if (c === 80 || c === 81 || c === 82) return 'Ливни';
  if (c === 95) return 'Гроза';
  return 'Погода';
}

function renderTabs() {
  const row = document.querySelector('.locations-row');
  removeChildren(row);

  for (let i = 0; i < locations.length; i++) {
    const loc = locations[i];
    const btn = createEl('button', {
      className: 'tab' + (String(loc.id) === String(activeId) ? ' tab-active' : ''),
      text: loc.title
    });
    btn.addEventListener('click', function () {
      activeId = loc.id;
      saveState();
      renderTabs();
      renderCards();
      loadWeatherForActive();
    });
    row.appendChild(btn);
  }
}

function renderCardsLoading(title) {
  const wrap = document.querySelector('.cards-wrap');
  removeChildren(wrap);
  for (let i = 0; i < 3; i++) {
    const card = createEl('div', { className: 'card' });
    card.appendChild(createEl('div', { className: 'card__title', text: title + ' • день ' + String(i + 1) }));
    card.appendChild(createEl('div', { className: 'loading', text: 'Загрузка...' }));
    wrap.appendChild(card);
  }
}

function renderCardsError(title, msg) {
  const wrap = document.querySelector('.cards-wrap');
  removeChildren(wrap);
  const card = createEl('div', { className: 'card' });
  card.appendChild(createEl('div', { className: 'card__title', text: title }));
  card.appendChild(createEl('div', { className: 'bad', text: msg || 'Ошибка запроса' }));
  wrap.appendChild(card);
}

function renderCardsFromData(title, data) {
  const wrap = document.querySelector('.cards-wrap');
  removeChildren(wrap);

  const daily = data && data.daily ? data.daily : null;
  if (!daily || !daily.time || daily.time.length < 3) {
    renderCardsError(title, 'Нет данных прогноза');
    return;
  }

  for (let i = 0; i < 3; i++) {
    const date = daily.time[i];
    const tmax = daily.temperature_2m_max ? daily.temperature_2m_max[i] : '';
    const tmin = daily.temperature_2m_min ? daily.temperature_2m_min[i] : '';
    const pr = daily.precipitation_sum ? daily.precipitation_sum[i] : '';
    const wc = daily.weathercode ? daily.weathercode[i] : '';

    const card = createEl('div', { className: 'card' });
    card.appendChild(createEl('div', { className: 'card__title', text: title + ' • ' + String(date) }));

    card.appendChild(createEl('div', { className: 'card__row' }, [
      createEl('div', { text: 'Состояние' }),
      createEl('div', { text: weatherText(wc) })
    ]));

    card.appendChild(createEl('div', { className: 'card__row' }, [
      createEl('div', { text: 'Макс' }),
      createEl('div', { text: String(tmax) + '°' })
    ]));

    card.appendChild(createEl('div', { className: 'card__row' }, [
      createEl('div', { text: 'Мин' }),
      createEl('div', { text: String(tmin) + '°' })
    ]));

    card.appendChild(createEl('div', { className: 'card__row' }, [
      createEl('div', { text: 'Осадки' }),
      createEl('div', { text: String(pr) + ' мм' })
    ]));

    wrap.appendChild(card);
  }
}

function getActive() {
  for (let i = 0; i < locations.length; i++) {
    if (String(locations[i].id) === String(activeId)) return locations[i];
  }
  return null;
}

function renderCards() {
  const loc = getActive();
  if (!loc) {
    const wrap = document.querySelector('.cards-wrap');
    removeChildren(wrap);
    wrap.appendChild(createEl('div', { className: 'card' }, [
      createEl('div', { className: 'card__title', text: 'Нет выбранной локации' })
    ]));
    return;
  }
  renderCardsLoading(loc.title);
}

function loadWeatherForActive() {
  const loc = getActive();
  if (!loc) return;

  renderCardsLoading(loc.title);

  fetchForecast(loc.lat, loc.lon)
    .then(function (data) {
      renderCardsFromData(loc.title, data);
    })
    .catch(function () {
      renderCardsError(loc.title, 'Ошибка получения прогноза');
    });
}

function refreshAll() {
  loadWeatherForActive();
}

function addLocation(obj) {
  if (!obj || typeof obj.lat !== 'number' || typeof obj.lon !== 'number') return;

  for (let i = 0; i < locations.length; i++) {
    const a = locations[i];
    if (Math.abs(a.lat - obj.lat) < 0.0001 && Math.abs(a.lon - obj.lon) < 0.0001) return;
  }

  locations.push({
    id: uid(),
    title: obj.title,
    lat: obj.lat,
    lon: obj.lon
  });

  if (!activeId) activeId = locations[0].id;

  saveState();
  renderTabs();
}

function requestGeoIfNeeded() {
  const wasInit = localStorage.getItem(KEY_GEO_INIT);
  if (wasInit) return;

  localStorage.setItem(KEY_GEO_INIT, '1');

  if (!navigator.geolocation) {
    showOverlayDenied();
    return;
  }

  navigator.geolocation.getCurrentPosition(
    function (pos) {
      const lat = pos.coords.latitude;
      const lon = pos.coords.longitude;

      locations = [];
      addLocation({
        title: 'Текущее местоположение',
        lat: lat,
        lon: lon
      });

      activeId = locations[0].id;
      saveState();
      renderTabs();
      renderCards();
      loadWeatherForActive();
    },
    function () {
      showOverlayDenied();
    },
    { enableHighAccuracy: true, timeout: 8000 }
  );
}


function showDropdown(items) {
  const dd = document.querySelector('.city-dropdown');
  removeChildren(dd);

  if (!items || items.length === 0) {
    dd.style.display = 'none';
    return;
  }

  for (let i = 0; i < items.length; i++) {
    const it = items[i];
    const name = normalizeName(it);
    const row = createEl('div', { className: 'dropdown__item', text: name });
    row.addEventListener('click', function () {
      const inp = document.querySelector('.city-input');
      inp.value = name;
      lastSuggest = items;
      dd.style.display = 'none';
      document.querySelector('.city-error').textContent = '';
    });
    dd.appendChild(row);
  }

  dd.style.display = 'block';
}

function findSelectedCityByInput() {
  const inp = document.querySelector('.city-input');
  const v = inp.value.trim().toLowerCase();
  if (!v) return null;

  for (let i = 0; i < lastSuggest.length; i++) {
    const it = lastSuggest[i];
    const name = normalizeName(it).trim().toLowerCase();
    if (name === v) return it;
  }
  return null;
}

function initUI() {
  const input = document.querySelector('.city-input');
  const addBtn = document.querySelector('.btn-add');
  const refreshBtn = document.querySelector('.btn-refresh');
  const closeModalBtn = document.querySelector('.btn-close-modal');

  let t = null;

  input.addEventListener('input', function () {
    const q = input.value.trim();
    document.querySelector('.city-error').textContent = '';

    if (t) clearTimeout(t);
    t = setTimeout(function () {
      if (q.length < 2) {
        showDropdown([]);
        lastSuggest = [];
        return;
      }

      fetchSuggest(q)
        .then(function (data) {
          const res = data && data.results ? data.results : [];
          lastSuggest = res;
          showDropdown(res);
        })
        .catch(function () {
          lastSuggest = [];
          showDropdown([]);
        });
    }, 250);
  });

  document.addEventListener('click', function (e) {
    const dd = document.querySelector('.city-dropdown');
    const box = document.querySelector('.add__col');
    if (!box.contains(e.target)) dd.style.display = 'none';
  });

  addBtn.addEventListener('click', function () {
    const err = document.querySelector('.city-error');
    err.textContent = '';


    const item = findSelectedCityByInput();
    if (!item) {
      err.textContent = 'Выберите город из списка';
      return;
    }

    addLocation({
      title: normalizeName(item),
      lat: Number(item.latitude),
      lon: Number(item.longitude)
    });

    const inp = document.querySelector('.city-input');
    inp.value = '';
    lastSuggest = [];
    showDropdown([]);

    renderTabs();
    if (activeId) {
      renderCards();
      loadWeatherForActive();
    }
  });

  refreshBtn.addEventListener('click', function () {
    refreshAll();
  });

  closeModalBtn.addEventListener('click', function () {
    hideOverlayDenied();
  });
}

function init() {
  loadState();
  initUI();
  renderTabs();

  requestGeoIfNeeded();

  if (locations.length > 0) {
    renderCards();
    loadWeatherForActive();
  } else {
    renderCards();
  }
}


document.addEventListener('DOMContentLoaded', init);
