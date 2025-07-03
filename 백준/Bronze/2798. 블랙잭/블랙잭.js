// const prompt = require('prompt-sync')();
// const input = prompt();
// const inputList = prompt();


const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const cardList = input[1].split(' ').map(Number);

let max = 0;


for (let i = 0; i < N; i++) {
    for (let j = i+1; j < N; j++) {
        for (let k = j+1; k < N; k++) {
            let sum = cardList[i] + cardList[j] + cardList[k];
            if (sum <= M) {
                if (sum > max) {
                    max = sum;
                    
                }
            }
            
        }
    }

}

console.log(max);