odoo.define('website_services.s_services.js', function (require) {
'use strict';

var core = require('web.core');
var wUtils = require('website.utils');
var publicWidget = require('web.public.widget');
//var swiper = require('website_swiper.SwiperRenderer')

var _t = core._t;

publicWidget.registry.js_get_services = publicWidget.Widget.extend({
    selector: '.swiper-container',
    disabledInEditableMode: true,
    
    /**
     * @override
     */
    start: function () {
        var self = this;
        var template = self.$target.data('template') || 'website_services.s_services_template';
        var domain = [];
        var prom = new Promise(function (resolve) {
   		 self._rpc({
                route: '/services/get_services',
                params: {
                    template: template,
                },
   		 }).then(function(services) {
   			 self.$target.html(services);
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
    
    
  

});

})