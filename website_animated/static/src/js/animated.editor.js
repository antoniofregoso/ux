odoo.define('website_animations.editor', function (require) {
    'use strict';
    
    var core = require('web.core');
    const options = require('web_editor.snippets.options');
    
    options.registry.AnimatedCSS = options.Class.extend({
        
         /**
         * @see this.selectClass for parameters
         */
    
        
        _setOptionsDefaultValues: function () {},

        _onLinkClick: function (ev) {
            console.log('Hola');
        },
        
            
        
        
        
    });
    
    });