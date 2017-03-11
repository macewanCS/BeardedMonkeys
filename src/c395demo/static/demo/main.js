$(document).ready(function(){
    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];
    var yBtn = document.getElementById("yButton");
    var nBtn = document.getElementById("nButton");
    $( "a[id*='myBtn']" ).click(function(){
        id = $(this).attr('id').replace("myBtn_", "")
        $("#myModal").css("display", "block")
        if ($("#status_"+id).text().indexOf("Open")>=0){
            $("#modalText").html("Are you sure the ticket has been resolved?");
        } else {
                $("#modalText").html("Are you sure that you want to re-open the ticket?");
        }
        yBtn.onclick = function() {
           modal.style.display = "none";
           if ($("#status_"+id).text().indexOf("Open")>=0){
            alterData(id, "Resolved")
            //$("#status_"+id).html("Resolved");
            $("#myBtn_"+id).html('<i class="fa fa-check" aria-hidden="true"></i>Re-open');
           }
           else {
            alterData(id, "Open")
            $("#myBtn_"+id).html('<i class="fa fa-check" aria-hidden="true"></i>Resolved');
           }
        }
    });
    nBtn.onclick = function() {
        modal.style.display = "none";
    }

    span.onclick = function() {
        modal.style.display = "none";
    }
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        };
    };

    function alterData(id, status){
        console.log(id, status)
        console.log(window.location.host)
        $.ajax({
            url : window.location.origin+"/alter-status/", // the endpoint
            type : "POST", // http method
            data : { status : status, id: id }, // data sent with the post request

            // handle a successful response
            success : function(json) {
                $('#status_'+id).html(status); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log('error')
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
})
