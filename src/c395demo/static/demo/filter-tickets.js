// -------------------------------------------------------
// citation: http://stackoverflow.com/a/5150486/4054527
$(function(){
    // bind change event to select
    $('#dynamic_select').on('change', function () {
        var url = $(this).val(); // get selected value
        if (url) { // require a URL
            window.location = url; // redirect
        }
    });
});
// -------------------------------------------------------

// filters the tickets based on category or status
function filters (visible){
    switch (visible) {
        // filter based on category of tickets
        case 'hardware':
            $("option[value='/manage-tickets/?ticketType=hardware']").attr("selected","selected");
            break;
        case 'software':
            $("option[value='/manage-tickets/?ticketType=software']").attr("selected","selected");
            break;
        case 'service':
            $("option[value='/manage-tickets/?ticketType=service']").attr("selected","selected");
            break;
        case 'password':
            $("option[value='/manage-tickets/?ticketType=password']").attr("selected","selected");
            break;
        case 'other':
            $("option[value='/manage-tickets/?ticketType=other']").attr("selected","selected");
            break;
        // filter based on the status of the tickets
        case 'open':
            $("option[value='/manage-tickets/?ticketType=open']").attr("selected","selected");
            break;
        case 'progress':
            $("option[value='/manage-tickets/?ticketType=progress']").attr("selected","selected");
            break;
        case 'resolved':
            $("option[value='/manage-tickets/?ticketType=resolved']").attr("selected","selected");
            break;
        case 'closed':
            $("option[value='/manage-tickets/?ticketType=closed']").attr("selected","selected");
            break;
        case 'needsapproval':
            $("option[value='/manage-tickets/?ticketType=needsapproval']").attr("selected","selected");
            break;
        case 'unapproved':
            $("option[value='/manage-tickets/?ticketType=unapproved']").attr("selected","selected");
            break;
        case 'disapproved':
            $("option[value='/manage-tickets/?ticketType=disapproved']").attr("selected","selected");
            break;
        default:
            if(visible != null) {
	            $("option[value='/manage-tickets/?ticketType=" + visible + "']").attr("selected","selected");
            }
            if(visible == "all") {
	            $("option[id='selected']").attr("selected","selected");
            }
    }
}
