function busca(){
    let username = document.getElementById('new').value
    username = username.toLowerCase()
    let n = document.getElementsByClassName('amizadesnovas')

    for (i = 0; i<n.length; i++){
        if(!n[i].innerHTML.toLowerCase().includes(username)){
            n[i].style.display = "none"
        }else{
            n[i].style.display = "list-item"
        }
    }
}
