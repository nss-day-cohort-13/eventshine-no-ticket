// The route provider. This is the main JS page.
angular.module('app', ['ngRoute', 'ui.bootstrap'])
  .config(($routeProvider) => (
    $routeProvider
    .when('/', {
        templateUrl: '/static/app/partials/home.html',
        controller: 'HomeCtrl',
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
    )
  )
