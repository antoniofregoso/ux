odoo.define('website_tag_cloud.website_tags_cloud_frontend', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.js_get_tags = publicWidget.Widget.extend({
    selector: '.js_get_tags',
    disabledInEditableMode: false,

    //init: function () {},
    
    willStart: function () {
    	var self = this;
    	var cloudID = self.$target.data('filterByCloudId');
    	var template = self.$target.data('template') || 'website_tags_cloud.s_tags_cloud_template';
    	var domain = [];
    	var tagsURL = '/tags-cloud/get_tags/cloud/' + cloudID
    	var prom = new Promise(function (resolve) {
      		 self._rpc({
                   route: tagsURL,
                   params: {
                       template: template,
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