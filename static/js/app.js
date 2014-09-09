var anymeterApp = angular.module('anymeterApp', ['ngRoute']); // app name, dependencies

anymeterApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/top', {
            templateUrl: 'index.html',
            controller: 'anymeterTopListCtrl'
        }).
        when('/top/:phoneId', {
            templateUrl: 'partials/phone-detail.html',
            controller: 'PhoneDetailCtrl'
        }).
        otherwise({
            redirectTo: '/top'
        });
    }
]);





anymeterApp.controller('anymeterTopListCtrl', ['$scope', '$http',
    function($scope, $http) {
        /*$http.get('phones.json').success(function(data) {
            $scope.phones = data;
        });

        $scope.orderProp = 'age';*/
        $scope.toppers = testTop;
    }
]);

anymeterApp.controller('PhoneDetailCtrl', ['$scope', '$routeParams',
    function($scope, $routeParams) {
        $scope.phoneId = $routeParams.phoneId;
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