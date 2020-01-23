odoo.define('website_floating_button_menu.website_floating_button_menu', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.MenuFloatingButton = publicWidget.Widget.extend({
	selector: '.st-menu-btn-container',
	events: {
		 'click .st-menu-button-main': '_openPanel',
		 'click .st-menu-panel': '_boxClick',
		 'click .st-menu-modal': '_modalClick',
	 },


	start: function () {
		 var def = this._super.apply(this, arguments);
		 this._clicks = 0;
	},
	
	_launchPanelAnim: function () {
		$(".st-menu-modal").fadeIn("300");
		 $(".st-menu-panel").animate({
		        opacity: "toggle",
		        height: "toggle"
		      }, 600);
	},
	
	_closePanelAnim: function () {
		$(".st-menu-modal").fadeOut("300");
		 $(".st-menu-panel").animate({
		        opacity: "hide",
		        height: "hide"
		      }, 200);
	},

	_openPanel: function (e) {
	      if (this._clicks === 0) {
	    	  $(".st-menu-button-main").removeClass('rotateBackward').toggleClass('rotateForward');  
	          this._launchPanelAnim();
	          this._clicks++;
	        } else {
	        	 $(".st-menu-button-main").removeClass('rotateForward').toggleClass('rotateBackward');
	          this._closePanelAnim();
	          this._clicks--;
	        }
	        e.preventDefault();
	        return false;
		
	},
	
	_boxClick: function (e) {
	      e.stopPropagation();	
	},
	
	_modalClick: function (e) {
	    },
	
});
});