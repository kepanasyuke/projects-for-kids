// МОДУЛЬ 3: цепочки и маршруты. Замени заглушки в данных.
const blocked = value => [...value].some(item => String(item).startsWith('ВПИШИ_'));
const task = (title, data, hint, example, draw) => ({ title, hint, example, valid: () => data.length > 0 && !blocked(data), draw });
const train = (c,f,w,h,color='#65e6bd') => data => { data.forEach((_,i)=>{const x=w/2+(i-(data.length-1)/2)*120+(f*.7%120);c.fillStyle=i===0?'#ff6574':color;c.fillRect(x-42,h/2-28,84,56);c.fillStyle='#11151c';c.fillRect(x-25,h/2-12,18,15);c.fillRect(x+8,h/2-12,18,15);c.beginPath();c.arc(x-24,h/2+34,10,0,7);c.arc(x+24,h/2+34,10,0,7);c.fill();});};
export const module3 = [
 task('09 · Поезд вагонов', ['ВПИШИ_ПАРОВОЗ','ВПИШИ_ВАГОН_1','ВПИШИ_ВАГОН_2'], 'Впиши паровоз и 2 вагона.', "['Паровоз', 'Вагон-лаборатория', 'Вагон-сад']", train),
 task('10 · Цепочка друзей', ['ВПИШИ_ДРУГА_1','ВПИШИ_ДРУГА_2','ВПИШИ_ДРУГА_3'], 'Впиши 3 имени друзей в цепочку.', "['Аня', 'Боря', 'Вика']", (c,f,w,h)=>{for(let i=0;i<3;i++){const x=130+i*150,y=h/2+Math.sin(f*.03+i)*30;c.strokeStyle='#ffd166';c.lineWidth=8;if(i<2){c.beginPath();c.moveTo(x+30,y);c.lineTo(x+120,y);c.stroke();}c.fillStyle=['#ff6574','#65e6bd','#9b8cff'][i];c.beginPath();c.arc(x,y,30,0,7);c.fill();}}),
 task('11 · Космический маршрут', ['ВПИШИ_СТАНЦИЮ_1','ВПИШИ_СТАНЦИЮ_2','ВПИШИ_СТАНЦИЮ_3'], 'Впиши 3 станции маршрута.', "['Луна', 'Марс', 'Юпитер']", (c,f,w,h)=>{c.strokeStyle='#65e6bd';c.lineWidth=3;c.beginPath();for(let i=0;i<3;i++){const x=130+i*180,y=h/2+Math.sin(f*.02+i)*70;i?c.lineTo(x,y):c.moveTo(x,y);c.fillStyle='#ffd166';c.arc(x,y,16,0,7);}c.stroke();}),
 task('12 · Музыкальная цепочка', ['ВПИШИ_НОТУ_1','ВПИШИ_НОТУ_2','ВПИШИ_НОТУ_3'], 'Впиши 3 ноты или названия звуков.', "['До', 'Ми', 'Соль']", (c,f,w,h)=>{for(let i=0;i<7;i++){c.fillStyle='#ff6574';c.beginPath();c.arc(100+i*95,h/2+Math.sin(f*.04+i)*45,14,0,7);c.fill();c.fillRect(112+i*95,h/2-55+Math.sin(f*.04+i)*45,5,55);}})
];
