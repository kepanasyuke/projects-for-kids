// МОДУЛЬ 1: базовые структуры. В каждом задании замени заглушки в блоке данных.
const blocked = value => [...value].some(item => String(item).startsWith('ВПИШИ_'));
const task = (title, data, hint, example, draw) => ({ title, hint, example, valid: () => data.length > 0 && !blocked(data), draw });
const orbit = (color, count, frame, width, height) => { const x = width / 2, y = height / 2; for (let i = 0; i < count; i++) { const angle = frame * .015 + i * Math.PI * 2 / count; const radius = 70 + i * 35; ctx.fillStyle = color; ctx.beginPath(); ctx.arc(x + Math.cos(angle) * radius, y + Math.sin(angle) * radius * .5, 12, 0, Math.PI * 2); ctx.fill(); } };
const ctx = document.querySelector('#canvas').getContext('2d');
export const module1 = [
 task('01 · Массив ракет', ['ВПИШИ_РАКЕТУ_1','ВПИШИ_РАКЕТУ_2','ВПИШИ_РАКЕТУ_3'], 'Впиши 3 названия в квадратных скобках.', "['Молния', 'Комета', 'Феникс']", (c,f,w,h) => { c.fillStyle='#ff6574'; for(let i=0;i<3;i++){const x=(f*2+i*180)% (w+100)-50;c.fillRect(x,h/2-30,45,60);c.fillStyle='#ffd166';c.fillRect(x-15,h/2-10,15,20);c.fillStyle='#ff6574';} }),
 task('02 · Список планет', ['ВПИШИ_ПЛАНЕТУ_1','ВПИШИ_ПЛАНЕТУ_2','ВПИШИ_ПЛАНЕТУ_3'], 'Впиши 3 названия планет. Порядок сохраняется.', "['Марс', 'Земля', 'Нептун']", (c,f,w,h) => { orbit('#65e6bd',3,f,w,h); }),
 task('03 · Очередь роботов', ['ВПИШИ_РОБОТА_1','ВПИШИ_РОБОТА_2','ВПИШИ_РОБОТА_3'], 'Впиши 3 имени роботов в очередь.', "['Бип', 'Боп', 'Бум']", (c,f,w,h) => { for(let i=0;i<3;i++){c.fillStyle=['#65e6bd','#ffd166','#ff6574'][i];c.fillRect(100+i*150,(h/2)+Math.sin(f*.04+i)*35,70,70);c.fillStyle='#11151c';c.fillRect(118+i*150,(h/2)+20+Math.sin(f*.04+i)*35,10,10);c.fillRect(142+i*150,(h/2)+20+Math.sin(f*.04+i)*35,10,10);} }),
 task('04 · Башня кубиков', ['ВПИШИ_КУБИК_1','ВПИШИ_КУБИК_2','ВПИШИ_КУБИК_3'], 'Впиши 3 цвета или названия кубиков.', "['Красный', 'Зелёный', 'Синий']", (c,f,w,h) => { for(let i=0;i<3;i++){c.save();c.translate(w/2+(i-1)*70,h/2-(i*55));c.rotate(f*.01+i);c.fillStyle=['#ff6574','#65e6bd','#ffd166'][i];c.fillRect(-25,-25,50,50);c.restore();} })
];
