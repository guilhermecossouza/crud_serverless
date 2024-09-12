const btnRegister = document.querySelector("#btn-register-user");
const btnSearchUsers = document.querySelector("#btn-search-users");
const inputBusca = document.querySelector("#nome-emai")
const alertMessage = document.querySelector("#alert-message");
const tableUsers = document.querySelector(".table");

alertMessage.style.display = "none";

btnRegister.addEventListener("click", (event) => {
    window.location.href = "register_user.html?register=1";
});

const showMessage = () => {
    alertMessage.style.display = "block";    
}

const hideMessage = () => {
    alertMessage.style.display = "none";    
}

inputBusca.addEventListener("keypress", (event) => {
    if (inputBusca.value.trim().length > 0) {
        alertMessage.style.display = "none";  
    } else {
        alertMessage.style.display = "block";     
    }       
});

btnSearchUsers.addEventListener("click", (event) => { 
    if (inputBusca.value.trim() !== "") {
        hideMessage();
    } else {
        showMessage();         
    }
});

tableUsers.addEventListener("click", (event) => {
    if (event.target.closest(".icon-edit")) {
        const buttonEdidt = event.target.closest(".icon-edit");
        console.log("001");
    }else if(event.target.closest(".icon-delete")) {
        const buttondelete = event.target.closest(".icon-delete");
        console.log("002");
    }
});



