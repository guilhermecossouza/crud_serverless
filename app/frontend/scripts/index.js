const api_integration_config = () => {
    fetch("http://localhost:3000/dev/user/config/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }    
    }).then(response => {
        if (response.ok) {
            console.log("zaca");
            console.log(response.json())
        }else {
            console.log("fudeu")
        }
        
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
        fetch("http://localhost:3000/dev/user/create/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(objecUser)
        }).then(response => {
            console.log(response.json());
        }).then(data => {
            console.log("sucesso:", data);        
        }).catch((error) => {
            console.log("Erro:", error);
        });
    }
});