let field = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
let score = 0;
let isGameOver = false;
let history = [];
let records = [];
let mergedCells = [];

const KEY_STATE = 'state';
const KEY_RECORDS = 'records';

function createEl(tag,{ className, attrs, text } = {}, children = []) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text != null) node.textContent = text;
  if (attrs) {
    for (const [k,v] of Object.entries(attrs)) node.setAttribute(k,v);
  }
  for (const c of children) node.appendChild(c);
  return node;
}

function removeChildren(node) {
  while (node.firstChild) node.removeChild(node.firstChild);
}

const header = createEl('header');
document.body.prepend(header);

const container = createEl('div',{ className: 'container' });
header.appendChild(container);

const h1 = createEl('h1',{ text: '2048 Game' });
container.appendChild(h1);

const main = createEl('main');
const headerQ = document.querySelector('header');
headerQ.insertAdjacentElement('afterend', main);

const mainSection = createEl('section',{ className: 'main' });
main.appendChild(mainSection);

const containerHeader = createEl('div',{ className: 'container' });
mainSection.appendChild(containerHeader);

const scoreText = createEl('h2',{ className: 'main__score', text: 'Счёт: ' });
containerHeader.appendChild(scoreText);

const resetButton = createEl('button',{ className: 'main__resetButton', text: 'Начать заново' });
containerHeader.appendChild(resetButton);

const undoButton = createEl('button',{ className: 'main__undoButton', text: 'Отмена хода' });
containerHeader.appendChild(undoButton);

const board = createEl('div',{ className: 'main__board' });
containerHeader.appendChild(board);

const controls = createEl('div',{ className: 'main__controls' });

const btnUp = createEl('button',{ className: 'main__btn main__btn--up', text: '↑' });
const btnLeft = createEl('button',{ className: 'main__btn main__btn--left', text: '←' });
const btnRight = createEl('button',{ className: 'main__btn main__btn--right', text: '→' });
const btnDown = createEl('button',{ className: 'main__btn main__btn--down', text: '↓' });

controls.appendChild(btnUp);
controls.appendChild(btnLeft);
controls.appendChild(btnRight);
controls.appendChild(btnDown);

containerHeader.appendChild(controls);

const recordsTitle = createEl('h3',{ className: 'main__recordsTitle', text: 'Топ-10 рекордов' });
containerHeader.appendChild(recordsTitle);

const recordsTable = createEl('table',{ className: 'main__recordsTable' });
const recordsThead = createEl('thead');
const recordsHeadRow = createEl('tr');
recordsHeadRow.appendChild(createEl('th',{ text: '№' }));
recordsHeadRow.appendChild(createEl('th',{ text: 'Имя' }));
recordsHeadRow.appendChild(createEl('th',{ text: 'Счёт' }));
recordsHeadRow.appendChild(createEl('th',{ text: 'Дата' }));
recordsThead.appendChild(recordsHeadRow);
recordsTable.appendChild(recordsThead);

const recordsTbody = createEl('tbody',{ className: 'records__body' });
recordsTable.appendChild(recordsTbody);
containerHeader.appendChild(recordsTable);

function loadRecords() {
  const data = localStorage.getItem(KEY_RECORDS);
  if (!data) {
    records = [];
    return;
  }
  try {
    const parsed = JSON.parse(data);
    if (!Array.isArray(parsed)) {
      records = [];
      return;
    }
    records = parsed.map(function(item){
      if (typeof item === 'number') return { name: null, score: item, date: new Date().toISOString() };
      if (item && typeof item === 'object' && typeof item.score === 'number') {
        return { name: item.name || null, score: item.score, date: item.date || new Date().toISOString() };
      }
      return null;
    }).filter(Boolean);
  } catch (e) {
    records = [];
  }
}

function saveRecords() {
  localStorage.setItem(KEY_RECORDS, JSON.stringify(records));
}

function updateRecords(entry) {
  let obj;
  if (typeof entry === 'number') obj = { name: null, score: entry, date: new Date().toISOString() };
  else obj = { name: entry.name || null, score: entry.score, date: entry.date || new Date().toISOString() };
  records.push(obj);
  records.sort(function(a,b){ return b.score - a.score; });
  if (records.length > 10) records = records.slice(0,10);
  saveRecords();
}

