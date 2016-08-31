angular.module('app').controller('NewEventCtrl', function(createNewEvent) {
    createNewEvent.today = function() {
        createNewEvent.dt = new Date();
        createNewEvent.dt2 = new Date();
    };
    createNewEvent.today();

    createNewEvent.clear = function() {
        createNewEvent.dt = null;
        createNewEvent.dt2 = null;
    };

    createNewEvent.inlineOptions = {
        customClass: getDayClass,
        minDate: new Date(),
        showWeeks: true
    };

    createNewEvent.dateOptions = {
        dateDisabled: disabled,
        formatYear: 'yy',
        maxDate: new Date(2020, 5, 22),
        minDate: new Date(),
        startingDay: 1
    };

    // Disable weekend selection
    function disabled(data) {
        var date = data.date,
            mode = data.mode;
        return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
    }

    createNewEvent.toggleMin = function() {
        createNewEvent.inlineOptions.minDate = createNewEvent.inlineOptions.minDate ? null : new Date();
        createNewEvent.dateOptions.minDate = createNewEvent.inlineOptions.minDate;
    };

    createNewEvent.toggleMin();

    createNewEvent.open1 = function() {
        createNewEvent.popup1.opened = true;
    };

    createNewEvent.open2 = function() {
        createNewEvent.popup2.opened = true;
    };

    createNewEvent.setDate = function(year, month, day) {
        createNewEvent.dt = new Date(year, month, day);
        createNewEvent.dt2 = new Date(year, month, day);
    };

    createNewEvent.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'MM/dd/yy', 'shortDate'];
    createNewEvent.format = createNewEvent.formats[3];
    createNewEvent.altInputFormats = ['M!/d!/yyyy'];

    createNewEvent.popup1 = {
        opened: false
    };

    createNewEvent.popup2 = {
        opened: false
    };

    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    var afterTomorrow = new Date();
    afterTomorrow.setDate(tomorrow.getDate() + 1);
    createNewEvent.events = [{
        date: tomorrow,
        status: 'full'
    }, {
        date: afterTomorrow,
        status: 'partially'
    }];

    function getDayClass(data) {
        var date = data.date,
            mode = data.mode;
        if (mode === 'day') {
            var dayToCheck = new Date(date).setHours(0, 0, 0, 0);

            for (var i = 0; i < createNewEvent.events.length; i++) {
                var currentDay = new Date(createNewEvent.events[i].date).setHours(0, 0, 0, 0);

                if (dayToCheck === currentDay) {
                    return createNewEvent.events[i].status;
                }
            }
        }

        return '';
    }
});
