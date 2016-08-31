angular.module('app')
.controller('TixitCtrl', function($scope, $location) {
  $scope.newEvent = function(){
    $location.path('/new_event')
  }
  $scope.findEvents = function(){
    $location.path('/all_events')
  }
})
