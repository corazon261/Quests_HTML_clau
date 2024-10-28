var numeroprimo = prompt("seu numero: ");
for (var i = 2; i * i <= numeroprimo; i++) {
    if (numeroprimo % i == 0) {
        console.log(numeroprimo + " não é um número primo");
        break;
    }
    else{
        console.log(numeroprimo + " é um número primo");
        break;
    }
}