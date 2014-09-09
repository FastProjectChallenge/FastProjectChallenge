'use strict';

(function() {

    var anymeterApp = angular.module('anymeterApp', ['ngRoute']); // app name, dependencies

    anymeterApp.config(['$routeProvider',
        function($routeProvider) {
            $routeProvider.

            when('/top', {
                templateUrl: 'index.html',
                controller: 'anymeterTopListCtrl' //,
                //resolve: anymeterTopListCtrl.resolve
            }).

            when('/singin', {
                templateUrl: 'singin.html',
                controller: 'anymeterSinginCtrl'
            }).
            when('/singup', {
                templateUrl: 'singup.html',
                controller: 'anymeterSingupCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
        }
    ]);



    anymeterApp.config(
        function($interpolateProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
        }
    );



    anymeterApp.controller('anymeterTopListCtrl', ['$scope', '$http',
        function($scope, $http) {

            var self = this;

            this.toppers = [];

            console.log(this.toppers);
            $http.get('/api/v1/relation/?format=json').then(function(response) {
                self.toppers = angular.copy(response.data.objects);
                //self.toppers = testTop;
                console.log(self.toppers, self.toppers[0], self.toppers.length);
            });

        }
    ]);


    anymeterApp.controller('anymeterSinginCtrl', ['$scope', '$routeParams',
        function($scope, $routeParams) {

        }
    ]);

    anymeterApp.controller('anymeterSingupCtrl', ['$scope', '$routeParams',
        function($scope, $routeParams) {

        }
    ]);

    var testTop = [{
        name: 'Name Lol',
        vote: 10,
        description: 'About me!',
        image: 'http://placehold.it/512x512',
        canPurchase: true,
    }, {
        name: 'asdsdf',
        vote: 7,
        description: 'descr',
        image: 'http://placehold.it/512x512',
        canPurchase: true,
    }, {
        name: 'asdasda',
        vote: 17,
        description: 'desthrtzntfbfdfvdsvdfsvdfvvdsfvd',
        image: 'http://placehold.it/512x512',
        canPurchase: true,
    }, {
        name: 'asdsdf',
        vote: 7,
        description: 'descr',
        image: 'http://placehold.it/512x512',
        canPurchase: true,
    }];

    //anymeterApp.factory('testTop', testTop);




})();