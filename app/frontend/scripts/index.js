const api_integration_config = () => {
    fetch("http://localhost:3000/dev/user/config/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }    
    }).then(response => {
        console.log(response)
    }).catch(error => {
        console.error(error)    
    });
}

api_integration_config();


document.querySelector("#frm-usuario").addEventListener("submit", (event) => {
    event.preventDefault();
    let formIsVelid = true
    if (event.target.nome.value.trim() === "") {
        formIsVelid = false;
        event.target.nome.style = "border-color: red;";

    }else {
        formIsVelid = true;
        event.target.nome.style = "border-color: none;";
    }

    if (event.target.email.value.trim() === "") {
        formIsVelid = false;
        event.target.email.style = "border-color: red;";
    }else {
        formIsVelid = true;
        event.target.email.style = "border-color: none;";
    }

    if (formIsVelid) {
        let objecUser = {
            "nome": event.target.nome.value.trim(),
            "email": event.target.email.value.trim()
        }
    }
});