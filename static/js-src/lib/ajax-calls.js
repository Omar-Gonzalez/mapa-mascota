const AJAX = require('./ajax-helpers');

function GlobalAjaxUpdate(){
    AJAX.html.replace({
        url:"v1/mascotas/feed",
        sel:"#ajax-node-feed"
    });

    AJAX.html.replace({
        url:"login",
        sel:".ajax-node-login"
    });

    AJAX.html.replace({
        url:"registro",
        sel:".ajax-node-registro"
    });

    AJAX.html.replace({
        url:"v1/mascotas/form/reporta",
        sel:".ajax-node-mascota-form"
    });  
}

module.exports = GlobalAjaxUpdate;