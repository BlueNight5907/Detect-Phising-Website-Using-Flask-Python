document.getElementById("submit")?.setAttribute("disabled",true);
document.getElementById("submit")?.addEventListener("click",()=>{
    let urlname = document.getElementById('url').value;
    let type = document.getElementById("type").value;

    let result = document.querySelector(".result")
    $.ajax({
        data : {
            name : urlname,
            type: type
        },
        type : 'GET',
        url : '/result'
    }).always(result.innerHTML= '<div class="loading-dots mt-4"><div class="loading-dots--dot"></div><div class="loading-dots--dot"></div><div class="loading-dots--dot"></div></div>')
    .done(function(data) {
        if (data.error) {
            alert(data.error);
        }
        else {
            if (data == "An error occurred during execution!!!") {
                result.innerHTML = "An error occurred during execution!!!"
                return
            }
            var newHTML = '<h3 class="text-white mt-4">This is a '+data+'</h3>';
            result.innerHTML=  newHTML;
        }

    });

})

document.getElementById("clear")?.addEventListener("click",()=>{
    console.log("clear")
    document.getElementById('url').value = "";
    document.getElementById("type")[0].selected = true;
    document.getElementById("submit").disabled = true;
})

document.getElementById("clear2")?.addEventListener("click",()=>{
    console.log("clear")
    document.getElementById('formFile').value = "";
    document.getElementById("type")[0].selected = true;
})


document.getElementById('url')?.addEventListener("keydown", ()=>{
    if(document.getElementById('url').value.length > 0){
        document.getElementById("submit").disabled = false;
    }
    else{
        document.getElementById("submit").disabled = true;
    }
})

document.getElementById('url')?.addEventListener("keyup", ()=>{
    if(document.getElementById('url').value.length > 0){
        document.getElementById("submit").disabled = false;
    }
    else{
        document.getElementById("submit").disabled = true;
    }
})


document.getElementById("submit2")?.addEventListener("click",()=>{
    let file = document.getElementById('formFile').files[0];
    let type = document.getElementById("type").value;
    let formData = new FormData();
    formData.append("file", file);
    formData.append("type", type);
    let result = document.querySelector(".result")
    document.getElementById('score').innerHTML = "";
    $.ajax({
        data:formData,
        processData: false,
        contentType:  false,
        type : 'POST',
        url : '/result'
    }).always(result.innerHTML= '<div class="loading-dots mt-4"><div class="loading-dots--dot"></div><div class="loading-dots--dot"></div><div class="loading-dots--dot"></div></div>')
        .done(function(data) {
            if (data.error) {
                alert(data.error);
            }

            if (data == "An error occurred during execution!!!") {
                result.innerHTML = "An error occurred during execution!!!"
                return
            }
            else if(!data){
                result.innerHTML=  "Invalid file data";
            }
            else {
                console.log(data);
                if(data == "No file has been upload"){
                    result.innerHTML = data
                    return;
                }
                result.innerHTML = "";    
                let accuracy_score = data["accuracy score"];
                accuracy_score = Math.ceil(accuracy_score*100)
                if(accuracy_score){
                    document.getElementById('score').innerHTML = `<p class="h4">Accuracy: ${accuracy_score}%</p>`;
                }
                list = data["result"]
                let table = document.createElement("table");
                table.classList.add("table")
                table.classList.add("align-middle")
                table.classList.add("table-hover")
                let thead = document.createElement("thead");
                let tr = document.createElement("tr");
                let th1 = document.createElement("th");
                th1.setAttribute("scope","col");
                th1.innerHTML = "Index";
                let th2 = document.createElement("th");
                th2.setAttribute("scope","col");
                th2.innerHTML = "URL";
                let th3 = document.createElement("th");
                th3.setAttribute("scope","col");
                th3.innerHTML = "Predict";
                tr.appendChild(th1)
                tr.appendChild(th2)
                tr.appendChild(th3)
                if(list && list[0]){
                    if(list[0]["right value"]){
                        let th4 = document.createElement("th");
                        th4.setAttribute("scope","col");
                        th4.innerHTML = "Right value";
                        tr.appendChild(th4)
                    }
                }
                thead.appendChild(tr)
                table.appendChild(thead)
                let tbody = document.createElement("tbody")
                list.forEach((e,index)=>{
                    let tr = document.createElement("tr");
                    let th = document.createElement("th");
                    th.setAttribute("scope","row");
                    th.innerHTML = index+1;

                    let domain = document.createElement("td");
                    domain.innerHTML = e.domain;
                    let predict = document.createElement("td");
                    predict.innerHTML = e.predict;
                    tr.appendChild(th)
                    tr.appendChild(domain);
                    tr.appendChild(predict);
                    if(e["right value"]){
                        let right_value = document.createElement("td");
                        right_value.innerHTML = e["right value"];
                        tr.appendChild(right_value);
                    }
                    tbody.appendChild(tr)
                })
                table.appendChild(tbody)
                result.appendChild(table)
            }

        });

})