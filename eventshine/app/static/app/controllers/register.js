angular.module('app')
.controller("registerCtrl", function($http, $location, $scope){
    const register = this;
    register.registerUser = function() {
        console.log('This works');
        $http({
            url: '/createUser/',
            method: 'POST',
            headers: {'Content-Type':      'application/x-www-form-urlencoded'},
            data: {
                'username': register.userName,
                'password': register.password,
                'email': register.email,
                'first_name': register.firstName,
                'last_name': register.lastName,
            }
        }).success(() => {
            $location.path('/static/app/partials/new_event.html')
        })
    }
})
