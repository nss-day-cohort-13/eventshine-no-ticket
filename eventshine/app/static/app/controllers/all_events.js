angular.module('app')
.controller('AllEventsCtrl', function($scope, $location, $http) {
  $http.get('/all_events').then(res => {
    console.log(res.data)
    $scope.events = res.data
  })
})
