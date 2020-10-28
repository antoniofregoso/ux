odoo.define('website_services.s_services', function (require) {
    'use strict';
    
    var wUtils = require('website.utils');
    var publicWidget = require('web.public.widget');
    
  
    
    publicWidget.registry.js_get_services = publicWidget.Widget.extend({
        selector: '.crmb-services-container',
        
        /**
         * @override
         */
        start: function () {
            var self = this;
            const data = self.$target[0].dataset;
            const template = data.template || 'website_services.s_services_template';
            this.$target.empty(); // Compatibility with db that saved content inside by mistake
            this.$target.attr('contenteditable', 'False'); // Prevent user edition

            var domain = [];   
            const servicesURL = '/services/get_services'        
            var prom = new Promise(function (resolve) {
                self._rpc({
                    route: servicesURL,
                    params: {
                        template: template,
                        domain: domain,
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
