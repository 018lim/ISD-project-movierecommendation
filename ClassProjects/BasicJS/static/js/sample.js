function sample(){
    alert('hello from js/sample.js!');
}

window.addEventListener("load",function (event){
    document.getElementById("one").addEventListener("click", function (event){
        alert('hithere');
    });
});