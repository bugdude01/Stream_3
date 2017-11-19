angular.module('RouteControllers', [])
    .controller('HomeController', function($scope) {
        $scope.title = "home";
    })
    .controller('BookingController', function($scope, UserAPIService) {
        $scope.bookingUser = {};

        $scope.submitForm = function() {
            if ($scope.bookingForm.$valid) {
                $scope.bookingUser.name = $scope.user.name;
                $scope.bookingUser.email = $scope.user.email;
                $scope.bookingUser.homePhone = $scope.user.homePhone;
                $scope.bookingUser.mobilePhone = $scope.user.mobilePhone;
                $scope.bookingUser.date = $scope.user.date;
                $scope.bookingUser.eventType = $scope.user.eventType;
                $scope.bookingUser.guestNumber = $scope.user.guestNumber;
            }
 
            console.log($scope.bookingUser.name + " " + $scope.bookingUser.email + " " + $scope.bookingUser.homePhone
                 + " " + $scope.bookingUser.mobilePhone + " " + $scope.bookingUser.date + " " + $scope.bookingUser.eventType
                  + " " + $scope.bookingUser.guestNumber);
        };
    });
