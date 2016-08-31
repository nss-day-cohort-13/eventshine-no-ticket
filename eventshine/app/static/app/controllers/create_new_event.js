angular.module('app')
.controller("createNewEventCtrl", function($http, $location, $scope){
    const createNewEvent = this;
    createNewEvent.makeEvent = function() {
        console.log('This works');
        $http({
            url: '/new_event/',
            method: 'POST',
            headers: {'Content-Type':      'application/x-www-form-urlencoded'},
            data: {
                'eventname': createNewEvent.eventName,
                'eventdescription': createNewEvent.eventDescription,
                'eventcity': createNewEvent.eventCity,
                'eventvenue': createNewEvent.eventVenue,
                'eventattendeelimit': createNewEvent.eventAttendees,
                'eventstartdate': createNewEvent.eventStartDate,
                'eventenddate': createNewEvent.eventEndDate
            }
        }).success(() => {
            $location.path('/new_event_conf')
        })
    }
})
