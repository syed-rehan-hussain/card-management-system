
$("#submitDepartment").click(function(){
        dept_name = $("#dept_name").val();
        dept_code = $("#dept_code").val();
        dept_phone = $("#dept_phone").val();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        depart_data = JSON.stringify({
                        "dept_name":dept_name,
                        "dept_code":dept_code,
                        "phone":dept_phone,
        })
        alert(depart_data)
        $.ajax({
            method: "POST",
            url: "http://localhost:8021/api/v1/department/",
            dataType: 'json',
            contentType: 'application/json',
            data: depart_data,
            headers: {
                "X-CSRFToken": csrftoken,
            },
            success: function(result){
                    console.log(result);
                    $("#depart_alert").css("display", "block")
                    setTimeout(
                          function()
                          {
                            $("#depart_alert").css("display", "none")
                          }, 2000);
                },
            error: function(result){
                alert(result.responseJSON.message);
            }
        });
 });