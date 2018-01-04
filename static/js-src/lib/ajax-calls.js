const AJAX = require('./ajax-helpers');

function GlobalAjaxUpdate() {
    let group = $("#ajax-group").val();

    if (group === "home") {
        AJAX.html.replace({
            url: "/v1/mascotas/feed",
            sel: "#ajax-node-feed"
        });

        AJAX.html.replace({
            url: "/v1/usuario/propio",
            sel: ".ajax-node-usuario-propio"
        });
    }

    if (group === "perfil" || group === "reporta") {

        AJAX.html.replace({
            url: "/v1/usuario/propio",
            sel: ".ajax-node-usuario-propio"
        });
    }
}

module.exports = GlobalAjaxUpdate;