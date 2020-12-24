odoo.define('website_animated.animated_editor', function (require) {
'use strict';


const options = require('web_editor.snippets.options');


    options.registry.AnimatedEditor = options.Class.extend({
        /**
         * @override
         */
        start: function () {
            console.log('Puto');
        },

    
});
});
