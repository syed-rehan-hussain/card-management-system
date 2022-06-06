$.ajax({
    type: "GET",
    url: "http://localhost:8021/api/v1/student/",
    success: function(data) {

        for(var i = 0; i<data.length; i++){
               console.log(data[i]);
//            var rows = $('<option value="'+data[i].id+'">'+data[i].first_name+'</option>')
            var rows = $('<div class="row1" id="container"><div class="column"><div class="card" style="background-image: url(http://localhost:8021/static/images/card/newcardfront.png); background-repeat: no-repeat; background-size: cover; background-size: 100% 100%;"><img id="output" src='+data[i].image+' width="87px" height="87px" style="margin-top:24%; border-radius:250px;"/><h3  style="margin-top:7%; color:white; font-size:1.2em;">'+data[i].first_name+' '+data[i].last_name+'</h3><p style="margin:15% 0 0 0; color:black; font-size:0.8em;" >FATHER NAME</p><p style="margin:0; color:black; font-size:1.1em;">'+data[i].father_name+'</p><p style="margin:0; color:black; font-size:1em;">'+data[i].semester_id+'</p><p style="margin:0; color:black; font-size:1em;"><b>'+data[i].department_id+'</b></p></div></div><div class="column"><div class="card" style="background-image: url(http://localhost:8021/static/images/card/cardbacknew.png); background-repeat: no-repeat; background-size: cover; background-size: 100% 100%;"><h3 style="margin-top:40%; font-size:1.2em;">Address</h3><p style="margin:7% 0 0 0;">'+data[i].address+'</p><p style="margin:23% 0 0 0;">Candidate keep this card very carefully & show it on demand</p><p style="margin:0;">if found please return to</p><p style="margin:0;"><b>UNIVERSITY OF KARACHI</b></p><p style="margin:0;">Student Advisor Office</p></div></div></div>')
            $("#container").append(rows)
        }
    },
    error: function(data) {
        console.log(data);
    }
})