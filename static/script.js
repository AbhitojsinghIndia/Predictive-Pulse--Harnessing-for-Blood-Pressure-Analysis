const button = document.getElementById("predictBtn");

if(button){

    button.addEventListener("click", function(){

        button.innerHTML = "Analyzing...";

        button.style.opacity = "0.8";

    });

}

const resultBox = document.querySelector(".result-box");

if(resultBox){

    resultBox.style.opacity = "0";

    setTimeout(() => {

        resultBox.style.opacity = "1";

        resultBox.style.transition = "1s";

    }, 300);

}