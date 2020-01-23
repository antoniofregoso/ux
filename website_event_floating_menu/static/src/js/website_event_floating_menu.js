odoo.define('website_event_floating_menu.website_event_floating_menu', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.EventFloatingButton = publicWidget.Widget.extend({
	selector: '#event_floating_button',
	events: {
		 'click .st-event-button-main': '_openPanel',
		 'click .st-event-panel': '_boxClick',
		 'click .st-event-modal': '_modalClick',
	 },

	start: function () {
		 var def = this._super.apply(this, arguments);
		 this._clicks = 0;
	},
	
	_launchPanelAnim: function () {
		$(".st-event-modal").fadeIn("300");
		 $(".st-event-panel").animate({
		        opacity: "toggle",
		        height: "toggle"
		      }, 600);
	},
	
	_closePanelAnim: function () {
		$(".st-event-modal").fadeOut("300");
		 $(".st-event-panel").animate({
		        opacity: "hide",
		        height: "hide"
		      }, 200);
	},

	_openPanel: function (e) {
	      if (this._clicks === 0) {
	    	  $(".st-event-button-main").removeClass('rotateBackward').toggleClass('rotateForward');  
	          this._launchPanelAnim();
	          this._clicks++;
	        } else {
	        	 $(".st-event-button-main").removeClass('rotateForward').toggleClass('rotateBackward');
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