function CreateEmail(){
    ToggleButtonsDisable();
    ErroEmail();
}

function CreateSenha(){
    ToggleButtonsDisable();
    ErroSenha();
}

function ConfirmSenha(){
    ToggleButtonsDisable();
    ConfirmSenhaError();
}

function validEmail(email){
    return /\S+@\S+\.\S+/.test(email);
}

function isEmailvalid(){
    const email = document.getElementById("iEmail").value;
    if(!email){
        return false;
    }
    return validEmail(email);
}

function IsPasswordValid(){
    const CrSenha = document.getElementById("iPassword").value;
    if(!CrSenha){
        return false;
    }
    return true;
}

function IsConfirmPasswordValid(){
    const Csenha = document.getElementById("ic-Password").value;
    if(!Csenha || Csenha!=CrSenha){
        return false;
    }
    return true;
}

function ErroEmail(){
    const email = document.getElementById("iEmail").value;
    if(!email){
        document.getElementById("E-required").style.display = 'block';
    } else{
        document.getElementById("E-required").style.display = 'none';
    }

    if(validEmail(email)){
        document.getElementById("Invalid-email").style.display = 'none';
    } else{
        document.getElementById("Invalid-email").style.display = 'block';
    }
}

function ErroSenha(){
    const senha = document.getElementById("iPassword").value;
    if(!senha){
        document.getElementById("P-required").style.display = 'block';
    } else{
        document.getElementById("P-required").style.display = 'none';
    }
}

function ConfirmSenhaError(){
    const newsenha = document.getElementById("iPassword").value;
    const confirm = document.getElementById("ic-Password").value;
    if(confirm != newsenha){
        document.getElementById("CP-password").style.display = 'block';
    } else if (!confirm){
        document.getElementById("No-password").style.display = 'block';
    } else{
        document.getElementById("CP-password").style.display = 'none';
        document.getElementById("No-password").style.display = 'none';
    }
}

function TButtonsDisable(){
    const emailV = isEmailvalid()
    const senhaV = IsPasswordValid();
    const senhaconfirm = IsConfirmPasswordValid();
    document.getElementById("ConfirmCadastro").disabled = !senhaV || !emailV || !senhaconfirm;
}