odoo.define('website_caramba_snippets.s_social_frontend', function (require) {
'use strict';

var core = require('web.core');
var wUtils = require('website.utils');
var publicWidget = require('web.public.widget');

var _t = core._t;

publicWidget.registry.js_get_social = publicWidget.Widget.extend({
    selector: '.js_get_social',
    disabledInEditableMode: true,
    
    /**
     * @override
     */
    start: function () {
         var self = this;
         const data = self.$target[0].dataset;
         const template = data.template || 'website_caramba_snippets.s_social_template';
         var domain = [];
         var prom = new Promise(function (resolve) {
    		 self._rpc({
                 route: '/caramba/get_social_media',
                 params: {
                     template: template,
                 },
    		 }).then(function(social_media) {
    			 self.$target.html(social_media);
    			 resolve();
    		 }).guardedCatch(function () {
    			 
    		 });
    		 resolve(); 
    	 });
    	 return Promise.all([this._super.apply(this, arguments), prom]);
    },
    
    destroy: function () {
        this.$target.empty();
        this._super.apply(this, arguments);
    },
        
    	
   
})    
})