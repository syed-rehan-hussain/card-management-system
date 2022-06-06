$.ajax({
    type: "GET",
    url: "http://localhost:8021/api/v1/section/",
    success: function(data) {
//        console.log(data);
        for(var i = 0; i<data.length; i++){
//            console.log(i)
            var rows = $('<option value="'+data[i].id+'">'+data[i].section_no+'</option>')
            $("#section_dropdown").append(rows)
        }
    },
    error: function(data) {
        console.log(data);
    }
})

$.ajax({
    type: "GET",
    url: "http://localhost:8021/api/v1/course/",
    success: function(data) {
        console.log(data);
        for(var i = 0; i<data.length; i++){
            console.log(i)
            var rows = $('<option value="'+data[i].id+'">'+data[i].course_name+'</option>')
            $("#course_dropdown").append(rows)
        }
    },
    error: function(data) {
        console.log(data);
    }
})



$("#submitSemester").click(function(){
        semester_name = $("#semester_name").val();
        start_date = $("#start_date").val();
        end_date = $("#end_date").val();
        section_id = $("#section_dropdown").val();
        course_id = $("#course_dropdown").val();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        semester_data = JSON.stringify({
                        "semester":semester_name,
                        "start_date":start_date,
                        "end_date":end_date,
                        "section_id":section_id,
                        "course_id":course_id,
        })
        $.ajax({
            method: "POST",
            url: "http://localhost:8021/api/v1/semester/",
            dataType: 'json',
            contentType: 'application/json',
            data: semester_data,
            headers: {
                "X-CSRFToken": csrftoken,
            },
            success: function(result){
                    console.log(result);
                    $("#semester_alert").css("display", "block")
                    setTimeout(
                          function()
                          {
                            $("#semester_alert").css("display", "none")
                          }, 2000);
                },
            error: function(result){
                alert(result.responseJSON.message);
            }
        });
 });
