document.getElementById("frm-usuario").addEventListener("submit",(formulario) => {
    formulario.preventDefault();
    let register = true;
    if(formulario.target.nome.value.trim() === "") {
        alert("Favor informar o nome.");    
        register = false    
    }

    if (formulario.target.email.value.trim() === "") {
        alert("Favor informar o e-mail.");
        register = false 
    } 

    if(register) {
        const user = {
            nome: formulario.target.nome.value.trim(),
            email: formulario.target.email.value.trim()
        }

        let url = "http://localhost:3000/dev/user/register"

        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(user)
            });

            console.log(response);

        } catch (error) {
            console.log("erro");
        }
    }

    
});