import { module1 } from './module_1.js';
import { module2 } from './module_2.js';
import { module3 } from './module_3.js';
import { module4 } from './module_4.js';
import { module5 } from './module_5.js';
import { module6 } from './module_6.js';
import { module7 } from './module_7.js';
import { module8 } from './module_8.js';
import { module9 } from './module_9.js';
import { module10 } from './module_10.js';
import { module11 } from './module_11.js';
import { module12 } from './module_12.js';
import { module13 } from './module_13.js';
import { module14 } from './module_14.js';
import { module15 } from './module_15.js';
import { module16 } from './module_16.js';

const tasks = [...module1, ...module2, ...module3, ...module4, ...module5, ...module6, ...module7, ...module8, ...module9, ...module10, ...module11, ...module12, ...module13, ...module14, ...module15, ...module16];
const canvas = document.querySelector('#canvas');
const context = canvas.getContext('2d');
const menu = document.querySelector('#menu');
const gameOver = document.querySelector('#game-over');
const label = document.querySelector('#scene-label');
let selected = 0;
let frame = 0;

function resize() { const scale = devicePixelRatio || 1; canvas.width = canvas.clientWidth * scale; canvas.height = canvas.clientHeight * scale; context.setTransform(scale, 0, 0, scale, 0, 0); }
function background(width, height, locked) { context.fillStyle = locked ? '#29151c' : '#151d28'; context.fillRect(0, 0, width, height); context.strokeStyle = locked ? 'rgba(255,101,116,.12)' : 'rgba(101,230,189,.1)'; for (let x = 0; x < width; x += 46) { context.beginPath(); context.moveTo(x, 0); context.lineTo(x, height); context.stroke(); } for (let y = 0; y < height; y += 46) { context.beginPath(); context.moveTo(0, y); context.lineTo(width, y); context.stroke(); } }
function showTask(index) { selected = index; const task = tasks[index]; document.querySelectorAll('button').forEach((button, i) => button.classList.toggle('active', i === index)); label.textContent = `${String(index + 1).padStart(2, '0')} / ${task.title.toUpperCase()}`; const valid = task.valid(); gameOver.hidden = valid; if (!valid) { document.querySelector('#message').textContent = 'Задание пока не выполнено. Основная анимация заблокирована.'; document.querySelector('#hint').textContent = task.hint; document.querySelector('#example').textContent = task.example; } }
tasks.forEach((task, index) => { const button = document.createElement('button'); button.textContent = task.title; button.addEventListener('click', () => showTask(index)); menu.appendChild(button); });
function animate() { requestAnimationFrame(animate); frame += 1; const width = canvas.clientWidth, height = canvas.clientHeight; const valid = tasks[selected].valid(); background(width, height, !valid); if (valid) tasks[selected].draw(context, frame, width, height); else { context.save(); context.translate(width / 2, height / 2); context.rotate(frame * .01); context.strokeStyle = 'rgba(255,101,116,.7)'; context.lineWidth = 4; context.strokeRect(-80, -80, 160, 160); context.restore(); } }
addEventListener('resize', resize); resize(); showTask(0); animate();
