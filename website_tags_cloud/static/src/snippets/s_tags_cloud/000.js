odoo.define('website_tag_cloud.website_tags_cloud_frontend', function (require) {
    'use strict';
    
    var core = require('web.core');
    var wUtils = require('website.utils');
    var publicWidget = require('web.public.widget');
    
    var _t = core._t;
    
    
    publicWidget.registry.js_get_tags = publicWidget.Widget.extend({
        selector: '.js_get_tags',
        disabledInEditableMode: false,
    
        //init: function () {},
        
        start: function () {
            var self = this;
            const data = self.$target[0].dataset;
            const cloudID = parseInt(data.filterByCloudId);
            const template = data.template || 'website_tags_cloud.s_tags_cloud_template';
            this.$target.empty(); // Compatibility with db that saved content inside by mistake
            this.$target.attr('contenteditable', 'False'); // Prevent user edition

            var domain = [];
            if (cloudID) {
                domain.push(['cloud_id', '=', cloudID]);
            }
            const tagsURL = '/tags-cloud/get_tags/cloud/' + cloudID
            var prom = new Promise(function (resolve) {
                   self._rpc({
                       route: tagsURL,
                       params: {
                           template: template,
                           domain: domain,
                       },
                   }).then(function(tags) {
                       self.$target.html(tags);
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
    
    });