console.log(`\n Trabalhando com condicionais`)
const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

const idadeComprador = 18
const estaAcompanhada = false
let temPassagemComprada = false
const destino = "Salvador"

console.log("\n Destinos possíveis:")
console.log(listaDeDestinos)

const podeComprar = idadeComprador >= 18 || estaAcompanhada == true

let contador = 0
let destionExiste = false
while(contador<3){
    if (listaDeDestinos[contador] == destino){
        destionExiste = true
        break
    }
    contador += 1
}

//console.log("Destino existe?", destionExiste)

if(podeComprar && destionExiste){
    console.log("Boa viajem")
}
else{
    console.log("Desculpe, algo está errado")
}

for(let i = 0 ; i < 3 ; i++){
    if (listaDeDestinos[i] == destino){
        destionExiste = true
        break
    }
}