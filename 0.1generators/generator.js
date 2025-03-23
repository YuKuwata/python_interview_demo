/* 
    1. 箭头函数不能生成genarator
*/


// function assignment
const gen = function* (maxNum) {
    let current = 0;
    while (current < maxNum) {
        yield current;
        current++;
    }
}

const generator = gen(3);

console.log(generator.next().value);

for (const i of generator) {
    console.log(`iter: ${i}`);
}

function* generatorWithSend() {
    const received = yield 'Start';
    const received2 = yield `received: ${received}`
    yield `received2: ${received2}`
}

const genSend = generatorWithSend();
console.log(genSend.next());
console.log(genSend.next('Hello'));
console.log(genSend.next('Hi'));