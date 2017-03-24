$(document).ready(function(){
    $( "a[id*='logout']" ).click(function(){
        $("#logoutModal").css("display", "block")
    });
    $( "a[id*='lit-log']" ).click(function(){
        $("#logoutModal").css("display", "block")
    });
    $( "a[id*='myBtn']" ).click(function(){
        id = $(this).attr('id').replace("myBtn_", "")
        $("#myModal").css("display", "block");
        if ($("#status_"+id).text().indexOf("Open")>=0){
            $("#modalText").html("Are you sure the ticket has been resolved?");
        } else {
                $("#modalText").html("Are you sure that you want to re-open the ticket?");
        }
        $("#yButton").click(function() {
           $("#myModal").css("display", "none");
           if ($("#status_"+id).text().indexOf("Open")>=0){
            alterData(id, "Resolved")
            //$("#status_"+id).html("Resolved");
            $("#myBtn_"+id).html('<i class="fa fa-check" aria-hidden="true"></i>Re-open');
           }
           else {
            alterData(id, "Open")
            $("#myBtn_"+id).html('<i class="fa fa-check" aria-hidden="true"></i>Resolved');
           }
        });
    });

    $(".nButton").click(function () {
        $(".modal").css("display", "none");
    });

    $(".close").click(function () {
        $(".modal").css("display", "none");
    });

    $('html').click(function(e) {
       if($(e.target).hasClass('modal') )
       {
           $(".modal").css("display", "none");
       }
    });

//    highlight field
    $("button").click(function(){
        $('input[required]').each(function(){
            if (!$(this).val()) {
               $(this).addClass("required")
            } else {
                $(this).removeClass("required")
            }

       });

       $('textarea[required]').each(function(){
            if (!$(this).val()) {
               $(this).addClass("required")
            } else {
                $(this).removeClass("required")
            }
       });
    });

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
