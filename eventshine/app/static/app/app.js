// The route provider. This is the main JS page.
angular.module('app', ['ngRoute', 'ui.bootstrap', 'ngCookies'])
  .config(($routeProvider, $httpProvider) => {
    // $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    // $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    // $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $routeProvider
    .when('/home', {
        templateUrl: '/static/app/partials/home.html',
        controller: 'HomeCtrl',
      })
    .when('/', {
          templateUrl: '/static/app/partials/login.html',
          controller: 'LoginCtrl',
        })
    .when('/events', {
        templateUrl: '/static/app/partials/events.html',
        controller: 'EventsCtrl',
      })
    .when('/tixit', {
        templateUrl: '/static/app/partials/tixit.html',
        controller: 'TixitCtrl',
      })
    .when('/new_event', {
        templateUrl: '/static/app/partials/new_event.html',
        controller: 'NewEventCtrl',
      })
    }
  )
  .run([
    '$http',
    '$cookies',
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    }]);
