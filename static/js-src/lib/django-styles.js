function ApplyDjangoSpecificStyles() {
    /**
     *Django Forms errors wrappers 
     */
    $('.helptext').each(function(index, value) {
        if ($(value).text().length > 0) {
            $(value).wrap("<div class=\"alert alert-info\" role=\"alert\"></div>");
        }
    });
    $('.errorlist').wrap("<div class=\"alert alert-danger\" role=\"alert\"></div>");
    $('ul').not('[class]').wrap("<div class=\"alert alert-warning\" role=\"alert\"></div>");
    /**
     * Attach boostrap styles to forms
     */
    $("input, textarea, select").addClass("form-control");
    $("form:button").addClass("btn btn-primary");

    $("form").each(function() {
        $(this).find("button").addClass("btn btn-primary");
    });
}

module.exports = ApplyDjangoSpecificStyles;