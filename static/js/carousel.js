angular.module('ui.bootstrap.demo').controller('CarouselDemoCtrl', function ($scope) {
  $scope.myInterval = 5000;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var slides = $scope.slides = ['/templates/images/wedding005-min.jpg', '/templates/images/wedding004-min.jpg', '/templates/images/wedding003-min.jpg', '/templates/images/ChristmasFayre-min.jpg', '/templates/images/NewLivery-min.jpg', '/templates/images/wedding001-min.jpg'];
  var currIndex = 0;