angular.module('app')

.controller('LoginCtrl', function($scope, $location, $http) {
  $scope.register = function() {
    $location.path('/home/')
  }
  // $scope.moveAlong = function() {
  //   $location.path('/tixit/')
  // }
})
