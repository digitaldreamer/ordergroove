var SITE = SITE || {};

requirejs.config({
    paths: {
        'backbone': 'libs/backbone',
        'bootstrap': 'libs/bootstrap',
        'jquery': 'libs/jquery-bootstrap',  // combined jquery and bootstrap
        'jquery.cookie': 'libs/jquery.cookie',
        'jquery.easing': 'libs/jquery.easing',
        'jquery.json': 'libs/jquery.json',
        'paper': 'libs/paper',
        'underscore': 'libs/underscore'
    },
    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        'underscore': {
            deps: ['jquery'],
            exports: '_'
        },
        'bootstrap': ['jquery'],
        'jquery.cookie': ['jquery'],
        'jquery.easing': ['jquery'],
        'jquery.json': ['jquery']
    }
});

require([
    'jquery',
    'underscore',
    'backbone'
], function($, _, Backbone) {
    console.log('ordergroove');
});
