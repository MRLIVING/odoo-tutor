odoo.define(function (require) {
    var options = require('web_editor.snippets.options');

    options.registry.snippet_testimonial_options = options.Class.extend({
        onFocus: function () {
            console.log("snippet_testimonial_options On focus!")
        },
    });
});


