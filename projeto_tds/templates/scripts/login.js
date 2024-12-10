function OnChangeEmail(){
    ToggleButtonsDisable();
    Emailerror();
}

function OnChangeSenha(){
    ToggleButtonsDisable();
    Passworderror();
}

function validateEmail(email){
    return /\S+@\S+\.\S+/.test(email);
}

function isEmailvalid(){
    const email = document.getElementById("iE-mail").value;
    if(!email){
        return false;
    }
    return validateEmail(email);
}

function IsPasswordValid(){
    const senha = document.getElementById("iSenha").value;
    console.log("senha: "+ senha);
    if(!senha){
        return false;
    }
    return true;
}

function Emailerror(){
    const email = document.getElementById("iE-mail").value;
    if(!email){
        document.getElementById("Email-required").style.display = 'block';
    } else{
        document.getElementById("Email-required").style.display = 'none';
    }

    if(validateEmail(email)){
        document.getElementById("Wrong-email").style.display = 'none';
    } else{
        document.getElementById("Wrong-email").style.display = 'block';
    }
}

function Passworderror(){
    const senha = document.getElementById("iSenha").value;
    if(!senha){
        document.getElementById("Password-required").style.display = 'block';
    } else{
        document.getElementById("Password-required").style.display = 'none';
    }
}

function ToggleButtonsDisable(){
    const emailV = isEmailvalid()
    const senhaV = IsPasswordValid();
    document.getElementById("enter").disabled = !senhaV || !emailV;
}

/*

if(!email){
        document.getElementById("forgot-senha").disabled = true;
    } else if(validateEmail(email)){
        document.getElementById("forgot-senha").disabled = false;
    } else{
        document.getElementById("forgot-senha").disabled = true;
    }

function validarEmail(email){
    const email = document.getElementById("iE-mail").value;
    usuario = email.value.substring(0, email.value.indexOf("@"));
    dominio = email.value.substring(email.value.indexOf("@")+ 1, email.value.length);
    
    if ((usuario.length >=1) &&
        (dominio.length >=3) &&
        (usuario.search("@")==-1) &&
        (dominio.search("@")==-1) &&
        (usuario.search(" ")==-1) &&
        (dominio.search(" ")==-1) &&
        (dominio.search(".")!=-1) &&
        (dominio.indexOf(".") >=1)&&
        (dominio.lastIndexOf(".") < dominio.length - 1)) 
    {
        document.getElementById("iE-mail").innerHTML="E-mail válido";
        alert("E-mail valido");
        document.getElementById("iE-mail").disabled = false;
    }
    else{
        document.getElementById("iE-mail").innerHTML="<font color='red'>E-mail inválido </font>";
        alert("E-mail invalido");
        document.getElementById("iE-mail").disabled = true;
    }
}
*/