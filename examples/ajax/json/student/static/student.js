async function getStudent(){
    let reply = await fetch("/get_data");
    if (reply.status == 200){
        let result = await reply.json();
        document.getElementById("name").value = result.name;
        document.getElementById("student_no").value = result.student_no;
    }
}

async function sendStudent(){
    let student = {
        name: name, student_no: student_no
    };
    student.name = document.getElementById("name").value;
    student.student_no = document.getElementById("student_no").value;
    

    let reply = await fetch("/post_data",{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({name: name, student_no: student_no})
    });
    if (reply.status == 200){
        console.log("Success");
    }
}