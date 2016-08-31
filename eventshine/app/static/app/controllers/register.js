angular.module('app')
.controller("registerCtrl", function($http, $location){
    $scope.registerUser = function() {
        $http({
            url: 'createUser/',
            method: 'POST',
            headers: {'Content-Type':      'application/x-www-form-urlencoded'},
            data: {
                'username': username,
                'password': password,
                'email': email,
                'first_name': firstName,
                'last_name': lastName,
            }
        }).success(() => {
            $location.path('/static/app/partials/new_event.html')
        })
    }
})
