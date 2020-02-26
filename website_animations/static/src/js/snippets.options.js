odoo.define('website_animations.snippets.options', function (require) {
'use strict';

var core = require('web.core');
var sOptions = require('web_editor.snippets.options');
var wUtils = require('website.utils');

sOptions.registry.js_set_animation = sOptions.Class.extend({
	
	animation:function (previewMode, value, $opt) {
        value = parseInt(value);
        this.$target.attr('data-animation', value).data('animation', value);
        this.trigger_up('widgets_start_request', {
            editableMode: true,
            $target: this.$target,
        });
    },
    
    _setActive: function () {
        this._super.apply(this, arguments);

        this.$el.find('[data-animation]').removeClass('active');
        this.$el.find('[data-animation=' + this.$target.attr('data-interval') + ']').addClass('active');
    },

});
});