function renderRecords() {
  const body = document.querySelector('.records__body');
  if (!body) return;
  while (body.firstChild) body.removeChild(body.firstChild);
  for (let i=0;i<records.length;i++) {
    const e = records[i];
    const tr = createEl('tr');
    tr.appendChild(createEl('td',{ text: String(i+1) }));
    tr.appendChild(createEl('td',{ text: e.name ? e.name : '—' }));
    tr.appendChild(createEl('td',{ text: String(e.score) }));
    tr.appendChild(createEl('td',{ text: e.date ? new Date(e.date).toLocaleString() : '' }));
    body.appendChild(tr);
  }
}

function saveGameState() {
  const state = { field: field, score: score, isGameOver: isGameOver };
  localStorage.setItem(KEY_STATE, JSON.stringify(state));
}

function loadGameState() {
  const data = localStorage.getItem(KEY_STATE);
  if (!data) return false;
  try {
    const state = JSON.parse(data);
    if (!state || !Array.isArray(state.field)) return false;
    field = state.field;
    if (typeof state.score === 'number') score = state.score;
    if (typeof state.isGameOver === 'boolean') isGameOver = state.isGameOver;
    if (isGameOver) showGameOver();
    return true;
  } catch (e) {
    return false;
  }
}

function addNewTiles(fieldRef) {
  let howMany = Math.random() < 0.9 ? 1 : 2;
  let empties = [];
  for (let i=0;i<4;i++) for (let j=0;j<4;j++) if (fieldRef[i][j] === 0) empties.push({ i:i, j:j });
  if (empties.length === 0) return;
  for (let i = empties.length-1; i>0; i--) {
    const j = Math.floor(Math.random() * (i+1));
    const tmp = empties[i]; empties[i] = empties[j]; empties[j] = tmp;
  }
  for (let k=0;k<howMany && k<empties.length;k++) {
    const cell = empties[k];
    fieldRef[cell.i][cell.j] = Math.random() < 0.9 ? 2 : 4;
  }
}

function hasPossibleMoves() {
  for (let i=0;i<4;i++) for (let j=0;j<4;j++) if (field[i][j] === 0) return true;
  for (let i=0;i<4;i++) for (let j=0;j<3;j++) if (field[i][j] === field[i][j+1]) return true;
  for (let j=0;j<4;j++) for (let i=0;i<3;i++) if (field[i][j] === field[i+1][j]) return true;
  return false;
}

function showGameOver() {
  let overlay = document.querySelector('.overlay-save');
  if (!overlay) {
    overlay = createEl('div', { className: 'overlay-save' });
    const card = createEl('div', { className: 'overlay-card' });
    const title = createEl('h3', { text: 'Игра окончена' });
    const info = createEl('div', { text: 'Введите имя для сохранения результата:' });
    const input = createEl('input', { attrs: { type: 'text', placeholder: 'Ваше имя' } });
    const row = createEl('div', { className: 'row' });
    const saveBtn = createEl('button', { text: 'Сохранить результат' });
    const restartBtn = createEl('button', { text: 'Начать заново' });

    row.appendChild(saveBtn);
    row.appendChild(restartBtn);

    card.appendChild(title);
    card.appendChild(info);
    card.appendChild(input);
    card.appendChild(row);
    overlay.appendChild(card);
    document.body.appendChild(overlay);

    input.focus();

    saveBtn.addEventListener('click', function () {
      const name = input.value.trim();
      if (name.length === 0) return;
      updateRecords({ name: name, score: score });
      renderRecords();
      input.style.display = 'none';
      saveBtn.style.display = 'none';
      info.textContent = 'Ваш рекорд сохранен.';
    });

    restartBtn.addEventListener('click', function () {
      closeOverlay();
      reset();
    });

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeOverlay();
    });
  }
}


function closeOverlay() {
  const overlay = document.querySelector('.overlay-save');
  if (overlay) overlay.remove();
}

function removeGameOver() {
  closeOverlay();
}

function reset() {
  score = 0;
  isGameOver = false;
  history = [];
  mergedCells = [];
  field = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
  removeGameOver();
  addNewTiles(field);
  render();
  summAll();
  saveGameState();
}

function undo() {
  if (isGameOver) return;
  if (history.length === 0) return;
  const prevField = history.pop();
  field = prevField.map(function(row){ return row.slice(); });
  isGameOver = false;
  mergedCells = [];
  removeGameOver();
  render();
  summAll();
  saveGameState();
}

function isMergedCell(i,j) {
  return mergedCells.some(function(cell){ return cell.i === i && cell.j === j; });
}

function render() {
  const b = document.querySelector('.main__board');
  removeChildren(b);
  for (let i=0;i<4;i++) {
    for (let j=0;j<4;j++) {
      const value = field[i][j];
      let className = 'tile tile-' + value;
      if (value !== 0 && isMergedCell(i,j)) className += ' tile-merged';
      const tile = createEl('div',{ className: className, text: value === 0 ? '' : value });
      tile.style.gridRowStart = i+1;
      tile.style.gridColumnStart = j+1;
      b.appendChild(tile);
    }
  }
}

