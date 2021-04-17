console.log(`Trabalhando com condicionais`)

const cidades = new Array(
    `Salvador`, `São Paulo`, `Rio de Janeiro`
)

console.log(cidades)

cidades.push(`Curitiba`) // add item na lista

console.log(cidades)

const idadeComprador = 17
const acompanhado = true

// if(idadeComprador >= 18){
//     cidades.splice(1, 1)
// }
// else{

//     if(acompanhado){
//         console.log("Menor de idade acompanhado")
//     }

//     else{
//         console.log("Não é maior de idade e esta desacompanhado")
//     }
// }

//console.log(cidades)

//console.log(idadeComprador > 18)
//console.log(idadeComprador < 18)
//console.log(idadeComprador >= 18)
//console.log(idadeComprador <= 18)
//console.log(idadeComprador == 18)

if(idadeComprador >= 18 || acompanhado){
    cidades.splice(1, 1)
    console.log("Boa viajem")
}
else
    console.log("Não é maior de idade e não esta desacompanhado")

