import { rockets, rocketsTask } from './1_rockets.js';
import { ingredients, pizzaTask } from './2_pizza.js';
import { trainCars, trainTask } from './3_train.js';
import { hero, heroTask } from './4_hero.js';

const tasks = [rocketsTask, pizzaTask, trainTask, heroTask];
const canvas = document.querySelector('#canvas');
const ctx = canvas.getContext('2d');
const menu = document.querySelector('#menu');
const gameOver = document.querySelector('#game-over');
const label = document.querySelector('#scene-label');
let selected = 0;
let frame = 0;

function resize() { const scale = devicePixelRatio || 1; canvas.width = canvas.clientWidth * scale; canvas.height = canvas.clientHeight * scale; ctx.setTransform(scale, 0, 0, scale, 0, 0); }
function drawBackground(width, height, warning = false) { ctx.fillStyle = warning ? '#24131a' : '#151d28'; ctx.fillRect(0, 0, width, height); ctx.strokeStyle = warning ? 'rgba(255,101,116,.12)' : 'rgba(101,230,189,.1)'; for (let x = 0; x < width; x += 46) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke(); } for (let y = 0; y < height; y += 46) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke(); } }
function showTask(index) { selected = index; const task = tasks[index]; document.querySelectorAll('button').forEach((button, i) => button.classList.toggle('active', i === index)); label.textContent = `${String(index + 1).padStart(2, '0')} / ${task.title.toUpperCase()}`; const valid = task.valid(); gameOver.hidden = valid; if (!valid) { document.querySelector('#message').textContent = 'Данные не заполнены. Основная анимация заблокирована.'; document.querySelector('#hint').textContent = task.hint; document.querySelector('#example').textContent = task.example; } }
['01 · РАКЕТЫ', '02 · ПИЦЦА', '03 · ПОЕЗД', '04 · ГЕРОЙ'].forEach((name, index) => { const button = document.createElement('button'); button.textContent = name; button.addEventListener('click', () => showTask(index)); menu.appendChild(button); });
function animate() { requestAnimationFrame(animate); frame += 1; const width = canvas.clientWidth, height = canvas.clientHeight; const valid = tasks[selected].valid(); drawBackground(width, height, !valid); if (valid) tasks[selected].draw(ctx, frame, width, height); else { ctx.save(); ctx.translate(width / 2, height / 2); ctx.rotate(frame * .01); ctx.strokeStyle = 'rgba(255,101,116,.6)'; ctx.lineWidth = 3; ctx.strokeRect(-80, -80, 160, 160); ctx.restore(); } }
addEventListener('resize', resize); resize(); showTask(0); animate();
