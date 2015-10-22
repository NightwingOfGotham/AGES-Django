/**
 * Directive: Ship <ship></ship>
 */
angular.module('GalacticApp')
  .directive('ship', function ShipDrctv ($timeout) {
    'use strict';

    return {
      restrict: 'EA',
      replace: true,
      scope: true,
      templateUrl: "/static/app/components/ship/ship.tmpl.html",
      controllerAs: 'ship',

      controller: function ($routeParams, ShipFactory) {
        this.officers = {};

        var fleetId = Number($routeParams.fleetId),
            shipId = Number($routeParams.shipId);

        this.goToOfficer = function(officerId) {
          ShipFactory.goToOfficer(fleetId, shipId, officerId);
        };

        this.goToFleet = function() {
          ShipFactory.goToFleet(fleetId);
        };

        this.goToCommand = function() {
          ShipFactory.goToCommand();
        };

        ShipFactory.getOfficers($routeParams.shipId)
          .then( angular.bind( this, function then() {
            this.officers = ShipFactory.officers;
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