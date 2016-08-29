angular.module('app')

.controller('HomeCtrl', function($scope, $location, $http) {
  $http.get("http://localhost:8000/app/")
  .then((res) => $scope.remote_todos = res.data)

  $scope.User = function() {
    $scope.User.push({name: $scope.User});
  };
})
