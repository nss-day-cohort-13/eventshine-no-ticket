angular.module('app')
.controller('TixitCtrl', function($scope, $location) {
  $scope.open = function(){
    $location.path('/new_event')
  }
})
