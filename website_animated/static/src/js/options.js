odoo.define('website_animated.animated_editor', function (require) {
'use strict';

const options = require('web_editor.snippets.options');


options.registry.AnimatedCSS = options.Class.extend({
    /**
    * @override
    */
    start: function () {
        const _objs = document.querySelectorAll('[data-animated]');
        _objs.forEach(animation => {
            animation.classList.forEach(_class => {
                if (_class.startsWith('animate__')){
                animation.classList.remove(_class);
                }
            });
        });
    },
   
});
});
