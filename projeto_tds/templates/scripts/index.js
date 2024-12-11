const brasileirao = "https://api.api-futebol.com.br/v1/campeonatos/10"

//pegar os jogos
async function GetGames(){

    const resposta = await fetch(brasileirao);

    console.log(resposta);

    const jogos = await resposta.json();

    console.log(jogos);
}

GetGames();