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
    
    

});
})