/**
 * Please consolidate all document ready and ajax stopfunctions here
 */

const GlobalAjaxUpdate = require('./ajax-calls');
const UI = require('./ui-scripts');

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
    /**
     *Initial Ajax Calls
     */
    GlobalAjaxUpdate();
});

$(document).ajaxStop(function() {
    /**
     * Attach boostrap styles to forms
     */
    $("input, textarea, select").addClass("form-control");
    $("form:button").addClass("btn btn-primary");

    $("form").each(function() {
        $(this).find("button").addClass("btn btn-primary");
    });
    /**
     * Update Reporta Mascota Form Area
     */
    $("#reporta-header").click(function() {
        UI.reportaMascota.update();
    });
    /**
     * Update Auth Area
     */
    $('.auth-area-toggle').click(function() {
        UI.authArea.update();
    });
});