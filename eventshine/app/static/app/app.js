// The route provider. This is the main JS page.
angular.module('app', ['ngRoute', 'ui.bootstrap', 'ngCookies'])
  .config(($routeProvider, $httpProvider, $interpolateProvider) => {
    // Lines 5 and 6: csrf token is a django thing (like an auth token but not actualy an auth token) that prevents bad-actor third parties from posting to the database in place of an authentic user. Sets Django token in javascript.
    $interpolateProvider.startSymbol('((');
    $interpolateProvider.endSymbol('))');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $routeProvider
    .when('/home', {
        templateUrl: '/static/app/partials/home.html',
        controller: 'registerCtrl',
        controllerAs: 'register'
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
        controller: 'createNewEventCtrl',
        controllerAs: 'createNewEvent'
      })
    .when('/new_event_conf', {
        templateUrl: '/static/app/partials/new_event_conf.html',
        controller: 'TixitCtrl',
      })
    .when('/all_events', {
        templateUrl: '/static/app/partials/all_events.html',
        controller: 'AllEventsCtrl',
      })
    }
  )
  .run([
    '$http',
    '$cookies',
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    }]);
