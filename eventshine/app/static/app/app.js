// The route provider. This is the main JS page.
angular.module('app', ['ngRoute', 'ui.bootstrap'])
  .config(($routeProvider) => (
    $routeProvider
    .when('/events', {
        templateUrl: '/static/app/partials/events.html',
        controller: 'EventsCtrl',
      })
    )
  )