function summAll() {
  let summ = 0;
  for (let i=0;i<4;i++) for (let j=0;j<4;j++) summ += field[i][j];
  score = summ;
  scoreText.textContent = 'Счёт: ' + summ;
}

function right() {
  let moved = false;
  for (let i=0;i<4;i++) {
    let row = field[i].filter(function(x){ return x !== 0; });
    for (let j=row.length-1;j>0;j--) {
      if (row[j] === row[j-1]) { row[j] *= 2; row[j-1] = 0; }
    }
    row = row.filter(function(x){ return x !== 0; });
    while (row.length < 4) row.unshift(0);
    for (let j=0;j<4;j++) {
      if (field[i][j] !== row[j]) { field[i][j] = row[j]; moved = true; }
    }
  }
  return moved;
}

function left() {
  let moved = false;
  for (let i=0;i<4;i++) {
    let row = field[i].filter(function(x){ return x !== 0; });
    for (let j=0;j<row.length-1;j++) {
      if (row[j] === row[j+1]) { row[j] *= 2; row[j+1] = 0; }
    }
    row = row.filter(function(x){ return x !== 0; });
    while (row.length < 4) row.push(0);
    for (let j=0;j<4;j++) {
      if (field[i][j] !== row[j]) { field[i][j] = row[j]; moved = true; }
    }
  }
  return moved;
}

function down() {
  let moved = false;
  for (let col=0; col<4; col++) {
    let column = [];
    for (let row=3; row>=0; row--) if (field[row][col] !== 0) column.push(field[row][col]);
    for (let i=column.length-1;i>0;i--) {
      if (column[i] === column[i-1]) { column[i] *= 2; column[i-1] = 0; }
    }
    column = column.filter(function(x){ return x !== 0; });
    while (column.length < 4) column.push(0);
    for (let row=3, i=0; row>=0; row--, i++) {
      if (field[row][col] !== column[i]) { field[row][col] = column[i]; moved = true; }
    }
  }
  return moved;
}

function up() {
  let moved = false;
  for (let col=0; col<4; col++) {
    let column = [];
    for (let row=0; row<4; row++) if (field[row][col] !== 0) column.push(field[row][col]);
    for (let i=0;i<column.length-1;i++) {
      if (column[i] === column[i+1]) { column[i] *= 2; column[i+1] = 0; }
    }
    column = column.filter(function(x){ return x !== 0; });
    while (column.length < 4) column.push(0);
    for (let row=0; row<4; row++) {
      if (field[row][col] !== column[row]) { field[row][col] = column[row]; moved = true; }
    }
  }
  return moved;
}

function handleMove(direction) {
  if (isGameOver) return;
  mergedCells = [];
  let moved = false;
  const beforeMove = field.map(function(row){ return row.slice(); });
  switch (direction) {
    case 'up': moved = up(); break;
    case 'down': moved = down(); break;
    case 'left': moved = left(); break;
    case 'right': moved = right(); break;
  }
  if (moved) {
    history.push(beforeMove);
    for (let i=0;i<4;i++) for (let j=0;j<4;j++) {
      const prev = beforeMove[i][j];
      const curr = field[i][j];
      if (prev !== 0 && curr > prev) mergedCells.push({ i:i, j:j });
    }
    addNewTiles(field);
    render();
    summAll();
    if (!hasPossibleMoves()) {
      isGameOver = true;
      showGameOver();
    }
    saveGameState();
  }
}

function init() {
  loadRecords();
  renderRecords();
  const hasState = loadGameState();
  if (!hasState) addNewTiles(field);
  render();
  summAll();
  saveGameState();
}

document.addEventListener('keydown',function(e){
  switch (e.key) {
    case 'ArrowUp': handleMove('up'); break;
    case 'ArrowDown': handleMove('down'); break;
    case 'ArrowLeft': handleMove('left'); break;
    case 'ArrowRight': handleMove('right'); break;
  }
});

resetButton.addEventListener('click', reset);
undoButton.addEventListener('click', undo);

btnUp.addEventListener('click', function(){ handleMove('up'); });
btnDown.addEventListener('click', function(){ handleMove('down'); });
btnLeft.addEventListener('click', function(){ handleMove('left'); });
btnRight.addEventListener('click', function(){ handleMove('right'); });

document.addEventListener('DOMContentLoaded', init);
