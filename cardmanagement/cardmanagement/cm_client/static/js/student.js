$.ajax({
    type: "GET",
    url: "http://localhost:8021/api/v1/department/",
    success: function(data) {
        for(var i = 0; i<data.length; i++){
            var rows = $('<option value="'+data[i].id+'" valname="'+data[i].dept_name+'">'+data[i].dept_name+'</option>')
            $("#depart_dropdown").append(rows)
        }
    },
    error: function(data) {
        console.log(data);
    }
})


$.ajax({
    type: "GET",
    url: "http://localhost:8021/api/v1/semesters/",
    success: function(data) {
        for(var i = 0; i<data.length; i++){
            var rows = $('<option value="'+data[i].id+'">'+data[i].semester+'</option>')
            $("#semester_dropdown").append(rows)
        }
    },
    error: function(data) {
        console.log(data);
    }
})



$("#submitStudent").click(function() {
    let formData = new FormData();
    formData.append("first_name", $("#first_name").val());
    formData.append("last_name", $("#last_name").val());
    formData.append("father_name", $("#father_name").val());
    formData.append("email", $("#email").val());
    formData.append("phone", $("#phone").val());
    formData.append("address", $("#address").val());
    formData.append("password", $("#password").val());
    formData.append("semester_id", $("#semester_dropdown").val());
    formData.append("department_id", $("#depart_dropdown").val());
    formData.append("image", $('input[type=file]')[0].files[0]);
        first_name = $("#first_name").val();
        last_name = $("#last_name").val();
        father_name = $("#father_name").val();
        email = $("#email").val();
        phone = $("#phone").val();
        address = $("#address").val();
        password = $("#password").val();
        semester_id = $("#semester_dropdown").val();
        department_id = $("#depart_dropdown").val();
        image = $("#profile").val();
//        image = image.split("\\");
//        image = image[image.length - 1];
//        console.log("image : "+image);
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        student_data = JSON.stringify({
                        "first_name":first_name,
                        "last_name":last_name,
                        "father_name":father_name,
                        "email":email,
                        "phone":phone,
                        "address":address,
                        "password":password,
                        "semester_id":semester_id,
                        "department_id":department_id,
                        "image":image,
        })
        $.ajax({
            method: "POST",
            processData: false,
            contentType: false,
            cache: false,
            enctype: 'multipart/form-data',
            url: "http://localhost:8021/api/v1/student/",
//            dataType: 'json',
//            contentType: 'application/json',
            data: formData,
            headers: {
                "X-CSRFToken": csrftoken,
            },
            success: function(result){
                    console.log(result);
                    $("#student_alert").css("display", "block")
                    setTimeout(
                          function()
                          {
                            $("#student_alert").css("display", "none")
                          }, 2000);
                },
            error: function(result){
                alert(result.responseJSON.message);
            }
        });
 });
