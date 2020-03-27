odoo.define('website_animations.snippets.options', function (require) {
'use strict';

var core = require('web.core');
var sOptions = require('web_editor.snippets.options');
var wUtils = require('website.utils');

var _t = core._t;
var qweb = core.qweb;

sOptions.registry.js_set_animated = sOptions.Class.extend({
	
	 /**
     * @see this.selectClass for parameters
     */

    
	_onLinkClick: function (ev) {
		 var option = $(ev.target).closest('we-button').attr('data-animated');
			 this.$el.find('[data-animated="' + this.animation + '"]').removeClass('active');
			 this.$target.find('[data-animated]').attr('data-animated', option);
			 this.$el.find('[data-animated="' + option + '"]').addClass('active');
			 this.animation = option;
	},
	
	
	 _setActive: function () {
		 this._super.apply(this, arguments);	
		 this.animation =  this.$target.find('[data-animated]').data('animated');
		 if (this.animation== undefined){
			 this.animation = 'none';
			var w = this.$target.prop('data-animated', 'Puto');
			 alert(w.html());
		 }
		 this.$el.find('[data-animated="' + this.animation + '"]').addClass('active');
	 },
	
});

});