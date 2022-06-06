
$("#submitCourse").click(function(){
        course_name = $("#course_name").val();
        course_description = $("#course_description").val();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        course_data = JSON.stringify({
                        "course_name":course_name,
                        "description":course_description,
        })
        $.ajax({
            method: "POST",
            url: "http://localhost:8021/api/v1/course/",
            dataType: 'json',
            contentType: 'application/json',
            data: course_data,
            headers: {
                "X-CSRFToken": csrftoken,
            },
            success: function(result){
                    console.log(result);
                    $("#course_alert").css("display", "block")
                    setTimeout(
                          function()
                          {
                            $("#course_alert").css("display", "none")
                          }, 2000);
                },
            error: function(result){
                alert(result.responseJSON.message);
            }
        });
 });
