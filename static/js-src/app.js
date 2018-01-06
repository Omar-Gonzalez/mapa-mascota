/**
* Dependencies
*/
//import 'bootstrap'; not yet used 

/**
* Required Modules
*/

const GlobalAjaxUpdate = require('./lib/ajax-calls');
const UI = require('./lib/ui-scripts');
const ApplyDjangoSpecificStyles = require('./lib/django-styles.js');

/**
* Consolidate Event Listeners Here 
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
    /**
     * Ajax Update 
     */
    GlobalAjaxUpdate();
    /**
     * Django Styles
     */
    ApplyDjangoSpecificStyles();
});