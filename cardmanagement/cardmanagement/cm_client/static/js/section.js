
$("#submitSection").click(function(){
        section_no = $("#section_name").val();
        section_year = $("#section_year").val();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        section_data = JSON.stringify({
                        "section_no":section_no,
                        "section_year":section_year,
        })
        $.ajax({
            method: "POST",
            url: "http://localhost:8021/api/v1/section/",
            dataType: 'json',
            contentType: 'application/json',
            data: section_data,
            headers: {
                "X-CSRFToken": csrftoken,
            },
            success: function(result){
                    console.log(result);
                    $("#section_alert").css("display", "block")
                    setTimeout(
                          function()
                          {
                            $("#section_alert").css("display", "none")
                          }, 2000);
                },
            error: function(result){
                alert(result.responseJSON.message);
            }
        });
 });
