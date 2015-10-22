/**
 * Directive: Officer <officer></officer>
 */
angular.module('GalacticApp')
  .directive('officer', function OfficerDrctv ($timeout) {
    'use strict';

    return {
      restrict: 'EA',
      replace: true,
      scope: true,
      templateUrl: "/static/app/components/officer/officer.tmpl.html",
      controllerAs: 'officer',

      controller: function ($routeParams, OfficerFactory) {
        this.officers = {};

        var fleetId = Number($routeParams.fleetId),
            shipId = Number($routeParams.shipId);

        this.goToShip = function() {
          OfficerFactory.goToShip(fleetId, shipId);
        };

        this.goToFleet = function() {
          OfficerFactory.goToFleet(fleetId);
        };

        this.goToCommand = function() {
          OfficerFactory.goToCommand();
        };

        OfficerFactory.getOfficer($routeParams)
          .then( angular.bind( this, function then() {
            this.officers = OfficerFactory.officers;
          }));
      },

      link: function(scope, element, attrs, ctrl) {
        /*
          by convention we do not $ prefix arguments to the link function
          this is to be explicit that they have a fixed order
        */
      }
    };


  });