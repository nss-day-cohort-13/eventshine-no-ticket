angular.module('app')

.controller('HomeCtrl', function($scope, $location, $http) {
  const register = this;
  console.log("i missed you");
  register.app_name = 'app'
  register.createUser = function() {
    // Construct $http POST verb XHR
    // console.log("register", register);
    $http({
      url: "/register/",
      method: "POST",
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: {
        "username": register.userName,
        "password": register.password,
        "email": register.email,
        "firstname": register.firstName,
        "lastname": register.lastName
      }
    }).then(() => {
      $location.path('/login')
    })
  }

})
