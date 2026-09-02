// МОДУЛЬ 4: словари и персонажи. Измени значения в объектах.
const blocked = object => Object.values(object).some(value => String(value).startsWith('ВПИШИ_'));
const task = (title, data, hint, example, draw) => ({ title, hint, example, valid: () => !blocked(data), draw });
export const module4 = [
 task('13 · Герой', {name:'ВПИШИ_ИМЯ', power:'ВПИШИ_СИЛУ', weapon:'ВПИШИ_ОРУЖИЕ'}, 'Заполни имя, силу и оружие героя.', "{name: 'Лира', power: 'Полёт', weapon: 'Меч'}", (c,f,w,h)=>{c.fillStyle='#65e6bd';c.beginPath();c.moveTo(w/2,h/2-110);c.lineTo(w/2+65,h/2+90);c.lineTo(w/2-65,h/2+90);c.fill();c.fillStyle='#f6c6a8';c.beginPath();c.arc(w/2,h/2-120,34,0,7);c.fill();}),
 task('14 · Питомец', {name:'ВПИШИ_ИМЯ', color:'ВПИШИ_ЦВЕТ', talent:'ВПИШИ_ТАЛАНТ'}, 'Придумай имя, цвет и талант питомца.', "{name: 'Искра', color: 'Золотой', talent: 'Прыжки'}", (c,f,w,h)=>{c.fillStyle='#ffd166';c.beginPath();c.arc(w/2,h/2,70+Math.sin(f*.04)*8,0,7);c.fill();c.fillStyle='#11151c';c.arc(w/2-25,h/2-12,8,0,7);c.arc(w/2+25,h/2-12,8,0,7);c.fill();}),
 task('15 · Волшебник', {name:'ВПИШИ_ИМЯ', spell:'ВПИШИ_ЗАКЛИНАНИЕ', level:'ВПИШИ_УРОВЕНЬ'}, 'Заполни имя, заклинание и уровень.', "{name: 'Орион', spell: 'Свет', level: '7'}", (c,f,w,h)=>{for(let i=0;i<10;i++){const a=f*.03+i*.62;c.fillStyle='#9b8cff';c.fillRect(w/2+Math.cos(a)*120,h/2+Math.sin(a)*90,12,12);}}),
 task('16 · Космонавт', {name:'ВПИШИ_ИМЯ', planet:'ВПИШИ_ПЛАНЕТУ', mission:'ВПИШИ_МИССИЮ'}, 'Придумай имя, планету и миссию.', "{name: 'Нова', planet: 'Марс', mission: 'Поиск воды'}", (c,f,w,h)=>{c.strokeStyle='#ff6574';c.lineWidth=5;c.beginPath();c.arc(w/2,h/2,100+Math.sin(f*.03)*15,0,7);c.stroke();c.fillStyle='#f4f1e8';c.beginPath();c.arc(w/2,h/2,35,0,7);c.fill();})
];
