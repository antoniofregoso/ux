odoo.define('website_instant_messaging.website_instant_messaging', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.IMFloatingButton = publicWidget.Widget.extend({
	selector: '.st-messagingContainer',
	events: {
		 'click .st-messaging-button-main': '_openPanel',
		 'click .st-messaging-panel': '_boxClick',
		 'click .st-messaging-modal': '_modalClick',
	 },


	start: function () {
		 var def = this._super.apply(this, arguments);
		 this._clicks = 0;
		 this._mainBtn = $(".st-messaging-button-main")
	},
	
	_launchPanelAnim: function () {
		$(".st-menu-modal").fadeIn("300");
		 $(".st-messaging-panel").animate({
		        opacity: "toggle",
		        height: "toggle"
		      }, 600);
	},
	
	_closePanelAnim: function () {
		$(".st-menu-modal").fadeOut("300");
		 $(".st-messaging-panel").animate({
		        opacity: "hide",
		        height: "hide"
		      }, 200);
	},

	_openPanel: function (e) {
	      if (this._clicks === 0) {
	    	  this._mainBtn.removeClass('rotateBackward').toggleClass('rotateForward');  
	          this._launchPanelAnim();
	          this._clicks++;
	        } else {
	        	this._mainBtn.removeClass('rotateForward').toggleClass('rotateBackward');
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
		this._closePanelAnim();
	      if (this._clicks === 1) {
	    	  this._mainBtn.removeClass('rotateForward').toggleClass('rotateBackward');
	        }
	      this._clicks = 0;
	    },
	
});
});