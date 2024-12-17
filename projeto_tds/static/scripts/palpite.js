function abrirPopup(){
    document.getElementById('popupPalpite').style.display = 'flex';
}

function fecharPopup(){
    document.getElementById('popupPalpite').style.display = 'none';
}


function enviarPalpite(){
    const form = document.getElementById('formPalpite');
    const timeA = form.timeA.value;
    const timeB = form.timeB.value;

    if (timeA === timeB){
        alert('Os times não podem ser iguais!');
        return;
    }

    fetch('/',
        {method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({timeA, timeB}),
    })
    .then(response=>response.json())
    .then(data => {
        alert('Palpite enviado com sucesso!');
        fecharPopup();
    })
    .catch(error => console.error('Erro ao enviar o palpite', error));

}