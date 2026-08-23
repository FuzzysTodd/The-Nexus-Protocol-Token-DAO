/**
 * Vercel Web Analytics Integration for Nexus Protocol
 * 
 * This file initializes Vercel Web Analytics for the Nexus Protocol
 * Token DAO application using the vanilla JavaScript approach.
 * 
 * According to Vercel documentation, for vanilla JavaScript/HTML projects,
 * we initialize the analytics queue and inject the tracking script.
 */

(function() {
  'use strict';
  
  /**
   * Initialize the Vercel Analytics queue
   * This sets up the window.va function that queues events
   */
  function initQueue() {
    if (window.va) return;
    window.va = function a() {
      var params = Array.prototype.slice.call(arguments);
      (window.vaq = window.vaq || []).push(params);
    };
  }
  
  /**
   * Detect the environment (development or production)
   */
  function detectEnvironment() {
    // In production (deployed to Vercel), analytics will be active
    // In development (localhost), analytics will not send data
    return (window.location.hostname === 'localhost' || 
            window.location.hostname === '127.0.0.1' ||
            window.location.hostname === '') ? 'development' : 'production';
  }
  
  /**
   * Inject the Vercel Analytics script
   */
  function injectScript() {
    var mode = detectEnvironment();
    window.vam = mode;
    
    // Only inject script in production mode
    if (mode === 'production') {
      var script = document.createElement('script');
      script.src = '/_vercel/insights/script.js';
      script.defer = true;
      script.setAttribute('data-sdkn', '@vercel/analytics');
      script.setAttribute('data-sdkv', '1.6.1');
      
      // Add error handling
      script.onerror = function() {
        console.warn('[Nexus Analytics] Failed to load Vercel Analytics script');
      };
      
      // Insert the script
      var firstScript = document.getElementsByTagName('script')[0];
      if (firstScript && firstScript.parentNode) {
        firstScript.parentNode.insertBefore(script, firstScript);
      } else {
        document.head.appendChild(script);
      }
      
      console.log('[Nexus Analytics] Vercel Web Analytics initialized (production mode)');
    } else {
      console.log('[Nexus Analytics] Running in development mode - analytics disabled');
    }
  }
  
  /**
   * Initialize Vercel Web Analytics
   */
  function initAnalytics() {
    // Initialize the queue first
    initQueue();
    
    // Then inject the script
    injectScript();
  }
  
  // Auto-initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAnalytics);
  } else {
    // DOM is already ready
    initAnalytics();
  }
  
  // Expose initialization function globally if needed
  window.NexusAnalytics = {
    init: initAnalytics,
    track: function(eventName, properties) {
      if (window.va) {
        window.va('event', eventName, properties);
      }
    }
  };
})();
