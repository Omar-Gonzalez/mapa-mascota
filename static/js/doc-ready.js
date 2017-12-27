/**
* Please consolidate all document ready functions in this file 
*/
$(document).ready(function() {
    /**
     * Update Sidebar 
     */
    $('.sb-toggle, .sb-close').click(function() {
        UI.sb.update();
    });
    /**
     * Update Auth Area
     */
    $('#auth-header').click(function() {
        UI.authArea.update();
    });
});