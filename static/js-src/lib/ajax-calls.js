const AJAX = require('./ajax-helpers');

function GlobalAjaxUpdate() {
    /**
     * Feed de Mascotas Calls:
     */

    if ($('#ajax-node-feed').length > 0) {
        let query = $('#ajax-node-feed').attr('data-query');
        let url = "";

        if(query){
            url = "/mascotas/feed/" + query;
        }else{
            url = "/mascotas/feed";
        }

        AJAX.html.replace({
            url: url,
            sel: "#ajax-node-feed"
        });
    }

    /**
     * User widget related calls:
     */

    if ($('.ajax-node-usuario-propio').length > 0) {
        AJAX.html.replace({
            url: "/usuario/propio",
            sel: ".ajax-node-usuario-propio"
        });
    }

    if ($('.ajax-node-usuario').length > 0) {
        let value = $("#ajax-query-value").val();

        AJAX.html.replace({
            url: "/usuario/" + value,
            sel: ".ajax-node-usuario"
        });
    }
}

module.exports = GlobalAjaxUpdate;