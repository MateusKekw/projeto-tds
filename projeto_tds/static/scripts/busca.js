const username = document.getElementById('new');
username.addEventListener('input', (event) => {
    const value = event.target.value;

    console.log(formatString(value))
});

function formatString(value){
    return value.toLowerCase().trin();
}
