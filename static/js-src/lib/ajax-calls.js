const AJAX = require('./ajax-helpers');

function GlobalAjaxUpdate() {
    /**
    * Build Feed Query with data attributes
    */

    let query = $('#ajax-node-feed').attr('data-query');
    let feedUrl = "";
    if (query) {
        feedUrl = "/mascotas/feed/" + query;
    } else {
        feedUrl = "/mascotas/feed";
    }

    /**
    * Feed Call 
    */

    AJAX.html.replace({
        url: feedUrl,
        sel: "#ajax-node-feed"
    });

    /**
     * User widget related calls:
     */

    AJAX.html.replace({
        url: "/usuario/propio",
        sel: ".ajax-node-usuario-propio"
    });

    if ($("#ajax-query-value").val() !== undefined) {
        AJAX.html.replace({
            url: "/usuario/" + $("#ajax-query-value").val(),
            sel: ".ajax-node-usuario"
        });
    }
}

module.exports = GlobalAjaxUpdate;